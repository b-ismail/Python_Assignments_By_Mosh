names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
names[0] = names[0].replace('h', '')
print(names[0])
print(names[-1])
print(names[2])
print(names[-2])
print(names[-3])
print(names[1:-1])

print()

list_numbers = [1,8,15,16,82,3,2,7,1]
highest = 0
for i in list_numbers:
    if i > highest:
        highest = i
print(highest)