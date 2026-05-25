import sys

inventory = {}

print(f" === Inventory System Analysis ===")

for parameter in sys.argv[1:]:
    if ":" not in parameter:
        print(f"Error- invalid parameter '{parameter}'")
        continue
    part = parameter.split(":")

    if len(part) != 2:
        print(f"Error - invalid parameter '{parameter}'")
        continue

    item_name = part[0]
    quantity_str = part[1]

    if item_name in inventory:
        print(f"Redundant item '{item_name}' - discarding")
        continue
    try:
        quantity = int(quantity_str)
    except ValueError as error:
        print(f"Quantity error for '{item_name}': {error}")
        continue

    inventory[item_name] = quantity

print(f"Got inventory:", inventory)


item_list = list(inventory.keys())

print("Item list:", item_list)

total_quantity = sum(inventory.values())

print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

for item in inventory:

    quantity = inventory[item]

    percentage = (quantity / total_quantity) * 100

    print(
        f"Item {item} represents "
        f"{round(percentage, 1)}%"
    )


most_abundant_item = None
most_abundant_quantity = None

least_abundant_item = None
least_abundant_quantity = None


for item in inventory:

    quantity = inventory[item]

    if (
        most_abundant_quantity is None
        or quantity > most_abundant_quantity
    ):
        most_abundant_item = item
        most_abundant_quantity = quantity

    if (
        least_abundant_quantity is None
        or quantity < least_abundant_quantity
    ):
        least_abundant_item = item
        least_abundant_quantity = quantity


print(
    f"Item most abundant: "
    f"{most_abundant_item} "
    f"with quantity "
    f"{most_abundant_quantity}"
)

print(
    f"Item least abundant: "
    f"{least_abundant_item} "
    f"with quantity "
    f"{least_abundant_quantity}"
)


inventory.update({
    "magic_item": 1
})


print("Updated inventory:", inventory)