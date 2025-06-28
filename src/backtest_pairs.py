import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
PAIR = ['HSBA.L', 'BARC.L']  # Change these to your chosen pair
Z_THRESHOLD = 1.0            # Entry threshold in z-score units

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
