\# System Architecture



\## Overview

This project integrates \*\*Azure AI Search\*\* with a product catalog database and extends it with \*\*Retrieval-Augmented Generation (RAG)\*\* using Azure OpenAI.



The workflow ensures:

\- All products are indexed in Azure AI Search.

\- Queries can be keyword, vector, or hybrid.

\- RAG provides grounded answers by combining search results with LLM responses.



\---



\## Components

\- \*\*Database (Postgres/CSV)\*\* → Source of product catalog data.

\- \*\*Indexer (src/indexer.py)\*\* → Reads product data and uploads to Azure AI Search.

\- \*\*Azure AI Search\*\* → Hosts the product index, supports keyword + vector search.

\- \*\*Query Service (src/query.py)\*\* → Executes search queries via SDK.

\- \*\*RAG Pipeline (src/rag\_pipeline.py)\*\* → Combines search results with Azure OpenAI chat model.

\- \*\*Azure OpenAI\*\* → Provides embeddings and chat completions.



\---



\## Data Flow

1\. \*\*Data Source\*\* → Product catalog rows exported as JSON.

2\. \*\*Indexer\*\* → Creates index schema (`config/search\_index.json`) and uploads docs.

3\. \*\*Azure AI Search\*\* → Stores indexed products with nested `specs`.

4\. \*\*Query Service\*\* → Retrieves results (keyword/vector).

5\. \*\*RAG Pipeline\*\* → Uses embeddings + chat model to generate grounded answers.



\---



\## Component Diagram



```text

┌──────────────┐     product docs      ┌──────────────────────┐

│  Data Source │ ────────────────────▶ │   indexer.py         │

│ (JSON / CSV /│                        │  • create index      │

│  Postgres)   │                        │  • upload documents  │

└──────────────┘                        └──────────┬───────────┘

&#x20;                                                   │ push model

&#x20;                                                   ▼

&#x20;                                       ┌──────────────────────┐

&#x20;                                       │   Azure AI Search     │

&#x20;                                       │  • text + vector      │

&#x20;                                       │    fields             │

&#x20;                                       │  • HNSW config        │

&#x20;                                       │  • semantic ranker    │

&#x20;                                       └──────────┬───────────┘

&#x20;                       query (keyword/vector/hybrid)│  grounding docs

&#x20;                                                   ▼

┌──────────────┐     question       ┌──────────────────────────┐

│    User /    │ ─────────────────▶ │   rag\_pipeline.py         │

│    Client    │                    │  • embed query (AOAI)     │

│              │ ◀───────────────── │  • retrieve from Search   │

└──────────────┘   grounded answer  │  • call Azure OpenAI chat │

&#x20;                                   └──────────────────────────┘

```

