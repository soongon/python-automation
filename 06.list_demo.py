favorite_colors = ['red', 'green', 'blue', 'orange', 'pink', 'tan']

# CRUD .. Create
favorite_colors.append('white')
print(favorite_colors)

# CRUD .. Update
favorite_colors.insert(1, '초록')
print(favorite_colors)
favorite_colors.remove('green')
print(favorite_colors)

# CRUD .. Read -> indexing, slicing
print(favorite_colors[2])
print(favorite_colors[1: -2])
