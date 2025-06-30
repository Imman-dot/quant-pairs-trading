import pandas as pd
import os

raw_dir = "data/raw"
for file in os.listdir(raw_dir):
    df = pd.read_csv(os.path.join(raw_dir, file))
    # Check for nonpositive prices or volumes
    mask = (df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] <= 0).any(axis=1)
    if mask.any():
        print(f"{file} has nonpositive values in rows:")
        print(df[mask])
    # Check for missing values
    if df.isna().sum().sum() > 0:
        print(f"{file} has missing data in rows:")
        print(df[df.isna().any(axis=1)])

# Clean a single file (example)
df = pd.read_csv("data/raw/HSBA.L.csv")
df = df[(df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] > 0).all(axis=1)]
df = df.dropna()
df.to_csv("data/raw/HSBA.L.csv", index=False)
print("Cleaned HSBA.L.csv and saved back to raw directory.")