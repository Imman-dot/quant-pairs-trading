import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PAIR = ['VOD.L', 'BARC.L']
df = pd.read_csv("data/ftse350_prices.csv", parse_dates=["Date"])
df_wide = df.pivot(index="Date", columns="Ticker", values="Close")

# Get close prices
prices1 = df_wide[PAIR[0]]
prices2 = df_wide[PAIR[1]]

# Calculate spread and z-score
spread = prices1 - prices2
mean = spread.mean()
std = spread.std()
zscore = (spread - mean) / std

# Generate signals
signals = pd.Series(index=spread.index, dtype=float)
signals[zscore > 1] = -1
signals[zscore < -1] = 1
signals = signals.ffill().fillna(0)

# Daily % returns
ret1 = prices1.pct_change().fillna(0)
ret2 = prices2.pct_change().fillna(0)

# Strategy return = ret1 * signal + ret2 * (-signal)
strategy_returns = ret1 * signals + ret2 * -signals
cumulative_strategy = (1 + strategy_returns).cumprod()

# Benchmark: long both stocks equally
benchmark_returns = (ret1 + ret2) / 2
cumulative_benchmark = (1 + benchmark_returns).cumprod()

# Plot returns
plt.figure(figsize=(12, 6))
plt.plot(cumulative_strategy.index, cumulative_strategy, label="Strategy")
plt.plot(cumulative_benchmark.index, cumulative_benchmark, label="Buy & Hold Both")
plt.title("Cumulative Returns")
plt.xlabel("Date")
plt.ylabel("Return (Growth of £1)")
plt.legend()
plt.tight_layout()
plt.show()

# Print final stats
print("Final Strategy Return:", f"{cumulative_strategy.iloc[-1] - 1:.2%}")
print("Final Benchmark Return:", f"{cumulative_benchmark.iloc[-1] - 1:.2%}")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ftse350_prices.csv", parse_dates=["Date"])
df_wide = df.pivot(index="Date", columns="Ticker", values="Close")
PAIR = ['HSBA.L', 'BARC.L']

p1 = df_wide[PAIR[0]]
p2 = df_wide[PAIR[1]]
spread = p1 - p2
ret1 = p1.pct_change().fillna(0)
ret2 = p2.pct_change().fillna(0)

thresholds = [0.5, 1.0, 1.5, 2.0]
print("Z-score Thresholds Backtest:")
print("-" * 35)

returns = []
trades = []
for t in thresholds:
    z = (spread - spread.mean()) / spread.std()
    
    signals = pd.Series(index=z.index, dtype=float)
    signals[z > t] = -1
    signals[z < -t] = 1
    signals = signals.ffill().fillna(0)

    strat_ret = ret1 * signals + ret2 * -signals
    cumulative = (1 + strat_ret).cumprod()

    final_return = cumulative.iloc[-1] - 1
    num_trades = (signals.diff().abs() > 0).sum()

    returns.append(final_return * 100)  # Store as percent
    trades.append(num_trades)

    print(f"Threshold ±{t:.1f} | Return: {final_return:.2%} | Trades: {num_trades}")

import numpy as np

def sharpe_ratio(returns, risk_free_rate=0):
    # Annualize assuming 252 trading days
    excess_ret = returns - risk_free_rate / 252
    return np.sqrt(252) * excess_ret.mean() / excess_ret.std()

def max_drawdown(cumulative_returns):
    running_max = cumulative_returns.cummax()
    drawdown = (cumulative_returns - running_max) / running_max
    return drawdown.min()

# Assume you've already run code for signals and cumulative_strategy for threshold 1.0
daily_returns = strategy_returns   # Your calculated strategy daily returns
cumulative = (1 + daily_returns).cumprod()

sharpe = sharpe_ratio(daily_returns)
drawdown = max_drawdown(cumulative)

print(f"Sharpe Ratio: {sharpe:.2f}")
print(f"Max Drawdown: {drawdown:.2%}")

with open("results/summary_thresholds.txt", "w") as f:
    for thresh, ret, ntrades in zip(thresholds, returns, trades):
        f.write(f"Threshold ±{thresh} | Return: {ret:.2f}% | Trades: {ntrades}\n")
