import os
import glob

DATA_DIR = "/projects/bodymaps/Zhuang/ccvlWork/pamap2_dataset/unzipped/PAMAP2_Dataset/Protocol"
subject_files = sorted(glob.glob(os.path.join(DATA_DIR, "subject*.dat")))

for file in subject_files:
    df = pd.read_csv(file, sep=' ', header=None, usecols=[1])
    df = df.dropna()
    df = df.astype(int)
    counts = df[1].value_counts().sort_index()
    print(f"Activity distribution for {os.path.basename(file)}:")
    print(counts, "\n")
