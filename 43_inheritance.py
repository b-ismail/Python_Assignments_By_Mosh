# class Dog:
#     def walk(self):
#         print('walk')

# class Dog:
#     def walk(self):
#         print('walk')


# Best Practice, DRY - Dont repeat yourself
# pass is used as a simple statement continue in C++, to move forward with the interpreter

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    # pass
    def bark(self):
        print('bark')

class Cat(Mammal):
    # pass
    def meow(self):
        print('meow')

cat1 = Cat()
cat1.meow()
cat1.walk()

dog1 = Dog()
dog1.bark()
dog1.walk()