import pandas as pd
df = pd.read_csv("data/ftse350_prices.csv")
print("Tickers in file:", df['Ticker'].nunique())
print("First date:", df['Date'].min())
print("Last date:", df['Date'].max())
print("Rows:", len(df))

