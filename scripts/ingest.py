import requests
import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.coingecko.com/api/v3"
HEADERS = {"accept": "application/json"}
CRYPTO_IDS = os.getenv("CRYPTO_IDS", "bitcoin,ethereum,cardano")
VS_CURRENCY = os.getenv("VS_CURRENCY", "usd")


def ingest_data(date_str=None):
    if date_str is None:
        date_str = datetime.today().strftime("%Y-%m-%d")

    output_dir = Path(__file__).parent.parent / "data" / "bronze" / date_str
    output_dir.mkdir(parents=True, exist_ok=True)

    url = f"{BASE_URL}/simple/price?ids={CRYPTO_IDS}&vs_currencies={VS_CURRENCY}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        output_file = output_dir / "crypto_prices.json"
        with open(output_file, "w") as f:
            import json
            json.dump(data, f, indent=4)
        print(f"✅ Dados salvos em {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao obter dados da API: {e}")


def run(date_str=None):
    """Entry point para orquestração."""
    ingest_data(date_str)


if __name__ == "__main__":
    import sys
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    run(arg)
