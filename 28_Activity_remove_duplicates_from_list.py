numbers = [1, 7, 5, 1, 6, 8, 9, 10, 9, 1, 3, 2, 1, 15, 20, 61, 8]
non_redundant = []
for item in numbers:
    if item not in non_redundant:
        non_redundant.append(item)

print(numbers)
print(non_redundant)
non_redundant.sort()
print(non_redundant)