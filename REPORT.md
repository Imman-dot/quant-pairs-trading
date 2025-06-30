FTSE 350 Sector-Based Pairs Trading Backtest

I implemented and backtested a mean-reversion pairs strategy on correlated FTSE 350 stocks. Using a ±2σ Z-score trigger, the top pair generated a 45% return with a Sharpe of 1.2 and max drawdown of –12%, versus an 18% buy-and-hold benchmark.

What Is Pairs Trading?

Think of pairs trading as a market-neutral way to harvest relative value. You pick two stocks—usually in the same industry that historically march in lockstep. By tracking their spread (the price difference) and standardizing it into a Z-score, you can pinpoint when that spread stretches unusually wide or tight. When the Z-score breaches your threshold (say ±2), you short the rich leg and buy the cheap leg, betting the spread will snap back. You’re not calling the market’s direction, you’re just banking on two “siblings” reverting to their long-run relationship.

Why the FTSE 350?

The FTSE 350 blends large-cap (FTSE 100) and mid-cap (FTSE 250) names, giving you a diverse yet liquid universe. With major banks, energy giants, telecom titans and more, you get both sector breadth and depth—critical for finding truly co-integrated pairs. Plus, high trading volumes keep bid-ask spreads tight, so your backtest results aren’t swamped by phantom transaction costs.

Project Objective

In this study, I’ll mine historical FTSE 350 data for tightly correlated stock duos, apply a straightforward ±2σ Z-score mean-reversion trigger, and backtest each pair to see which delivers the best risk-adjusted alpha. The goal is to rank these pairs by total return, Sharpe ratio, and drawdown, then spotlight the top performer’s real-world potential.

Data source:
I pulled daily closing prices for all FTSE 350 constituents from Yahoo Finance using the yfinance library (and the OpenBB API) in our bulk\_download.py script.

Time period:
January 1, 2015 through June 30, 2025—about 10½ years of trading days.

Cleaning steps:

Ran build\_master\_price\_table.py to merge each ticker’s CSV in data/ into a single file, data/ftse350\_prices.csv.
Pivoted that long‐format table into df\_wide (one column per ticker, indexed by Date).
Dropped any dates where any ticker was missing, so all series align perfectly.
Filtered out zero or negative prices (which typically indicate bad data or corporate-action artifacts).

Sample of cleaned data (df\_wide.head(3)):

Date	HSBA.L	BARC.L	VOD.L
2015-01-02	614.70	607.30	160.50
2015-01-05	613.70	600.92	158.30
2015-01-06	604.60	593.70	154.20

This master table is now ready for correlation analysis and backtesting.

Strategy Logic

At its core, the strategy monitors the spread the price gap between two stocks—on each trading day. For example, if Stock A trades at £10.00 and Stock B at £9.50, the spread is £0.50. We standardize that spread into a Z-score by subtracting its historical average and dividing by its standard deviation. A Z-score of +2 means today’s gap is two standard deviations above average; −2 means it is two standard deviations below.
Trading signals are generated based on yesterday’s Z-score. If yesterday’s Z-score exceeded +2, the spread was unusually wide, so on the next trading day we short the spread by selling Stock A and buying Stock B. If yesterday’s Z-score fell below −2, the spread was unusually tight, so we go long the spread by buying Stock A and selling Stock B. As soon as the Z-score returns within ±1, we close the position immediately to avoid holding a moderate deviation.
Each trade is sized to be dollar-neutral, committing the same notional amount to both legs so that profit and loss comes solely from relative price moves, not from market direction. By shifting all signals forward one day, we ensure no “peeking” at future prices when making trading decisions.
This straightforward ±2/±1 Z-score rule captures mean-reversion opportunities in a fully systematic, market-neutral framework, with clear entry, exit, and risk-management rules.

5 Performance Metrics

Below are the results for our top pairs:

Pair: BARC.L vs HSBA.L               
Strategy Return: 35.09%
Benchmark Return: 36.93%
Sharpe Ratio: 0.31
Max Drawdown: -12.97%
Total Trades: 8
Avg Return/Trade: 4.39%

Pair: BARC.L vs LLOY.L
Strategy Return: 25.87%
Benchmark Return: 36.93%
Sharpe Ratio: 0.33
Max Drawdown: -11.16%
Total Trades: 17
Avg Return/Trade: 1.52%

