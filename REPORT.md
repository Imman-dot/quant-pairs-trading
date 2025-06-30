FTSE 350 Sector-Based Pairs-Trading Backtest

I built and backtested a market-neutral, mean-reversion strategy on highly correlated FTSE 350 stock pairs. Using a simple ±2 σ Z-score trigger, the top duo (HSBA.L vs BARC.L) returned 45 % with a Sharpe of 1.20 and a max drawdown of –12 %, comfortably beating an 18 % buy-and-hold benchmark.

What It Does
• Screens all FTSE 350 stocks for pairwise Pearson correlations ≥ 0.70
• Calculates the spread (price difference) for each pair, standardizes it into a Z-score
• When yesterday’s Z-score > +2 → short the spread (sell the expensive stock, buy the cheap)
• When yesterday’s Z-score < –2 → long the spread (buy the cheap, sell the expensive)
• Exit as soon as |Z| ≤ 1; size each leg equally ($1 notional) and shift signals by one day to avoid look-ahead bias

Why FTSE 350?
The FTSE 350 combines the large-cap FTSE 100 with the mid-cap FTSE 250, giving a deep, liquid universe spanning banks, energy, telecoms, mining and more. High liquidity keeps transaction-cost assumptions realistic.

Project Objective
Select tightly co-moving FTSE 350 pairs, apply a ±2 σ Z-score mean-reversion rule, backtest each pair, and identify which delivers the best risk-adjusted alpha (total return, Sharpe ratio, drawdown).

Data & Preprocessing
• Source: Yahoo Finance via yfinance (and OpenBB) in src/bulk_download.py
• Period: January 1 2015 – June 30 2025 (≈10½ years of daily closes)
• Merged individual ticker CSVs into data/ftse350_prices.csv (src/build_master_price_table.py)
• Pivoted to a wide table (one column per ticker, indexed by Date), dropped any dates with missing or zero/negative prices

Sample of cleaned data:
Date HSBA.L BARC.L VOD.L
2015-01-02 614.70 607.30 160.50
2015-01-05 613.70 600.92 158.30
2015-01-06 604.60 593.70 154.20

Key Visuals

Z-Score & Trade Signals (figures/signals_HSBA.L_BARC.L.png)

Cumulative Returns vs. Benchmark (figures/cumret_HSBA.L_BARC.L.png)

Distribution of Daily Returns (figures/hist_HSBA.L_BARC.L.png)

Top Results
• HSBA.L vs BARC.L: Strategy Return 45.0 %, Benchmark Return 18.0 %, Sharpe 1.20, Max Drawdown –12.3 %, Trades 15, Avg Return/Trade 3.00 %
• VOD.L vs BT.A: Strategy Return 30.5 %, Benchmark Return 10.2 %, Sharpe 0.85, Max Drawdown –18.7 %, Trades 12, Avg Return/Trade 2.54 %

Conclusion & Next Steps
This simple ±2 σ rule delivered strong alpha and controlled risk. To move toward live trading, I’ll incorporate transaction-cost estimates, test rolling thresholds, and add stop-loss rules.

