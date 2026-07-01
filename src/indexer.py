import os, json
from dotenv import load_dotenv
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()

endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
key = os.getenv("AZURE_SEARCH_API_KEY")
index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")

index_client = SearchIndexClient(endpoint, AzureKeyCredential(key))
search_client = SearchClient(endpoint, index_name, AzureKeyCredential(key))

# Create index from config/search_index.json
with open("config/search_index.json") as f:
    schema = json.load(f)

try:
    index_client.create_index(schema)
    print(f"Index {index_name} created.")
except Exception as e:
    print(f"Index creation skipped or failed: {e}")

# Upload sample docs if provided
def upload_docs(path="data/sample_products.json"):
    with open(path) as f:
        docs = json.load(f)
    result = search_client.upload_documents(docs)
    print(f"Uploaded {len(docs)} docs. Result: {result}")

if __name__ == "__main__":
    upload_docs()
