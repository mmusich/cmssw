#!/usr/bin/env python3
import importlib.util
import os
import tempfile, shutil
import subprocess
import sys

from HLTrigger.Configuration.Tools.confdb import HLTProcess
import FWCore.ParameterSet.Config as cms

class _DummyConfig:
    """Minimal config to drive HLTProcess.overrideOutput()."""
    def __init__(self, output):
        self.hilton   = False
        self.fragment = False
        self.output   = output  # "minimal", "all", or "full"

def _load_menu():
    """Generate a Run3 HLT menu with cmsDriver and load the process object."""

    with tempfile.TemporaryDirectory() as tmpdir:
        menu_path = os.path.join(tmpdir, "myMenu.py")

        # Run cmsDriver
        cmsdriver_cmd = [
            "cmsDriver.py",
            "TEST",
            "-s", "L1REPACK:uGT,HLT:GRun",
            "--data",
            "--scenario=pp",
            "-n", "1",
            "--conditions", "auto:run3_hlt_GRun",
            "--datatier", "RAW",
            "--eventcontent", "RAW",
            "--era", "Run3",
            "--process", "reHLT",
            "--no_exec",
            "--python_filename", menu_path,
        ]

        subprocess.run(cmsdriver_cmd, check=True)

        # Import the generated configuration
        spec = importlib.util.spec_from_file_location("myMenu", menu_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        return mod.process
                
def _prune_all_outputs(process):
    """Remove ALL existing output modules and any EndPaths that carry them (and unschedule them)."""
    # Collect current output modules
    outputs = list(process.outputModules_())
    if not outputs:
        return

    # Identify EndPaths that contain those outputs
    endpaths_to_remove = []
    try:
        ep_items = process.endpaths_().items()   # available in CMSSW python API
    except Exception:
        ep_items = []
    for ep_name, ep in ep_items:
        try:
            if any(lbl in ep.moduleNames() for lbl in outputs):
                endpaths_to_remove.append(ep_name)
        except Exception:
            pass

    # Unschedule those EndPaths first (if schedule exists)
    if hasattr(process, "schedule") and process.schedule is not None:
        for ep_name in endpaths_to_remove:
            ep = getattr(process, ep_name, None)
            if ep is not None:
                try:
                    process.schedule.remove(ep)
                except Exception:
                    pass

    # Drop EndPaths
    for ep_name in endpaths_to_remove:
        if hasattr(process, ep_name):
            delattr(process, ep_name)

    # Drop the output modules
    for lbl in outputs:
        if hasattr(process, lbl):
            delattr(process, lbl)

def _build_hltprocess_from(process, output_mode: str, input_file: str) -> HLTProcess:
    """Seed an HLTProcess with the (possibly pruned) process text."""
    cfg = _DummyConfig(output=output_mode)
    hlt = HLTProcess.__new__(HLTProcess)  # bypass __init__ (no ConfDB query)
    hlt.config  = cfg
    hlt.config.parent = None
    hlt.config.input = input_file
    hlt.config.emulator = "uGT"
    hlt.data    = process.dumpPython()
    hlt.parent  = []
    hlt.options = {k: [] for k in
                   ['essources','esmodules','modules','sequences','services','paths','psets','blocks']}
    hlt.labels  = {'process': 'process', 'dict': 'process.__dict__'}
    return hlt

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 test_overrideOutput_cfg.py [minimal|all|full] [input_file.root]")
        sys.exit(1)

    mode = sys.argv[1]
    infile = sys.argv[2]

    if mode not in ("minimal", "all", "full"):
        print(f"Do not understand command '{mode}'")
        sys.exit(1)

    # 1) Load the real menu
    process = _load_menu()

    # 2) For minimal/full, prune existing outputs so we end up with ONLY the requested one
    if mode in ("minimal", "full"):
        _prune_all_outputs(process)
        # sanity: should be empty now
        assert len(process.outputModules_()) == 0, "Output pruning failed: outputs still present"

    # 3) Wrap in HLTProcess and apply overrideOutput()
    hlt = _build_hltprocess_from(process, mode, infile)
    hlt.overrideOutput()
    hlt.build_source()
        
    # 4) Make the job runnable without input files
    hlt.data += """
# --- test harness tweaks ---
%(process)s.options.wantSummary = cms.untracked.bool(False)
"""

    # 5) Finalize substitutions and write cfg
    cfg_text = hlt.dump()
    cfg_path = f"override_{mode}_cfg.py"
    with open(cfg_path, "w") as f:
        f.write(cfg_text)
    print(f"[ok] wrote {cfg_path}")

    # Optional: quick check of outputs in the final text (informational)
    if mode in ("minimal", "full"):
        expect = "hltOutputMinimal" if mode == "minimal" else "hltOutputFull"
        if expect not in cfg_text:
            print(f"[warn] expected {expect} not found in generated cfg")

    # 6) Run cmsRun
    print(f"[run] cmsRun -j job_{mode}.xml {cfg_path}")
    ret = subprocess.run(["cmsRun", "-j", f"job_{mode}.xml", cfg_path])
    sys.exit(ret.returncode)

if __name__ == "__main__":
    main()