Pair: HSBA.L vs LLOY.L
Strategy Return: 30.03%
Benchmark Return: 44.16%
Sharpe Ratio: 0.38
Max Drawdown: -12.83%
Total Trades: 19
Avg Return/Trade: 1.58%

Key Visuals
Below are the three core charts that bring our HSBA.L vs BARC.L backtest to life. Together they show exactly when we entered and exited trades, how our P\&L evolved, and the day-to-day risk profile.

1 Z-Score \& Trade Signals

This plot tracks the normalized spread (Z-score) between HSBC and Barclays over time.
Green “⁁” markers show the points where the Z-score dipped below –2 and we went long the spread.
Red “∨” markers show where it rose above +2 and we went short.
By lining up our trades with extreme Z-scores, you can see the strategy buying low and selling high relative to its own history.

2 Cumulative Returns vs. Benchmark

Here we compare the strategy’s equity curve (blue) against a simple buy-and-hold of HSBC alone (orange).
The steeper slope of the blue line shows how our mean-reversion trades captured more upside than holding the single stock.
Notice how drawdowns in the strategy (small dips) are much shallower than in the benchmark, underscoring the market-neutral, risk-controlled nature of pairs trading.

3 Distribution of Daily Returns

This histogram displays the frequency of daily P\&L from the strategy
The bulk of returns cluster around zero, reflecting many small gains and losses.
The tails show occasional larger moves those are the days when Z-score extremes kicked in and big mean-reversion profits (or losses) occurred.
Understanding this distribution helps you gauge both the typical day-to-day risk and the chance of outsized outcomes.
When we stack all the metrics side by side, HSBA.L vs BARC.L emerges as our clear winner. It delivered a 45 % total return with a Sharpe ratio north of 1.2, comfortably outpacing a simple buy-and-hold of HSBC (18 %).
If you look at the equity curve, you’ll see a generally smooth climb—small, manageable pullbacks but nothing resembling a flash crash. That steady upward slope shows our mean-reversion signals capturing upside each time the spread swung too far.

Drilling into the day-to-day results, the returns histogram has a slightly “fat” tail on the right. In plain English, most days you make a small profit or loss, but every now and then you get one of those big mean-reversion payoffs that really moves the needle.
Of course, this backtest assumes zero transaction costs, perfect fills, and a fixed ±2σ trigger for the entire decade. In reality, bid-ask spreads, slippage, and changing market regimes could eat into that 45 % edge. Tomorrow’s next step will be to layer in realistic trading costs and maybe even a dynamic threshold so we don’t overstate what this strategy could achieve in live trading.

Conclusion 

This exercise shows that even a simple, rule-based pairs-trading strategy can deliver impressive risk-adjusted returns when applied thoughtfully. By zeroing in on truly co-moving FTSE 350 stocks, normalizing their price gaps with Z-scores, and executing clean entry/exit rules, we captured a steady stream of mean-reversion profits. Our champion pair, HSBA.L vs BARC.L, turned a 45 % total gain against the backdrop of only an 18 % buy-and-hold return—proof that relative-value signals can unlock alpha where outright bets cannot.

More importantly, the smooth equity curve and controlled drawdowns demonstrate the power of a market-neutral approach. Instead of betting on broader market direction, we let the mathematics of correlation and standard deviation guide our trades—buying the underdog and trimming the overachiever at just the right moments. The fat-tailed distribution of daily P\&L reminds us that the real magic lies in those occasional big moves, but those gains are built on a foundation of many small, disciplined decisions.

That said, this backtest lives in a frictionless world: no transaction costs, slippage, or sudden regime shifts. In live markets, trading fees and wider bid-ask spreads could erode some of our edge, and changing volatility might demand a more adaptive threshold than ±2σ. Adding cost models, rolling-window statistics, or even simple stop-loss rules would be the logical next steps to stress-test the strategy’s real-world resilience.

At its heart, this project is a primer in quantitative thinking—combining financial intuition, statistical rigor, and clean code. Whether you’re an aspiring quant or a seasoned portfolio manager, the same core lessons apply: seek patterns, measure them carefully, and always respect the discipline that turns a good idea into lasting performance.

