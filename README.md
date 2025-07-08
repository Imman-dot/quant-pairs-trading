# PairsTrading 🔗
End-to-end **cointegration screener and cost-aware long–short back-tester** for equity pairs.

## Key Features
- Vectorised back-test engine with slippage and commission  
- Performance report: Sharpe ratio, max drawdown, turnover, underwater plots  

---

## Overview
This self-directed project shows how a real-world pairs-trading strategy works. I focused on FTSE 350 stocks that usually move together and built rules to catch moments when their prices drift apart and then snap back. By back-testing these rules on historical data, I tracked profits, losses and risk to see whether the strategy could beat a simple buy-and-hold. My aim was to turn numbers into smart trading decisions and create results that would impress desks looking for people who can analyse markets and manage risk.

## Why I Chose This Project
I wanted a challenge my classmates hadn’t attempted. A pairs-trading / limit-order-book prompt online caught my eye because it blends stats, coding and real market application. Tackling it on my own helped me learn new technical skills, apply financial theory outside class and build a portfolio piece that shows initiative.

## Problem Statement
Markets aren’t perfectly efficient; prices of related stocks wander apart and then converge. I set out to:
1. Detect stock pairs whose prices historically move together.  
2. Build a systematic way to profit from short-term divergences, regardless of overall market direction.  
3. Demonstrate that I can bridge theory and practice in a trading-desk context.

## Business Context
Pairs trading is used by hedge funds, prop-trading shops and investment banks. Because it is market-neutral, it can generate returns even in volatile conditions and helps manage portfolio risk. Knowing how to design, test and monitor such strategies is valuable for roles in quantitative research, trading and asset management.

## Data & Tools Used
| Category | Details |
|----------|---------|
| **Data** | Historical daily prices from Yahoo Finance (2015-2024) plus supplemental macro data (FRED, Quandl). |
| **Languages** | Python for all analysis and modelling. |
| **Libraries** | Pandas, NumPy, Matplotlib, Seaborn, `statsmodels` (ADF, Johansen tests), scikit-learn, Jupyter Notebook. |

## Methodology
I combined my own research with AI tools (ChatGPT) to plan and troubleshoot.  
1. **Data collection & cleaning**: pulled daily closes via Yahoo Finance, aligned series in Pandas.  
2. **Pair selection**: ran ADF and Johansen tests to find co-integrated pairs.  
3. **Signal generation**: computed the spread and used Z-score thresholds to trigger trades (enter if Z > 1 or Z < -1, exit at Z ≈ 0).  
4. **Back-testing**: simulated positions with transaction costs, calculated Sharpe ratio and max drawdown.  
5. **Documentation & reproducibility**: all steps live in a Jupyter notebook.

## Results
- **Average annual return**: **7.2 %** vs. 5.1 % for buy-and-hold.  
- **Sharpe ratio**: **1.18** (higher return per unit risk than the market benchmark).  
- **Max drawdown**: **6.5 %**, meaning losses stayed relatively shallow during rough periods.  
Overall, the strategy delivered steadier gains and lower risk than holding the stocks outright.

## Key Challenges & Solutions
Working with new libraries led to frequent syntax and logic errors. Breaking tasks into small milestones and using AI plus online docs helped me debug faster and stay focused.

## Takeaways
- Sharpened advanced Python for data analysis and visualisation.  
- Learned to turn raw data into actionable trading insights.  
- About **30 % of code** was AI-assisted—great for overcoming roadblocks and learning faster.  
- Gained practical insight into risk management and market-neutral trading.

## Improvements
Next, I plan to:
1. Rewrite the project without AI help to deepen my coding skill.  
2. Extend testing to other asset classes (FX, ETFs).  
3. Integrate live data feeds for near-real-time monitoring.

---

*Last updated July 2025*

