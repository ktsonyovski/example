"""Helper functions for coffee machine project."""
import json

RESOURCES_PATH = r"/home/ktsonyovski/projects/example/day_15/resources"

def load_resources(resource_path: str = RESOURCES_PATH):
    """Load resources"""
    with open(f"{resource_path}/avail_res.json", "r", encoding="utf-8") as resources:
        data = json.load(resources)
        return data["resources"]
