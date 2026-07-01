import json

def normalize_specs(specs):
    """
    Normalize specs into a list of {name, value} dicts.
    Accepts JSON strings, dicts, or lists.
    """
    if specs is None:
        return []
    if isinstance(specs, str):
        try:
            specs = json.loads(specs)
        except Exception:
            return [{"name": "raw", "value": specs}]
    if isinstance(specs, dict):
        return [{"name": k, "value": str(v)} for k, v in specs.items()]
    if isinstance(specs, list):
        out = []
        for item in specs:
            if isinstance(item, dict):
                n = item.get("name") or item.get("key") or "item"
                v = item.get("value")
                out.append({"name": n, "value": str(v)})
            else:
                out.append({"name": "item", "value": str(item)})
        return out
    return [{"name": "raw", "value": str(specs)}]
