"""Coffee machine"""
AVAIL_RESOURCES = {
    "water": 5000,
    "milk": 2000,
    "coffee": 1000,
    "money": 50.00
}
REQUIRED_DRINK_RESOURCES = {
    "espresso":{
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "money": 1.50
    },
    "latte":{
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "money": 2.50
    },
    "capp":{
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "money": 3.00
    },
}

def resource_report(resource: dict = AVAIL_RESOURCES) -> str:
    water = resource["water"]
    milk = resource["milk"]
    coffee = resource["coffee"]
    money = resource["money"]
    return f"Current resources:\nWater:{water} ml\nMilk:{milk} ml\nCoffee:{coffee} g\nMoney:{money}$"

def prompt_input() -> str:
    return input("What would you like?\n").lower()

def check_if_enough_resources(drink: str = "espresso", available_resources: dict = AVAIL_RESOURCES) -> bool:
    selected_drink = REQUIRED_DRINK_RESOURCES[drink]
    water = selected_drink["water"]
    milk = selected_drink["milk"]
    coffee = selected_drink["coffee"]

    if water > available_resources["water"]:
        print(f"Not enough water! Required {water}, got {available_resources["water"]}")
        return False
    if milk > available_resources["milk"]:
        print(f"Not enough milk! Required {milk}, got {available_resources["milk"]}")
        return False
    if coffee > available_resources["coffee"]:
        print(f"Not enough coffee! Required {coffee}, got {available_resources["coffee"]}")
        return False

def machine_operations(operation: str, report: dict = AVAIL_RESOURCES) -> str:
    if operation == "off":
        return("Machine turned off!")
    if operation == "report":
        return resource_report(report)
    if operation in REQUIRED_DRINK_RESOURCES.keys():
        return check_if_enough_resources(drink=operation)
        
def main():
    response = prompt_input()
    print(machine_operations(response))

if __name__ == "__main__":
    main()