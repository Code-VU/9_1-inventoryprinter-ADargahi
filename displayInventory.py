stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    count = 0

    for item, val in reversed(inventory.items()):
        print(val, item)
        count += int(val)
    print("Total number of items:", count)

displayInventory(stuff)