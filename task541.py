a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

for key in a:
    if key in b and a[key] == b[key]:
        print((key, a[key]))