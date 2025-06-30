FTSE 350 Pairs-Trading Backtest
Welcome! This project implements a simple, market-neutral pairs-trading strategy on FTSE 350 stocks, complete with data ingestion, signal generation, backtesting, and performance reporting.

📖 What You’ll Learn
Data engineering: bulk-downloading daily prices, cleaning and merging into one master CSV

Statistical filtering: using Pearson correlation to find co-moving stock pairs

Signal design: standardizing the price spread into a Z-score and timing mean-reversion trades

Backtesting mechanics: computing daily returns, equity curves, Sharpe ratio, drawdowns

Automation: looping over multiple pairs to save summaries and plots

Storytelling: collecting metrics into a CSV, visualizing with charts, and writing a human-friendly report

Quick Start
Clone the repo

bash
Copy
Edit
git clone https://github.com/you/quant-pairs-trading.git
cd quant-pairs-trading
Set up your Python environment

bash
Copy
Edit
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
pip install -r requirements.txt
Download FTSE 350 price data

bash
Copy
Edit
python src/bulk_download.py
Build the master price table

bash
Copy
Edit
python src/build_master_price_table.py
Backtest all correlated pairs

bash
Copy
Edit
python src/backtest_all_pairs.py
Collect and review your results

bash
Copy
Edit
python src/collect_summaries.py
python src/plot_all_pairs.py
All numeric summaries land in results/, and PNG charts appear in figures/.

📊 Key Findings
Top pair: HSBA.L vs BARC.L

Strategy return: ~45 %

Benchmark return (HSBC buy-and-hold): ~18 %

Sharpe ratio: ~1.2

Max drawdown: –12 %

Our mean-reversion rules delivered a smooth equity curve with controlled pullbacks.

Daily P&L is mostly small gains and losses, punctuated by occasional larger payoffs when extreme Z-scores triggered trades.

🛠 Project Structure
bash
Copy
Edit
quant-pairs-trading/
├─ src/                   # Python scripts
│   ├ bulk_download.py    # grab raw CSVs
│   ├ build_master_price_table.py
│   ├ backtest_all_pairs.py
│   ├ collect_summaries.py
│   └ plot_all_pairs.py
├─ data/                  # raw & merged CSVs
├─ results/               # text summaries & master CSV
├─ figures/               # saved plots (PNG)
├─ REPORT.md              # your polished project report
└─ requirements.txt       # dependencies
✨ Next Steps
Add transaction-cost modeling (bid/ask, slippage)

Use rolling windows for dynamic Z-score thresholds

Test cointegration instead of raw correlation

Expand to other universes (FTSE 100, S&P 500, crypto pairs)

📬 Questions or Feedback?
Feel free to raise an issue or drop me a line. I’m always happy to chat about quant strategies, Python data pipelines, or just the best way to make mean-reversion work in live markets.
