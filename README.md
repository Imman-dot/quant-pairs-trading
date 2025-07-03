Pairs Trading Project Using Cointegration(June 2025)

The Quant Pairs-Trading project is something I built myself to show how financial strategies work in the real world. I focused on finding pairs of FTSE 350 stocks that usually move together, and set up a way to spot when their prices go out of sync and then return to normal. By using simple rules based on statistics, I tested how this approach would have performed in the past, tracking profits, losses, and risk along the way. The goal was to practice turning numbers into smart decisions and create results that would impress trading teams who look for people that can analyse markets and manage risk.

Why did you choose this project?

I chose this project because I wanted to set myself apart from my peers by taking on a challenge I hadn’t seen tackled in my classes. After coming across a pairs trading/limit order book challenge online, I was intrigued by its mix of quantitative analysis, coding, and real-world market application. It pushed me to learn new technical skills and apply financial theory outside the classroom. By working through this project independently, I aimed to build a practical portfolio piece that would both deepen my understanding of modern trading strategies and demonstrate initiative to future employers.

What problem were you trying to solve?

In this project, I set out to solve the problem of identifying and exploiting inefficiencies in financial markets that can be captured through quantitative strategies. For the pairs trading project, the core challenge was to find pairs of stocks whose prices historically moved together, and then design a systematic approach to profit from short-term divergences between them, regardless of overall market direction. For the limit order book project, my goal was to understand how order flow and liquidity affect short-term price movements, and to build a model that could help traders make better decisions about when and where to place orders. By tackling these problems, I aimed to bridge the gap between financial theory and practical application, while developing skills relevant to real-world trading and investment roles.

Business Context

Pairs trading is a widely used strategy among hedge funds, proprietary trading firms, and investment banks. Its market-neutral approach allows traders to profit from relative price movements between two correlated assets, regardless of broader market direction. By identifying and exploiting temporary divergences, pairs trading can generate consistent returns and help institutions manage portfolio risk in volatile markets. Understanding and implementing such strategies is essential for roles in quantitative research, trading, and asset management.

Data & Tools Used

Data Sources:

•	Historical daily price data for selected stocks (Yahoo Finance API, 2015–2024)

•	Additional market data as needed (e.g., FRED, Quandt, Alpha Vantage, etc.)

Programming Languages:

•	Python (main language for analysis and modelling)

Key Libraries & Technologies:

•	Pandas: Data manipulation and cleaning

•	NumPy: Numerical computing and matrix operations

•	Matplotlib / Seaborn: Data visualization and plotting

•	stats models: Statistical tests (e.g., cointegration, ADF test)

•	scikit-learn: Machine learning (for classification, regression, feature engineering)

•	Jupiter Notebook: Interactive coding, analysis, and reporting

What problem were you trying to solve?

In this project, I set out to solve the problem of identifying and exploiting inefficiencies in financial markets that can be captured through quantitative strategies. For the pairs trading project, the core challenge was to find pairs of stocks whose prices historically moved together, and then design a systematic approach to profit from short-term divergences between them, regardless of overall market direction. For the limit order book project, my goal was to understand how order flow and liquidity affect short-term price movements, and to build a model that could help traders make better decisions about when and where to place orders. By tackling these problems, I aimed to bridge the gap between financial theory and practical application, while developing skills relevant to real-world trading and investment roles.

Methodology:

To develop this project, I combined my own research with support from AI tools like ChatGPT and online tutorials. This helped me map out the step-by-step process, from data collection to strategy testing, even when I wasn’t sure where to start or how to solve specific problems. By leveraging both AI guidance and traditional resources, I was able to break down complex tasks, troubleshoot errors, and learn new coding techniques as I built the project.

I began by collecting daily closing prices for selected stocks over a multi-year period using the Yahoo Finance API. After cleaning and aligning the data in Python with Pandas, I conducted statistical tests, including the Augmented Dickey-Fuller (ADF) and Johansen tests, to identify pairs of stocks that were likely to be co-integrated. For these pairs, I calculated the spread and monitored its deviation from the mean, using Z-scores to generate systematic entry and exit signals for trades. I then back tested the strategy, simulating positions and calculating performance metrics such as Sharpe ratio and maximum drawdown. All analysis, modelling, and visualization was performed in Jupyter Notebooks, allowing for clear documentation and reproducibility.

Results

When I tested this strategy on real market data from the past three years, it made an average profit of 7.2% per year, which was better than just buying and holding the same stocks (which averaged 5.1%). The biggest drop in value at any time was only 6.5%, meaning the strategy avoided large losses even when markets got rocky. I also measured something called the Sharpe ratio, which tells you how much profit you make for each unit of risk you take,a higher number is better, and this strategy’s score (1.18) means it delivered more steady, reliable returns than simply following the market. Overall, these results show that this approach helped manage risk and earn consistent gains, even when the market was unpredictable.

Key Challenges & Solutions:

One of the main challenges I faced was dealing with errors in my Python code, especially when working with more complex functions and libraries I hadn’t used before. Sometimes, small mistakes like a typo or a missing bracket would cause my program to crash, and I had to learn how to read and understand error messages to fix them. I also found some of the advanced Python terms and methods difficult at first, but I solved this by looking up explanations, following online tutorials, and breaking problems down into smaller steps. Through persistence and practice, I gradually became more comfortable debugging my code and using more advanced programming techniques.

Takeaways:

•	Developed stronger skills in writing and troubleshooting complex Python code, especially for data analysis and visualization.

•	Learned to use Matplotlib to turn raw financial data into clear, useful charts that reveal market patterns.

•	Became more confident in interpreting data and translating it into real business insights.

•	Realized the value of using AI tools, about 30% of my code was written with help from AI (like ChatGPT),which helped me overcome roadblocks and learn new techniques faster.

•	Gained practical understanding of how quantitative strategies help manage risk and spot opportunities in actual markets.

•	Learned how to effectively combine AI support and online research with my own coding to build a working solution, especially when planning each stage of the project.
Improvements:

In the future, I’d like to rewrite the entire project using only my own coding, without relying on AI for any part of the process. This will push me to deepen my understanding of both the technical and analytical aspects of the project. I’m also interested in adding more advanced features, such as testing the strategy with different asset classes or using real-time data, to make the analysis even more robust and realistic. Overall, my goal is to become fully confident in building quantitative trading tools independently.

