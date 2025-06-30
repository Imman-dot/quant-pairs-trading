import os
import pandas as pd

RAW_DIR = "data/raw"

for filename in os.listdir(RAW_DIR):
    if not filename.endswith(".csv"):
        continue
    path = os.path.join(RAW_DIR, filename)
    print(f"Cleaning {filename}...")
    df = pd.read_csv(path)
    # Remove rows with any nonpositive price or volume
    df = df[(df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] > 0).all(axis=1)]
    # Remove rows with any missing values
    df = df.dropna()
    # Save cleaned data back to the file (overwrite original)
    df.to_csv(path, index=False)
    print(f"  Remaining rows: {len(df)}")

print("✅ All files cleaned! Run your checker again to verify.")
