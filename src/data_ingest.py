"""
data_ingest.py
Download daily OHLCV prices for ONE ticker and store to data/raw/<ticker>.csv.

Usage (run from project root, venv active):
    python src/data_ingest.py HSBA.L
"""

import sys
from pathlib import Path
import yfinance as yf


def download_one(ticker: str, start="2015-01-01") -> None:
    """Download <ticker> from Yahoo Finance and save as CSV."""
    print(f"Downloading {ticker}…")
    df = yf.download(ticker, start=start, auto_adjust=False, progress=False)
    if df.empty:
        raise ValueError(f"No data returned for {ticker}")
    out_path = Path("data", "raw", f"{ticker}.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)  # ensure folder
    df.to_csv(out_path)
    print(f"Saved {len(df):,} rows → {out_path.resolve()}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:  python src/data_ingest.py <TICKER>  e.g. HSBA.L")
        sys.exit(1)
    download_one(sys.argv[1])
