#  Tuples are immutable, connot be mutated.
#  Only count and index methods.

numbers = (1, 2, 3)
try:
    numbers[0] = 10
except:
    print(numbers.count(1))


coordinates = (1, 2, 3)

# coordinates[0] * coordinates[1] * coordinates[2]
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[3]


x, y, z = coordinates

print(z, x, y)

coordinates = [4, 5, 6]


x, y, z = coordinates

print(z, x, y)
