import os
import glob

DATA_DIR = "/projects/bodymaps/Zhuang/ccvlWork/pamap2_dataset/unzipped/PAMAP2_Dataset/Protocol"

# Step 1: Define expected subject filenames
expected_subjects = [f"subject10{i}.dat" for i in range(1, 10)]  # subject101 to subject109

# Step 2: Get actual .dat files in folder
actual_subjects = sorted([os.path.basename(f) for f in glob.glob(os.path.join(DATA_DIR, "subject*.dat"))])

# Step 3: Check for missing and extra subjects
missing_subjects = sorted(list(set(expected_subjects) - set(actual_subjects)))
extra_subjects = sorted(list(set(actual_subjects) - set(expected_subjects)))

# Output
print("✅ Found Subjects:", actual_subjects)
print("❌ Missing Subjects:", missing_subjects)
print("🧐 Extra Subjects (not in expected list):", extra_subjects)
