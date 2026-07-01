import os, json
import psycopg2
from dotenv import load_dotenv
from transform_utils import normalize_specs

load_dotenv()

def fetch_products():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT")
    )
    cur = conn.cursor()
    cur.execute("SELECT id, name, tier, description, specs FROM products;")
    rows = cur.fetchall()
    products = []
    for r in rows:
        products.append({
            "id": str(r[0]),
            "name": r[1],
            "tier": r[2],
            "description": r[3],
            "specs": normalize_specs(r[4])
        })
    conn.close()
    return products

if __name__ == "__main__":
    docs = fetch_products()
    with open("../sample_products.json", "w") as f:
        json.dump(docs, f, indent=2)
    print(f"Exported {len(docs)} products from Postgres.")
