import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# === CONFIGURATION ===
PAIR = ['HSBA.L', 'BARC.L']
DATA_PATH = Path("data/ftse350_prices.csv")

# === LOAD DATA ===
df = pd.read_csv(DATA_PATH, parse_dates=["Date"])
df_wide = df.pivot(index="Date", columns="Ticker", values="Close")
prices1 = df_wide[PAIR[0]]
prices2 = df_wide[PAIR[1]]

# === CALCULATE SPREAD/Z-SCORE ===
spread = prices1 - prices2
mean = spread.mean()
std = spread.std()
zscore = (spread - mean) / std

# === SIGNAL GENERATION ===
signals = pd.Series(index=spread.index, dtype=float)
signals[zscore > 1] = -1   # Short 1st, Long 2nd
signals[zscore < -1] = 1   # Long 1st, Short 2nd
signals = signals.ffill().fillna(0)

# === PLOT ===
plt.figure(figsize=(14, 6))
plt.plot(spread.index, zscore, label='Z-score')
plt.axhline(1, color='r', linestyle='--', label='Sell threshold')
plt.axhline(-1, color='g', linestyle='--', label='Buy threshold')
plt.axhline(0, color='black', linestyle='-')

# Mark signals
buy_signals = zscore[signals == 1]
sell_signals = zscore[signals == -1]
plt.plot(buy_signals.index, buy_signals, '^', markersize=10, color='green', label='Buy Signal')
plt.plot(sell_signals.index, sell_signals, 'v', markersize=10, color='red', label='Sell Signal')

plt.legend()
plt.title("Z-score with Buy/Sell Signals")
plt.tight_layout()
plt.show()
