# src/collect_summaries.py

import pandas as pd
import re
from pathlib import Path

# Path to your results folder
RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"

records = []

for path in RESULTS_DIR.glob("summary_*.txt"):
    lines = path.read_text().splitlines()
    # Initialize placeholders
    pair = None
    strat_ret = bench_ret = sharpe = maxdd = None
    trades = avgpt = None

    for line in lines:
        if line.startswith("Pair:"):
            pair = line.split(":", 1)[1].strip()

        elif line.startswith("Strategy Return:"):
            m = re.search(r"([-]?\d+\.?\d*)%", line)
            strat_ret = float(m.group(1)) / 100 if m else None

        elif line.startswith("Benchmark Return:"):
            m = re.search(r"([-]?\d+\.?\d*)%", line)
            bench_ret = float(m.group(1)) / 100 if m else None

        elif line.startswith("Sharpe Ratio:"):
            m = re.search(r"Sharpe Ratio:\s*([-]?\d+\.?\d*)", line)
            sharpe = float(m.group(1)) if m else None

        elif line.startswith("Max Drawdown:"):
            m = re.search(r"([-]?\d+\.?\d*)%", line)
            maxdd = float(m.group(1)) / 100 if m else None

        elif line.startswith("Total Trades:"):
            trades = int(line.split(":", 1)[1].strip())

        elif line.startswith("Avg Return/Trade:"):
            m = re.search(r"([-]?\d+\.?\d*)%", line)
            avgpt = float(m.group(1)) / 100 if m else None

    # Append a record for this pair
    records.append({
        "pair": pair,
        "strategy_return": strat_ret,
        "benchmark_return": bench_ret,
        "sharpe": sharpe,
        "max_drawdown": maxdd,
        "num_trades": trades,
        "avg_return_per_trade": avgpt
    })

# Build a DataFrame and sort by Sharpe (or any metric you choose)
df = pd.DataFrame(records)
df = df.sort_values("sharpe", ascending=False)

# Save a master CSV and print it out
master_csv = RESULTS_DIR / "all_pairs_summary.csv"
df.to_csv(master_csv, index=False)
print("Master summary:")
print(df)

print(f"\n✅ Saved combined summary to {master_csv}")

