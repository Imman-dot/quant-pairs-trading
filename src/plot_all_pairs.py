# src/plot_all_pairs.py
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv(Path(__file__).resolve().parent.parent / "results" / "all_pairs_summary.csv")

# Plot strategy returns
ax = df.set_index("pair")["strategy_return"].sort_values().plot(kind="barh", figsize=(8,6))
ax.set_xlabel("Strategy Return")
ax.set_title("Returns by Pair")
plt.tight_layout()
plt.savefig(Path(__file__).resolve().parent.parent / "figures" / "all_pairs_returns.png")
plt.show()
