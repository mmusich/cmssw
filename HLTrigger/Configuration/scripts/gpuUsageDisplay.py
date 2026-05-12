import sys
import math
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.colors import Normalize
from matplotlib.collections import LineCollection
from matplotlib.cm import get_cmap, ScalarMappable
import numpy as np
import mplhep as hep

hep.style.use("CMS")

def load_gpu_memory_csv(csv_path):
    """
    Load a CSV of the form:

        elapsed_seconds,cumulative_gpus_memory_usage
        0,0
        1,0
        ...

    where the header line is basically bogus for GPU columns.
    """
    # Skip the first row (header) and let pandas infer raw columns
    df = pd.read_csv(csv_path, header=None, skiprows=1)

    # First column = time, other = memory
    colnames = ["elapsed_seconds", "cumulative_memory_usage"]
    df.columns = colnames

    # Sort by time just in case
    df = df.sort_values("elapsed_seconds").reset_index(drop=True)
    return df

def load_gpu_csv(csv_path):
    """
    Load a CSV of the form:

        elapsed_seconds,gpus_usage
        0,0,0,0,0
        1,0,0,0,0
        ...

    where the header line is basically bogus for GPU columns.
    """
    # Skip the first row (header) and let pandas infer raw columns
    df = pd.read_csv(csv_path, header=None, skiprows=1)

    # First column = time, others = GPUs
    n_gpus = df.shape[1] - 1
    colnames = ["elapsed_seconds"] + [f"gpu{i}" for i in range(n_gpus)]
    df.columns = colnames

    # Sort by time just in case
    df = df.sort_values("elapsed_seconds").reset_index(drop=True)
    return df

def plot_gpu_line(df, filter=None, title=None, draw_percent=True, saveImages=False, image_output="default"):
    gpu_cols = [c for c in df.columns if c.startswith("gpu")]

    if filter:
        import re
        def filter_cols():
            return [c for c in df.columns if re.match(filter, c)]
        gpu_cols = filter_cols()

    times = df["elapsed_seconds"].to_numpy(float)

    cmap = get_cmap("coolwarm")  # Blue->White->Red

    for col in gpu_cols:

        values = df[col].to_numpy(float)

        if draw_percent:
           norm = Normalize(0, 100)     # Map values from 0-100%
        else:
           norm = Normalize(0, values.max())

        # Construct line segments from adjacent points
        points = np.array([times, values]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        lc = LineCollection(segments, cmap=cmap, norm=norm)
        lc.set_array(values)
        lc.set_linewidth(2.0)

        fig, ax = plt.subplots(figsize=(12, 4))
        ax.add_collection(lc)

        ax.set_xlim(times.min(), times.max())
        if draw_percent:
            ax.set_ylim(0, 100)  # GPU utilization range
        else:
            ax.set_ylim(0, 1.05*values.max())
        ax.set_xlabel("Elapsed Seconds", fontsize=12)
        ax.set_ylabel(f"{col.upper()}", fontsize=12)
        if title:
            ax.set_title(title, fontsize=12)
#        ax.set_title(f"GPU Utilization Line - {col.upper()}", fontsize=12)

        # Colorbar
        cbar = fig.colorbar(lc, ax=ax)
        cbar.set_label(f"{col.upper()}", fontsize=12)
        cbar.ax.tick_params(labelsize=12)

        ax.grid(True, linestyle="--", alpha=0.6)
        ax.tick_params(axis="both", labelsize=12)

        # CMS text overlay with smaller font
        hep.cms.text("Phase-2 Simulation Preliminary", ax=ax, fontsize=12)
        hep.cms.lumitext(
            col.upper(),
            ax=ax,
            fontsize=12,
        )
        plt.tight_layout()

        # Save the figure
        if saveImages:
            plt.savefig(f"{image_output}.png", dpi=300)   # High-resolution PNG
            plt.savefig(f"{image_output}.pdf")            # Vector PDF

        plt.show()

def compute_weighted_average(df, threshold=1.0, filter=None):
    """
    Time-weighted average per GPU, ignoring all intervals where usage <= threshold.

    For each interval [t_i, t_{i+1}), we assume usage is df[gpu][i].
    Only intervals with usage > threshold are included in the average.
    """
    gpu_cols = [c for c in df.columns if c.startswith("gpu")]
    if filter:
        import re
        def filter_cols():
            return [c for c in df.columns if re.match(filter, c)]
        gpu_cols = filter_cols()
    times = df["elapsed_seconds"].to_numpy(float)

    if len(times) < 2:
        print("Not enough samples to compute time-weighted averages.")
        return

    # Durations between consecutive samples (one per interval)
    diffs = np.diff(times)  # length N-1
    total_time = diffs.sum()

    print(f"\n----------- Time-Weighted GPU Averages (filtered at {threshold:.2f}%) -----------")
    print(f"Activity threshold: {threshold}% (intervals at/under this are ignored)\n")

    for col in gpu_cols:
        usage = df[col].to_numpy(float)

        # Interval usages: usage[i] applies to [t_i, t_{i+1})
        interval_usages = usage[:-1]   # length N-1
        interval_widths = diffs        # length N-1

        # Keep only intervals above threshold
        mask = interval_usages > threshold
        if not mask.any():
            print(f"{col.upper():<6}: No intervals above {threshold}% threshold")
            continue

        kept_usages = interval_usages[mask]
        kept_widths = interval_widths[mask]

        active_time = kept_widths.sum()
        weighted_avg = np.average(kept_usages, weights=kept_widths)

        print(
            f"{col.upper():<6}: {weighted_avg:6.2f} "
            f"(active time {active_time:.1f}s / total {total_time:.1f}s)"
        )

    print("------------------------------------------------------------\n")

def print_average_usage(df, filter=None):
    gpu_cols = [c for c in df.columns if c.startswith("gpu")]
    if filter:
        import re
        def filter_cols():
            return [c for c in df.columns if re.match(filter, c)]
        gpu_cols = filter_cols()
    print("\n---------------- FLAT GPU Usage Averages ----------------")
    for col in gpu_cols:
        mean_val = df[col].mean()
        max_val = df[col].max()
        min_val = df[col].min()
        print(f"{col.upper():<6}: Mean: {mean_val:6.2f}, Min: {min_val:6.2f}, Max: {max_val:6.2f}")
    print("---------------------------------------------------\n")

for streams in [4, 8, 12, 16, 20, 24, 28, 30, 32]:
    basename = f"gpu_usage_NGTScouting_8j_32t_{streams}s_workflow6_1GPU"
    images = f"Images/{basename}"
    title = f"8j_32t_{streams}s"
    df = utils.load_gpu_csv(f"GPUUsageByWorkflow/{basename}.csv")
    utils.print_average_usage(df, "gpu0")
    utils.compute_weighted_average(df, threshold=10, filter="gpu0")
    utils.plot_gpu_line(df, filter="gpu0", title=title, saveImages=True, image_output=f"{images}")
