import os, json
from dotenv import load_dotenv
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.openai import OpenAIClient

load_dotenv()

search_client = SearchClient(
    os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT"),
    os.getenv("AZURE_SEARCH_INDEX_NAME"),
    AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
)

openai_client = OpenAIClient(
    os.getenv("AZURE_OPENAI_ENDPOINT"),
    AzureKeyCredential(os.getenv("AZURE_OPENAI_API_KEY"))
)

def rag_query(user_question):
    # Step 1: Retrieve context from AI Search
    results = list(search_client.search(user_question))
    context = "\n".join([json.dumps(r) for r in results])

    # Step 2: Pass context into Azure OpenAI
    deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
    resp = openai_client.get_chat_completions(
        deployment_id=deployment,
        messages=[
            {"role": "system", "content": "You are a product assistant."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {user_question}"}
        ]
    )
    return resp.choices[0].message["content"]

if __name__ == "__main__":
    answer = rag_query("What specs does the Pro tier include?")
    print(answer)
