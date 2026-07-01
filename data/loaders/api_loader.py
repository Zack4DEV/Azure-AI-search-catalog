import os, json, requests
from transform_utils import normalize_specs
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("CATALOG_API_URL", "https://example.com/api/products")

def fetch_products():
    resp = requests.get(API_URL, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    products = []
    for item in data:
        products.append({
            "id": str(item["id"]),
            "name": item["name"],
            "tier": item.get("tier", "Standard"),
            "description": item.get("description", ""),
            "specs": normalize_specs(item.get("specs"))
        })
    return products

if __name__ == "__main__":
    docs = fetch_products()
    with open("../sample_products.json", "w") as f:
        json.dump(docs, f, indent=2)
    print(f"Fetched {len(docs)} products from API.")
