import csv, json
from transform_utils import normalize_specs

def load_csv(path="products.csv"):
    products = []
    with open(path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products.append({
                "id": row["id"],
                "name": row["name"],
                "tier": row.get("tier", "Standard"),
                "description": row.get("description", ""),
                "specs": normalize_specs(row.get("specs"))
            })
    return products

if __name__ == "__main__":
    docs = load_csv()
    with open("../sample_products.json", "w") as f:
        json.dump(docs, f, indent=2)
    print(f"Exported {len(docs)} products from CSV.")
