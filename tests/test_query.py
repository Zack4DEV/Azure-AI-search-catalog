import os
import pytest
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

@pytest.fixture
def search_client():
    endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    key = os.getenv("AZURE_SEARCH_API_KEY")
    index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")
    return SearchClient(endpoint, index_name, AzureKeyCredential(key))

def test_keyword_query(search_client):
    results = list(search_client.search("Pro tier"))
    assert len(results) > 0, "No results found for keyword query"

def test_vector_query(search_client):
    # Example vector query (requires embeddings uploaded)
    vector = [0.1] * 1536  # dummy vector
    results = list(search_client.search(
        search_text="",
        vectors=[{"value": vector, "fields": ["embedding"], "k": 3}]
    ))
    assert len(results) > 0, "No results found for vector query"
