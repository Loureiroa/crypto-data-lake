# crypto-data-lake

Projetei e implementei um mini data lake simplificado para demonstrar um fluxo completo de dados, do Bronze ao Gold, incluindo qualidade e catálogo de metadados.

## 🎯 Objetivo

Criar um pipeline que:

1. **Ingestão (Bronze)**: captura preços de criptomoedas da CoinGecko em JSON.
2. **Processamento (Silver)**: converte JSON em Parquet tabular.
3. **Curadoria (Gold)**: ordena e refina dados para análise.
4. **Qualidade**: valida nulos, duplicatas e outliers.
5. **Catálogo de Metadados**: gera arquivo YAML com schema e amostras.

## ⚙️ Tecnologias utilizadas

- **Python 3.8+**
- **requests** para chamadas HTTP à API CoinGecko
- **pandas** para manipulação de dados
- **pyarrow** para leitura/gravação de Parquet
- **python-dotenv** para gestão de variáveis de ambiente
- **PyYAML** para serialização de catálogo de metadados

## 🗂️ Estrutura do Projeto

```
crypto_data_lake/
├── data/                     # Armazenamento de dados por camada e data
│   ├── bronze/               # JSON cru da API
│   ├── silver/               # Parquet tabular
│   └── gold/                 # Dados curados + relatórios QA + catálogo
├── scripts/
│   ├── ingest.py             # Dia 1: ingestão da API
│   ├── process.py            # Dia 2: conversão para Parquet
│   ├── curate.py             # Dia 3: refinamento de dados
│   ├── quality.py            # Dia 4: checks de qualidade
│   └── metadata.py           # Dia 5: geração de catálogo YAML
├── main.py                   # CLI unificado para orquestração (all, ingest, ...)
└── README.md                 # Documentação do projeto
```

---

> *Projeto concluído em 26/05/2025 — pronto para evoluir com orquestração (Airflow), API e dashboard.*
