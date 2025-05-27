import pandas as pd
from pathlib import Path
from datetime import datetime
import sys


def quality_checks(date_str=None):
    if date_str is None:
        date_str = datetime.today().strftime("%Y-%m-%d")

    base = Path(__file__).parent.parent / "data" / "gold" / date_str
    parquet_path = base / "crypto_prices_curated.parquet"
    if not parquet_path.exists():
        print(f"[ERRO] Arquivo não encontrado: {parquet_path}")
        sys.exit(1)

    df = pd.read_parquet(parquet_path)
    total_rows = len(df)
    total_cols = len(df.columns)
    nulls = df.isna().sum().to_dict()
    dups = df.duplicated().sum()
    stats = df["price"].describe().to_dict()
    mean_price = stats.get("mean", 0)
    outliers = ((df["price"] < 0) | (df["price"] > mean_price * 3)).sum()

    print("=== QUALITY REPORT ===")
    print(f"Linhas totais        : {total_rows}")
    print(f"Colunas totais       : {total_cols}")
    print(f"Nulos por coluna     : {nulls}")
    print(f"Duplicatas           : {dups}")
    print(f"Estatísticas de preço: {stats}")
    print(f"Outliers (>3×média)  : {outliers}")

    # salva CSV
    report = {
        "total_rows": total_rows,
        "total_cols": total_cols,
        "dup_count": dups,
        "outliers": outliers,
        **{f"nulls_{k}": v for k, v in nulls.items()},
        **{f"price_{k}": v for k, v in stats.items()},
    }
    report_df = pd.DataFrame([report])
    rpt_file = base / "quality_report.csv"
    report_df.to_csv(rpt_file, index=False)
    print(f"[INFO] Relatório salvo em: {rpt_file}")


def run(date_str=None):
    """Entry point para orquestração."""
    quality_checks(date_str)


if __name__ == "__main__":
    import sys
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    run(arg)
