lista = [
    'Davi',
    1,
    1.1,
    True,
    [10, 20, 30],
    (0, 1),
    {0, 1},
    {'Nome': 'Davi'}
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item)

    elif isinstance(item, str):
        print(item.upper())

    elif isinstance(item, list):
        for index, x in enumerate(item):
            print(index, x)

    elif isinstance(item, (int, float)):
        print(item * 2)

    else:
        print(item, 'OUTRO')
