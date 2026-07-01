\# Azure AI Search Product Catalog + RAG



\## Overview

This project demonstrates how to integrate \*\*Azure AI Search\*\* with a product catalog database and extend it with \*\*Retrieval-Augmented Generation (RAG)\*\* using Azure OpenAI.



The workflow:

1\. \*\*Create index\*\* → Define schema for product catalog.

2\. \*\*Upload documents\*\* → Push product data into Azure AI Search.

3\. \*\*Query with SDK\*\* → Run keyword, vector, and hybrid queries.

4\. \*\*Integrate RAG\*\* → Use Azure OpenAI to generate grounded answers.



\---



\## Prerequisites

\- Python 3.10+

\- Azure subscription with AI Search provisioned

\- Azure OpenAI (optional, for RAG)

\- Environment variables set in `.env`



\---



\## Project Structure



```text

azure-ai-search-catalog/

│

├── README.md                # Overview, setup, usage instructions

├── requirements.txt         # Python dependencies (azure-search-documents, azure-identity, etc.)

├── .env.example             # Example environment variables (ES\_URL, AZURE\_SEARCH\_KEY)

├── .gitignore               # Ignore venv, logs, secrets

│

├── config/

│   ├── search\_index.json    # Index schema definition (fields, analyzers, vector settings)

│   ├── mapping.json         # Elasticsearch-style mapping if hybrid search used

│   └── settings.yaml        # General config (chunk size, embedding model)

│

├── data/

│   ├── sample\_products.json # Example product docs for testing

│   └── loaders/             # Scripts to pull data from Postgres/CSV

│

├── src/

│   ├── indexer.py           # Create index, upload documents

│   ├── query.py             # Query examples (keyword, vector, hybrid)

│   ├── rag\_pipeline.py      # Retrieval-Augmented Generation integration with Azure OpenAI

│   └── utils.py             # Helper functions (auth, logging)

│

├── notebooks/

│   ├── 01\_setup.ipynb       # Walkthrough: provision service, create index

│   ├── 02\_upload\_docs.ipynb # Upload product catalog

│   └── 03\_query\_rag.ipynb   # Run queries with RAG pipeline

│

├── tests/

│   ├── test\_indexer.py      # Unit tests for index creation

│   ├── test\_query.py        # Validate search results

│   └── test\_rag\_pipeline.py # Ensure RAG returns grounded answers

│

└── docs/

&#x20;   ├── architecture.md      # Diagram of workflow (DB → AI Search → RAG → App)

&#x20;   └── api\_examples.md      # REST/SDK usage snippets

```





\---



\## Setup

```bash

git clone https://github.com/Zack4DEV/azure-ai-search-catalog.git

cd azure-ai-search-catalog

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

```

\---



\## Usage



\#### 1. Create index

python src/indexer.py



\#### 2. Upload sample docs

python src/indexer.py --data data/sample\_products.json



\#### 3. Query

python src/query.py "Pro tier products"



\#### 4. Run RAG Piepline

python src/rag\_pipeline.py "What specs does the Pro tier include?"



