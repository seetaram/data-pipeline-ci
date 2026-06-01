import json
import os


def extract(filepath: str) -> list:
    """Read raw records from a JSON file."""
    with open(filepath, "r") as f:
        return json.load(f)


def transform(data: list) -> list:
    """Filter active records and normalize fields."""
    result = []
    for record in data:
        if record.get("status") == "active":
            result.append({
                "id": record["id"],
                "name": record["name"].strip().title(),
                "status": record["status"]
            })
    return result


def load(data: list, output_path: str) -> None:
    """Write transformed records to output JSON file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Loaded {len(data)} records to {output_path}")


if __name__ == "__main__":
    raw = extract("data/input.json")
    transformed = transform(raw)
    load(transformed, "data/output.json")
    print(f"ETL complete. {len(transformed)} records processed.")
