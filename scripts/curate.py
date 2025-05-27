import pandas as pd
from pathlib import Path
from datetime import datetime


def curate_data(date_str=None):
    if date_str is None:
        date_str = datetime.today().strftime("%Y-%m-%d")

    in_path = Path(__file__).parent.parent / "data" / "silver" / date_str / "crypto_prices.parquet"
    out_dir = Path(__file__).parent.parent / "data" / "gold" / date_str
    out_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_parquet(in_path)
    curated = df.sort_values(by="price", ascending=False)
    out_file = out_dir / "crypto_prices_curated.parquet"
    curated.to_parquet(out_file, index=False)
    print(f"✅ Dados curados salvos em {out_file}")


def run(date_str=None):
    """Entry point para orquestração."""
    curate_data(date_str)


if __name__ == "__main__":
    import sys
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    run(arg)
