"""
bulk_download.py
Loop through tickers in data/ftse350_tickers.csv and download each one.
Run in the terminal with:
    python src/bulk_download.py
"""

import time
import logging
from pathlib import Path

import pandas as pd
from data_ingest import download_one      # <- yesterday's function

CSV_PATH = Path("data", "ftse350_tickers.csv")
SLEEP_SEC = 1                             # pause 1 s between downloads

# --------------------- configure logging ---------------------
logging.basicConfig(
    filename="data/download_errors.log",  # log file goes here
    level=logging.INFO,                   # log INFO and above
    format="%(asctime)s  %(message)s",
)
# -------------------------------------------------------------


def main() -> None:
    """Read the ticker list and download each one if missing."""
    tickers = pd.read_csv(CSV_PATH, header=None)[0].tolist()

    for i, ticker in enumerate(tickers, 1):
        out_path = Path("data", "raw", f"{ticker}.csv")

        # ---------- SKIP if file already exists ----------
        if out_path.exists():                   # 📝 Note-time:
            print(f"[{i}/{len(tickers)}] {ticker} ✔ already done – skip")
            continue                            #  continue = next loop item

        try:
            download_one(ticker)
        except Exception as err:                # catch any error
            print(f"[{ticker}] ⚠ {err}")
            logging.info("%s — %s", ticker, err)
        else:
            print(f"[{i}/{len(tickers)}] {ticker} ✅ done")

        time.sleep(SLEEP_SEC)                   # polite pause


if __name__ == "__main__":
    main()
