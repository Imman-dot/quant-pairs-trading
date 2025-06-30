FTSE 350 Pairs-Trading Backtest (Quick Preview)
What it does:
Runs a simple ±2σ Z-score mean-reversion strategy on your most correlated FTSE 350 stock pairs.

Key Result:
HSBA.L vs BARC.L returned ~45 % vs an 18 % buy-and-hold, Sharpe ≈ 1.2, max drawdown ~ –12 %.

Quickstart:

git clone … && cd quant-pairs-trading

python -m venv .venv && .\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

python src/backtest_all_pairs.py

All summaries land in results/, charts in figures/.
