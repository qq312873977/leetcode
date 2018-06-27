ids = [1, 4, 3, 3, 4, 2, 3, 4, 5, 6, 1]
reduce(lambda x, y: x if y in x else x + [y], [[], ] + ids)
