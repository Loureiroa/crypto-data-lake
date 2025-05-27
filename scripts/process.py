import json
import pandas as pd
from pathlib import Path
from datetime import datetime


def process_data(date_str=None):
    if date_str is None:
        date_str = datetime.today().strftime("%Y-%m-%d")

    in_path = Path(__file__).parent.parent / "data" / "bronze" / date_str / "crypto_prices.json"
    out_dir = Path(__file__).parent.parent / "data" / "silver" / date_str
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(in_path, "r") as f:
        data = json.load(f)

    rows = []
    for coin, prices in data.items():
        for curr, price in prices.items():
            rows.append({"coin": coin, "currency": curr, "price": price, "date": date_str})

    df = pd.DataFrame(rows)
    out_file = out_dir / "crypto_prices.parquet"
    df.to_parquet(out_file, index=False)
    print(f"✅ Dados processados salvos em {out_file}")


def run(date_str=None):
    """Entry point para orquestração."""
    process_data(date_str)


if __name__ == "__main__":
    import sys
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    run(arg)
