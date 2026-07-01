import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential

load_dotenv()

def get_search_credentials():
    endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    key = os.getenv("AZURE_SEARCH_API_KEY")
    index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")
    return endpoint, key, index_name, AzureKeyCredential(key)

def get_openai_credentials():
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    key = os.getenv("AZURE_OPENAI_API_KEY")
    embedding_deployment = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
    chat_deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
    return endpoint, key, embedding_deployment, chat_deployment, AzureKeyCredential(key)
