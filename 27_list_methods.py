numbers = [5, 2, 1, 7, 4]

numbers.append(12)
print(numbers)

numbers.insert(10, 15)
print(numbers)

numbers.insert(2, 21)
print(numbers)

popped_element = numbers.pop()
print(numbers)
print(popped_element)

print(numbers.index(2))


try:
    find = 47
    print(f'{find in numbers}, bool eill be returned.')
    print(numbers.index(find))
except:
    print(f'{numbers.count(find)}, total occourances.')



numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers.append(10)
print(numbers)
print(numbers2)