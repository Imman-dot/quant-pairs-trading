import matplotlib.pyplot as plt
from pathlib import Path

# Ensure figures folder exists
FIGURES_DIR = Path(__file__).resolve().parent.parent / "figures"
FIGURES_DIR.mkdir(exist_ok=True)

# 1) Spread with Signals
Z_THRESHOLD = 2  # Set your desired z-score threshold here

# Example signal generation: signals = 1 for long, -1 for short, 0 otherwise
# Replace this logic with your actual signal generation if needed

# Dummy zscore and spread for demonstration; replace with your actual calculation
import numpy as np
import pandas as pd
np.random.seed(0)
spread = pd.Series(np.random.normal(0, 1, 252), name="spread")
zscore = (spread - spread.mean()) / spread.std()

signals = (zscore > Z_THRESHOLD).astype(int) - (zscore < -Z_THRESHOLD).astype(int)

plt.figure(figsize=(10,4))
plt.plot(spread.index, zscore, label="Z-score")
plt.axhline(Z_THRESHOLD, color='r', linestyle='--', label='+Threshold')
plt.axhline(-Z_THRESHOLD, color='g', linestyle='--', label='-Threshold')
# Mark entry/exit
buy = zscore[signals==1]; sell = zscore[signals==-1]
plt.scatter(buy.index, buy, marker='^', color='green', label='Long')
plt.scatter(sell.index, sell, marker='v', color='red', label='Short')
plt.title("Z-score & Trade Signals")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES_DIR / "signals_zscore.png")
plt.close()

# 2) Cumulative Returns vs. Benchmark
# Dummy cumulative_strategy and cumulative_benchmark for demonstration; replace with your actual calculation
cumulative_strategy = pd.Series(np.cumprod(1 + np.random.normal(0, 0.01, 252)), name="Strategy")
cumulative_benchmark = pd.Series(np.cumprod(1 + np.random.normal(0, 0.008, 252)), name="Benchmark")

plt.figure(figsize=(10,4))
plt.plot(cumulative_strategy.index, cumulative_strategy, label="Strategy")
plt.plot(cumulative_benchmark.index, cumulative_benchmark, label="Benchmark")
plt.title("Cumulative Returns Comparison")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES_DIR / "cumulative_returns.png")
plt.close()

# 3) Histogram of Daily Strategy Returns
# Ensure strategy_daily_returns is defined; replace the following line with your actual calculation if needed
# Example: strategy_daily_returns = cumulative_strategy.pct_change().dropna()
# Calculate daily returns from cumulative_strategy if not already defined
if 'strategy_daily_returns' not in locals():
	strategy_daily_returns = cumulative_strategy.pct_change().dropna()

plt.figure(figsize=(8,4))
plt.hist(strategy_daily_returns, bins=50)
plt.title("Distribution of Daily Strategy Returns")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "returns_histogram.png")
plt.close()

print("✅ Figures saved to figures/ directory")
