import pandas as pd
import yaml
from pathlib import Path
from datetime import datetime
import sys


def generate_catalog(date_str=None):
    if date_str is None:
        date_str = datetime.today().strftime("%Y-%m-%d")

    base = Path(__file__).parent.parent / "data" / "gold" / date_str
    parquet_path = base / "crypto_prices_curated.parquet"
    if not parquet_path.exists():
        print(f"[ERRO] Parquet não encontrado: {parquet_path}")
        sys.exit(1)

    df = pd.read_parquet(parquet_path)
    schema = [{"column": c, "dtype": str(df[c].dtype)} for c in df.columns]
    samples = {c: df[c].dropna().astype(str).tolist()[:5] for c in df.columns}

    catalog = {
        "date"        : date_str,
        "record_count": len(df),
        "schema"      : schema,
        "samples"     : samples
    }

    out_file = base / "data_catalog.yaml"
    with open(out_file, "w", encoding="utf-8") as f:
        yaml.safe_dump(catalog, f, sort_keys=False, allow_unicode=True)

    print("=== METADATA CATALOG ===")
    print(f"Arquivo gerado em: {out_file}")


def run(date_str=None):
    """Entry point para orquestração."""
    generate_catalog(date_str)


if __name__ == "__main__":
    import sys
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    run(arg)
