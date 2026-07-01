import os
import pytest
from azure.ai.openai import OpenAIClient
from azure.core.credentials import AzureKeyCredential

@pytest.fixture
def openai_client():
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    key = os.getenv("AZURE_OPENAI_API_KEY")
    return OpenAIClient(endpoint, AzureKeyCredential(key))

def test_embedding_generation(openai_client):
    deployment = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
    resp = openai_client.get_embeddings(deployment_id=deployment, input="Pro tier product")
    assert resp.data[0].embedding is not None
    assert len(resp.data[0].embedding) > 100

def test_chat_completion(openai_client):
    deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
    resp = openai_client.get_chat_completions(
        deployment_id=deployment,
        messages=[{"role": "user", "content": "What specs does the Pro tier include?"}]
    )
    assert resp.choices[0].message["content"], "Chat completion returned empty content"
