import os
import pytest
from azure.search.documents.indexes import SearchIndexClient
from azure.core.credentials import AzureKeyCredential

@pytest.fixture
def index_client():
    endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    key = os.getenv("AZURE_SEARCH_API_KEY")
    return SearchIndexClient(endpoint, AzureKeyCredential(key))

def test_index_exists(index_client):
    index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")
    indexes = [i.name for i in index_client.list_indexes()]
    assert index_name in indexes, f"Index {index_name} not found in Azure AI Search"

def test_index_schema_fields(index_client):
    index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")
    index = index_client.get_index(index_name)
    field_names = [f.name for f in index.fields]
    assert "id" in field_names
    assert "name" in field_names
    assert "specs" in field_names
