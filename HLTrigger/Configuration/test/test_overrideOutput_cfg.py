#!/usr/bin/env python3
import os
import sys
import subprocess
import importlib.util

from HLTrigger.Configuration.Tools.confdb import HLTProcess

# --- Minimal config object for HLTProcess ---
class _DummyConfig:
    def __init__(self, output):
        self.hilton   = False
        self.fragment = False
        self.output   = output  # "minimal", "all", or "full"


def _load_menu_safely():
    """
    Import OnLine_HLT_GRun.py while hiding our argv so VarParsing in
    customizeHLTforALL doesn't see extra tokens like 'minimal'.
    """
    argv_saved = sys.argv[:]
    sys.argv = [argv_saved[0]]  # present a clean argv

    menu_path = os.path.join(
        os.environ["CMSSW_BASE"],
        "src/HLTrigger/Configuration/test/OnLine_HLT_GRun.py"
    )
    spec = importlib.util.spec_from_file_location("OnLine_HLT_GRun", menu_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    sys.argv = argv_saved  # restore
    return mod.process


def _build_hltprocess(output_mode: str) -> HLTProcess:
    """
    Wrap the loaded process text into an HLTProcess so we can call overrideOutput().
    """
    process = _load_menu_safely()

    # Build an HLTProcess instance without running its __init__ (which would query ConfDB)
    cfg = _DummyConfig(output=output_mode)
    hlt = HLTProcess.__new__(HLTProcess)
    hlt.config  = cfg
    hlt.data    = process.dumpPython()  # text that customize/overrideOutput operates on
    hlt.source  = ['/store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/593/00000/91a08676-199e-404c-9957-f72772ef1354.root']
    hlt.parent  = []
    hlt.options = {k: [] for k in
                   ['essources','esmodules','modules','sequences','services','paths','psets','blocks']}
    hlt.labels  = {'process': 'process', 'dict': 'process.__dict__'}
    return hlt


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 test_overrideOutput_cfg.py [minimal|all|full]")
        sys.exit(1)

    mode = sys.argv[1]
    if mode not in ("minimal", "all", "full"):
        print(f"Do not understand command '{mode}'")
        sys.exit(1)

    # Build HLTProcess around the real menu text
    hlt = _build_hltprocess(mode)

    # Apply only the output override (no other custom steps)
    hlt.overrideOutput()

    # Make the job runnable without input files
    # (append to the text, then finalize with hlt.dump() to substitute %(process)s)
    hlt.data += """
# --- test harness tweaks ---
%(process)s.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(2))
"""

    # IMPORTANT: finalize substitutions for %(process)s / %(dict)s placeholders
    cfg_text = hlt.dump()

    # Write config
    cfg_path = f"override_{mode}_cfg.py"
    with open(cfg_path, "w") as f:
        f.write(cfg_text)
    print(f"[ok] Wrote {cfg_path}")

    # Run cmsRun on the generated config
    print(f"[run] cmsRun -j job_{mode}.xml {cfg_path}")
    result = subprocess.run(
        ["cmsRun", "-j", f"job_{mode}.xml", cfg_path],
        stdout=sys.stdout,
        stderr=sys.stderr
    )
    if result.returncode != 0:
        raise SystemExit(result.returncode)
    print("[ok] cmsRun completed successfully")


if __name__ == "__main__":
    main()

# #!/usr/bin/env python3

# import os
# import sys
# import importlib.util
# from HLTrigger.Configuration.Tools.confdb import HLTProcess

# # --- small dummy config class, mimicking HLTProcess expectations ---
# class DummyConfig:
#     def __init__(self, output):
#         self.hilton   = False
#         self.fragment = False
#         self.output   = output


# def make_config(output_mode):
#     """
#     Import OnLine_HLT_GRun.py with a clean sys.argv, and wrap the process
#     into an HLTProcess instance for manipulation.
#     """
#     # save sys.argv so VarParsing in OnLine_HLT_GRun.py doesn't see our arg
#     argv_save = sys.argv[:]
#     sys.argv = [argv_save[0]]

#     # locate the menu file
#     menu_path = os.path.join(
#         os.environ["CMSSW_BASE"],
#         "src/HLTrigger/Configuration/test/OnLine_HLT_GRun.py"
#     )

#     # import OnLine_HLT_GRun.py as module
#     spec = importlib.util.spec_from_file_location("OnLine_HLT_GRun", menu_path)
#     menu = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(menu)

#     # restore sys.argv
#     sys.argv = argv_save

#     process = menu.process

#     # build an HLTProcess wrapper around the dumped python
#     cfg = DummyConfig(output=output_mode)
#     hlt = HLTProcess.__new__(HLTProcess)
#     hlt.config  = cfg
#     hlt.data    = process.dumpPython()
#     hlt.source  = []
#     hlt.parent  = []
#     hlt.options = {k: [] for k in
#                    ['essources','esmodules','modules',
#                     'sequences','services','paths','psets','blocks']}
#     hlt.labels  = {'process':'process','dict':'process.__dict__'}

#     return process, hlt


# def run_case(mode):
#     """
#     Build a config for a given mode and run cmsRun on it.
#     """
#     process, hlt = make_config(mode)

#     # apply overrideOutput
#     hlt.overrideOutput()

#     # write out the modified config
#     cfg_name = f"override_{mode}_cfg.py"
#     with open(cfg_name, "w") as out:
#         out.write(hlt.data)

#     print(f"Created {cfg_name}, running cmsRun...")
#     ret = os.system(f"cmsRun -j job_{mode}.xml {cfg_name}")
#     if ret != 0:
#         raise RuntimeError(f"cmsRun failed for mode {mode} with status {ret}")


# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python3 test_overrideOutput_cfg.py [minimal|all|full]")
#         sys.exit(1)

#     mode = sys.argv[1]
#     if mode not in ("minimal", "all", "full"):
#         print(f"Do not understand command '{mode}'")
#         sys.exit(1)

#     run_case(mode)

# #!/usr/bin/env python3
# import sys, os, types, importlib.util
# import FWCore.ParameterSet.Config as cms

# from HLTrigger.Configuration.Tools.confdb import HLTProcess

# class DummyMenu:
#     # minimal menu-like object, HLTProcess only needs these attributes
#     def __init__(self):
#         self.version  = None
#         self.database = None
#         self.name     = "GRun"
#         self.run      = None

# class DummyConfig:
#     def __init__(self, output):
#         self.fragment   = False
#         self.hilton     = False
#         self.output     = output  # <<<<<<<<<< key
#         self.type       = "GRun"
#         self.events     = 5
#         self.globaltag  = None
#         self.data       = True
#         self.prescale   = None
#         self.menu       = DummyMenu()
#         self.proxy      = None
#         self.proxy_host = None
#         self.proxy_port = None
#         self.tunnel     = None
#         self.tunnel_port= None
#         self.customise  = None
#         self.l1         = types.SimpleNamespace(override=None)
#         self.l1Xml      = types.SimpleNamespace(XmlFile=None)
#         self.emulator   = None

# def make_config(output_mode):
#     # load the real HLT menu
#     menu_path = os.path.join(os.environ["CMSSW_BASE"], "src/HLTrigger/Configuration/test/OnLine_HLT_GRun.py")
#     spec = importlib.util.spec_from_file_location("OnLine_HLT_GRun", menu_path)
#     menu = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(menu)
#     process = menu.process

#     # build HLTProcess around DummyConfig
#     cfg = DummyConfig(output=output_mode)
#     hlt = HLTProcess.__new__(HLTProcess)  # bypass normal __init__
#     hlt.config = cfg
#     hlt.data   = process.dumpPython()     # this is what customize() operates on
#     hlt.source = []
#     hlt.parent = []
#     hlt.options= {k:[] for k in ['essources','esmodules','modules','sequences','services','paths','psets','blocks']}
#     hlt.labels = {'process':'process','dict':'process.__dict__'}

#     return process, hlt

# def run_case(mode):
#     process, hlt = make_config(mode)
#     hlt.customize()  # calls overrideOutput internally
#     cfg_py = f"test_Online_HLT_GRun_{mode}.py"
#     with open(cfg_py, "w") as f:
#         f.write(hlt.data % hlt.labels)
#     print(f"Wrote {cfg_py}")
#     return cfg_py

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: test_overrideOutput_cfg.py [minimal|all|full]")
#         sys.exit(1)
#     cfg_py = run_case(sys.argv[1])
#     # now run cmsRun on the produced config
#     os.system(f"cmsRun {cfg_py}")
