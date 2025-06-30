import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/ftse350_prices.csv", parse_dates=["Date"])
tickers = ['VOD.L', 'BARC.L']

# Plot each ticker
for ticker in tickers:
    ts = df[df['Ticker'] == ticker].set_index('Date')['Close']
    plt.plot(ts.index, ts, label=ticker)

plt.legend()
plt.title("Price Series Comparison")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.tight_layout()

# Calculate correlation
df_wide = df.pivot(index="Date", columns="Ticker", values="Close")
cor = df_wide[tickers[0]].corr(df_wide[tickers[1]])

# Add correlation text right under the legend (top-left)
ax = plt.gca()
x_pos, y_pos = 0.05, 0.85  # Adjust if needed
ax.text(x_pos, y_pos, f"Correlation: {cor:.2f}",
        transform=ax.transAxes, fontsize=12,
        bbox=dict(facecolor='black', alpha=0.7, edgecolor='gray', boxstyle='round'))

print("Correlation is:", cor)
print(df[df['Ticker'] == tickers[0]].head())
print(df[df['Ticker'] == tickers[1]].head())

plt.show()
