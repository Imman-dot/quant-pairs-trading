import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

# Determine project root (one level up from this script)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR   = PROJECT_ROOT / "results"
RESULTS_DIR.mkdir(exist_ok=True)   # create it if it doesn't exist

SUMMARY_FILE = RESULTS_DIR / "summary.txt"


# --- Parameters ---
PAIR = ['VOD.L', 'BARC.L']  # Change these to your chosen pair
Z_THRESHOLD = 2.0            # Entry threshold in z-score units

# --- Load data ---
df = pd.read_csv("data/ftse350_prices.csv", parse_dates=["Date"])
df_wide = df.pivot(index="Date", columns="Ticker", values="Close")
prices1 = df_wide[PAIR[0]]
prices2 = df_wide[PAIR[1]]

# --- Compute spread ---
spread = prices1 - prices2
mean = spread.mean()
std = spread.std()
zscore = (spread - mean) / std

# --- Trading signals ---
# Long spread (buy 1, sell 2) when spread is low
# Short spread (sell 1, buy 2) when spread is high
signals = pd.Series(index=spread.index, dtype=float)
signals[zscore >  Z_THRESHOLD] = -1    # Short spread
signals[zscore < -Z_THRESHOLD] = +1    # Long spread
signals = signals.fillna(0)

# --- Track position & simple returns (not compounded) ---
returns = (prices1.pct_change() - prices2.pct_change()) * signals.shift()
equity = returns.cumsum().fillna(0)

# --- Plot ---
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(spread.index, spread, label="Spread")
plt.axhline(mean, color='gray', linestyle='--', label='Mean')
plt.axhline(mean+std, color='red', linestyle=':', label='+1 std')
plt.axhline(mean-std, color='green', linestyle=':', label='-1 std')
plt.title(f"Spread between {PAIR[0]} and {PAIR[1]}")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(equity.index, equity, label='Cumulative PnL')
plt.title("Strategy Cumulative Profit/Loss")
plt.xlabel("Date")
plt.ylabel("Cumulative Returns")
plt.legend()

plt.tight_layout()
plt.show()

print(f"Final strategy return: {equity[-1]:.2%}")

print("Unique signals:", signals.unique())
print("Number of trades triggered:", (signals != 0).sum())

import numpy as np

trade_signals = signals.diff().fillna(0).abs()  # Points where position changes
num_trades = int((trade_signals > 0).sum())
total_pnl = equity.iloc[-1]
average_pnl = total_pnl / num_trades if num_trades > 0 else np.nan

print(f"Total number of trades: {num_trades}")
print(f"Final strategy return: {total_pnl:.2%}")
print(f"Average return per trade: {average_pnl:.4%}")


# Calculate returns as decimal
final_strategy_return = equity.iloc[-1]
final_benchmark_return = (prices1.iloc[-1] / prices1.iloc[0]) - 1

# Calculate Sharpe Ratio (annualized, risk-free rate assumed 0)
# Note: 252 trading days in a year
strategy_daily_returns = returns.fillna(0)
sharpe_ratio = (strategy_daily_returns.mean() / strategy_daily_returns.std()) * np.sqrt(252)

# Calculate Max Drawdown
cum_max = equity.cummax()
drawdown = equity - cum_max
max_drawdown = drawdown.min()


with open(SUMMARY_FILE, "w") as f:
    f.write(f"Final Strategy Return: {final_strategy_return:.2%}\n")
    f.write(f"Final Benchmark Return: {final_benchmark_return:.2%}\n")
    f.write(f"Sharpe Ratio: {sharpe_ratio:.2f}\n")
    f.write(f"Max Drawdown: {max_drawdown:.2%}\n")
    f.write(f"Total number of trades: {num_trades}\n")
    f.write(f"Average return per trade: {average_pnl:.4%}\n")



