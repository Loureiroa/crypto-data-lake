import sys
import argparse
from datetime import datetime

# Informação de onde está o projeto
from pathlib import Path
project_root = Path(__file__).resolve().parent

# Importa cada step como módulo
import scripts.ingest as ingest
import scripts.process as process
import scripts.curate as curate
import scripts.quality as quality
import scripts.metadata as metadata


def main():
    parser = argparse.ArgumentParser("Pipeline Crypto Data Lake")
    parser.add_argument(
        "step",
        choices=["ingest", "process", "curate", "quality", "metadata", "all"],
        help="Etapa a executar"
    )
    parser.add_argument(
        "date",
        nargs="?",
        help="Data no formato YYYY-MM-DD (default: hoje)"
    )
    args = parser.parse_args()

    # Data padrão = hoje se não for informada
    date_str = args.date or datetime.today().strftime("%Y-%m-%d")

    # Mapeia nome da etapa para a função run
    steps = {
        "ingest": ingest.run,
        "process": process.run,
        "curate": curate.run,
        "quality": quality.quality_checks,
        "metadata": metadata.generate_catalog
    }

    if args.step == "all":
        # Executa todas em sequência dentro do mesmo processo
        for fn in [ingest.run, process.run, curate.run, quality.quality_checks, metadata.generate_catalog]:
            fn(date_str)
    else:
        steps[args.step](date_str)


if __name__ == "__main__":
    main()
