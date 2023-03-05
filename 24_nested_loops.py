# list of coordinates

# (x, y)
# (0,0)
# (0,1)
# (0,2)
# (1,0)
# (1,1)
# (1,2)

for x in range(3):
    for y in range(2):
        print(f'({x},{y})')
print("")

# Printing an F with various lines of 'X' using the list of numbers provided
numbers = [5, 2, 5, 2, 2]
for i in numbers:
    print('X' * i)
print("")

# Printing an L with various lines of 'X' using the list of numbers provided
numbers = [2, 2, 2, 2, 5]
for i in numbers:
    print('X' * i)

