import pandas as pd

# Load your data
df = pd.read_csv("data/ftse350_prices.csv", parse_dates=["Date"])

# Pivot so each ticker is a column
df_wide = df.pivot(index="Date", columns="Ticker", values="Close")

# Compute the correlation matrix for all tickers
cor_matrix = df_wide.corr()

# Find the top pairs (excluding correlation of a ticker with itself)
pairs = []
for t1 in cor_matrix.columns:
    for t2 in cor_matrix.columns:
        if t1 < t2:  # Avoid duplicates and self-pairs
            corr = cor_matrix.loc[t1, t2]
            pairs.append((t1, t2, corr))

# Sort by correlation, highest first
pairs.sort(key=lambda x: abs(x[2]), reverse=True)

# Print the top 10 pairs with highest absolute correlation
print("Top 10 most correlated pairs:")
for t1, t2, corr in pairs[:10]:
    print(f"{t1} & {t2}: {corr:.2f}")
