inventory = {
    'key': 3,
    'mace': 1,
    'gold coin': 24,
    'lantern': 1,
    'stone': 10
}

total = 0

print('Equipment:')
for item in inventory:
    print(inventory[item], item)
    total += inventory[item]

print('Total number of things:', total)