\# API Examples



\## Azure AI Search SDK



\### Create Index

```python

from azure.search.documents.indexes import SearchIndexClient

from azure.core.credentials import AzureKeyCredential

import json



endpoint = os.getenv("AZURE\_SEARCH\_SERVICE\_ENDPOINT")

key = os.getenv("AZURE\_SEARCH\_API\_KEY")



client = SearchIndexClient(endpoint, AzureKeyCredential(key))

with open("config/search\_index.json") as f:

&#x20;   index\_schema = json.load(f)



client.create\_index(index\_schema)



\### Upload Documents

```python

from azure.search.documents import SearchClient



search\_client = SearchClient(endpoint, "product-catalog", AzureKeyCredential(key))



docs = json.load(open("data/sample\_products.json"))

search\_client.upload\_documents(docs)





\### Query

```python

results = search\_client.search("Pro tier products")

for r in results:

&#x20;   print(r\["id"], r\["name"])



\## Azure OpenAI (RAG)

\### Embeddings

```python

from azure.ai.openai import OpenAIClient



openai\_client = OpenAIClient(endpoint, AzureKeyCredential(os.getenv("AZURE\_OPENAI\_API\_KEY")))

embedding = openai\_client.get\_embeddings(

&#x20;   deployment\_id=os.getenv("AZURE\_OPENAI\_EMBEDDING\_DEPLOYMENT"),

&#x20;   input="Pro tier product specifications"

)



\### Chat Completion

```python

chat = openai\_client.get\_chat\_completions(

&#x20;   deployment\_id=os.getenv("AZURE\_OPENAI\_CHAT\_DEPLOYMENT"),

&#x20;   messages=\[{"role": "user", "content": "What specs does the Pro tier include?"}]

)

print(chat.choices\[0].message\["content"])










