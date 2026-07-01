import os
from dotenv import load_dotenv
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()

endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
key = os.getenv("AZURE_SEARCH_API_KEY")
index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")

search_client = SearchClient(endpoint, index_name, AzureKeyCredential(key))

def run_query(text):
    results = search_client.search(text)
    for r in results:
        print(r["id"], r["name"], r.get("tier"))

if __name__ == "__main__":
    run_query("Pro tier products")
