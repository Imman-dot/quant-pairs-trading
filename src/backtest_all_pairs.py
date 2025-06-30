# src/backtest_all_pairs.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# === CONFIGURE PATHS ===
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR  = PROJECT_ROOT / "results"
FIGURES_DIR  = PROJECT_ROOT / "figures"
RESULTS_DIR.mkdir(exist_ok=True)
FIGURES_DIR.mkdir(exist_ok=True)

# === LOAD AND PIVOT DATA ===
df      = pd.read_csv(PROJECT_ROOT / "data" / "ftse350_prices.csv", parse_dates=["Date"])
df_wide = df.pivot(index="Date", columns="Ticker", values="Close")

# === COMPUTE CORRELATION MATRIX AND SHOW TOP PAIRS ===
corr = df_wide.corr()
mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
top_pairs = (
    corr.where(mask)  # keep only upper triangle
        .stack()     # turn into Series
        .sort_values(ascending=False)
)
print("Top 10 FTSE350 correlations:")
print(top_pairs.head(10))

# === IDENTIFY PAIRS ABOVE CORRELATION THRESHOLD ===
corr_threshold = 0.35
PAIRS = [(t1, t2) for t1, t2 in top_pairs.index if top_pairs.loc[(t1, t2)] >= corr_threshold]
print(f"\nBacktesting {len(PAIRS)} pairs with corr ≥ {corr_threshold}:\n", PAIRS)

# === BACKTEST LOOP ===
for t1, t2 in PAIRS:
    prices1 = df_wide[t1].dropna()
    prices2 = df_wide[t2].dropna()
    common  = prices1.index.intersection(prices2.index)
    prices1, prices2 = prices1.loc[common], prices2.loc[common]

    # SPREAD & Z-SCORE
    spread    = prices1 - prices2
    mean, std = spread.mean(), spread.std()
    zscore    = (spread - mean) / std

    # SIGNALS
    signals = pd.Series(0.0, index=spread.index)
    signals[zscore >  2.0] = -1  # short spread
    signals[zscore < -2.0] = +1  # long spread

    # RETURNS & EQUITY
    returns = (prices1.pct_change() - prices2.pct_change()) * signals.shift()
    equity  = returns.fillna(0).cumsum()

    # METRICS
    final_ret     = equity.iloc[-1]
    bench_ret     = (prices1.iloc[-1] / prices1.iloc[0]) - 1
    daily_rets    = returns.fillna(0)
    sharpe        = (daily_rets.mean() / daily_rets.std()) * np.sqrt(252)
    max_dd        = (equity - equity.cummax()).min()
    num_trades    = int(signals.diff().abs().sum())
    avg_ret_trade = final_ret / num_trades if num_trades else np.nan

    # SAVE SUMMARY
    summary_path = RESULTS_DIR / f"summary_{t1}_{t2}.txt"
    with open(summary_path, "w") as f:
        f.write(f"Pair: {t1} vs {t2}\n")
        f.write(f"Strategy Return: {final_ret:.2%}\n")
        f.write(f"Benchmark Return: {bench_ret:.2%}\n")
        f.write(f"Sharpe Ratio: {sharpe:.2f}\n")
        f.write(f"Max Drawdown: {max_dd:.2%}\n")
        f.write(f"Total Trades: {num_trades}\n")
        f.write(f"Avg Return/Trade: {avg_ret_trade:.2%}\n")

    # PLOT 1: Z-SCORE & SIGNALS
    plt.figure(figsize=(10,4))
    plt.plot(zscore.index, zscore, label="Z-score")
    plt.axhline( 2.0, color="r", linestyle="--")
    plt.axhline(-2.0, color="g", linestyle="--")
    buy  = zscore[signals==1];  sell = zscore[signals==-1]
    plt.scatter(buy.index, buy, marker="^", color="green", label="Long")
    plt.scatter(sell.index, sell, marker="v", color="red",   label="Short")
    plt.title(f"Z-Score & Signals: {t1} vs {t2}")
    plt.legend(); plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"signals_{t1}_{t2}.png")
    plt.close()

    # PLOT 2: CUMULATIVE RETURNS vs BENCHMARK
    cum_strat = (1 + daily_rets).cumprod()
    cum_bench = (1 + prices1.pct_change().fillna(0)).cumprod()
    plt.figure(figsize=(10,4))
    plt.plot(cum_strat.index, cum_strat, label="Strategy")
    plt.plot(cum_bench.index, cum_bench, label="Benchmark")
    plt.title(f"Cumulative Returns: {t1} vs {t2}")
    plt.legend(); plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"cumret_{t1}_{t2}.png")
    plt.close()

    # PLOT 3: HISTOGRAM OF DAILY RETURNS
    plt.figure(figsize=(8,4))
    plt.hist(daily_rets, bins=50)
    plt.title(f"Daily Returns Distribution: {t1} vs {t2}")
    plt.xlabel("Daily Return"); plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"hist_{t1}_{t2}.png")
    plt.close()

print(f"\n✅ Backtested and saved results for {len(PAIRS)} pairs.")
