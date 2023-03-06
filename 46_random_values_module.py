import random

for i in range(3):
    print(random.random())  # values b/w 0 and 1 floats
    print(random.randint(0,50))  # values b/w a preset range ints


members = ['John', 'Mary', 'Bob', 'Josh']
print(random.choice(members))
