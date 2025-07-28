import json

def save_annotations(annotations, filename="annotations.json"):
    """Save annotations to JSON file"""
    with open(filename, "w") as f:
        json.dump(annotations, f, indent=4)
    print(f"Annotations saved to {filename}")

def load_annotations(filename="annotations.json"):
    """Load annotations from JSON file"""
    try:
        with open(filename, "r") as f:
            annotations = json.load(f)
        print(f"Annotations loaded from {filename}")
        return annotations
    except FileNotFoundError:
        print("No saved annotations found.")
        return []
