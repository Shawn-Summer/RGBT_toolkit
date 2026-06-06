# -*- coding: utf-8 -*-

import os
from rgbt import RGBT234
rgbt234 = RGBT234()


"""
RGBT234 have 2 benchmarks: MPR MSR
"""

# Register your tracker by scanning all first-level subdirectories
results_dir = "../result/RGBT234"
if os.path.exists(results_dir):
    # Get all first-level subdirectories
    subdirs = [d for d in os.listdir(results_dir) if os.path.isdir(os.path.join(results_dir, d))]

    # Register each subdirectory as a tracker
    for subdir in subdirs:
        tracker_name = subdir  # Use directory name as tracker name
        result_path = os.path.join(results_dir, subdir)
        rgbt234(
            tracker_name=tracker_name,
            result_path=result_path,
            bbox_type="ltwh")

    print(f"Registered {len(subdirs)} trackers from {results_dir}")
else:
    print(f"Directory {results_dir} does not exist")


# Evaluate multiple trackers
mpr_dict = rgbt234.MPR()
msr_dict = rgbt234.MSR()

# Print all results
print("\n=== MSR Results ===")
for tracker in sorted(msr_dict.keys()):
    values = msr_dict[tracker]
    print(f"{tracker}: {values[0]}")

print("\n=== MPR Results ===")
for tracker in sorted(mpr_dict.keys()):
    values = mpr_dict[tracker]
    print(f"{tracker}: {values[0]}")



# # Evaluate single challenge
# pr_tc_dict = rgbt234.MPR(seqs=rgbt234.TC)
# sr_tc_dict = rgbt234.MSR(seqs=rgbt234.TC)

# 绘图功能
# rgbt234.draw_plot(metric_fun=rgbt234.MPR)
# rgbt234.draw_plot(metric_fun=rgbt234.MSR)
rgbt234.draw_attributeRadar(metric_fun=rgbt234.MSR)
