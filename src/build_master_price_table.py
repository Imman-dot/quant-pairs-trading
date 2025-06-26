"""
build_master_price_table.py
Combine every CSV in data/raw/ into one master table.
Run:
    python src/build_master_price_table.py
Output:
    data/ftse350_prices.csv
"""
from pathlib import Path
import pandas as pd

RAW_DIR = Path("data", "raw")
out_path = Path("data", "ftse350_prices.csv")

frames = []

for csv_file in RAW_DIR.glob("*.csv"):          # loop over every raw price file
    ticker = csv_file.stem                      # filename without .csv  -> ticker
    df = pd.read_csv(csv_file, parse_dates=["Date"])
    df["Ticker"] = ticker                       # add a Ticker column
    frames.append(df)

if not frames:
    raise SystemExit("❌ No files found in data/raw. Run bulk_download first.")

master = pd.concat(frames, ignore_index=True)
master.to_csv(out_path, index=False)
print(f"✅ Saved combined file → {out_path.resolve()}  ({len(master):,} rows)")
