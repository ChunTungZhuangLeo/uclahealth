import os
import pandas as pd
import glob

# === CONFIGURATION ===
DATA_DIR = "/projects/bodymaps/Zhuang/ccvlWork/pamap2_dataset/unzipped/PAMAP2_Dataset/Protocol"
EXPECTED_ACTIVITIES = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 24]  # Full activity set

# Helper to load a .dat file
def load_subject_file(filepath):
    return pd.read_csv(filepath, sep=' ', header=None, usecols=[1], names=["activity"], engine="python")

# Collect activity distribution per subject
all_distributions = []

filepaths = sorted(glob.glob(os.path.join(DATA_DIR, "subject*.dat")))
for filepath in filepaths:
    df = load_subject_file(filepath)
    subject = os.path.basename(filepath)
    
    counts = df["activity"].value_counts().to_dict()
    
    # Fill in missing activity labels with zero
    full_counts = {label: counts.get(label, 0) for label in EXPECTED_ACTIVITIES}
    full_counts["subject"] = subject
    all_distributions.append(full_counts)

# Convert to DataFrame and save
distribution_df = pd.DataFrame(all_distributions)
distribution_df = distribution_df[["subject"] + EXPECTED_ACTIVITIES]  # Ensure correct column order
distribution_df.to_csv("pamap2_activity_distribution_full.csv", index=False)

print("✅ Saved full activity distribution to pamap2_activity_distribution_full.csv")
