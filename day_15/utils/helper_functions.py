"""Helper functions for coffee machine project."""
import json

RESOURCES_PATH = r"/home/ktsonyovski/projects/example/day_15/resources"
AVAIL_RESOURCES = "avail_res"
COST_FILE = "cost"

def load_json(file: str, resource_path: str = RESOURCES_PATH) -> dict:
    """Load JSON data from a file"""
    with open(f"{resource_path}/{file}.json", "r", encoding="utf-8") as resources:
        data = json.load(resources)
        return data

def get_avail_res(file: str = AVAIL_RESOURCES) -> dict:
    """Get resources from avail_resources file"""
    resource_file = load_json(file)
    avail_resources = resource_file["resources"]
    return avail_resources

def get_drink_res(drink: str, file: str = COST_FILE) -> dict:
    """Get resources from avail_resources file"""
    resource_file = load_json(file)
    drink_res = resource_file[drink]
    return drink_res

def check_sufficient_resources(drink: str) -> bool:
    """Check if there are sufficient resources to make the drink"""
    drink_resources = dict(get_drink_res(drink))
    avail_resources = dict(get_avail_res())
    
    for resource, needed in drink_resources.items():
        available = avail_resources.get(resource, 0)
        if needed > available:
            print(f"Not enough {resource}! Got {available}, needed {needed}")
            return False
    return True