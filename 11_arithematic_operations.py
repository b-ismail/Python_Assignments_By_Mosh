print(10+3)
print(10-3)
print(10*3)
print(10/3) # returns float
print(10//3) # returns integer
print(10%3) # remainder
print(10**3) # power(exponentiation)

#  Augmented assignment operator

x=10
x=x+3
print(x)

x += 3
print(x)

x-=3
print(x)

#  Operator presidence 
#  parenthesis
#  exp
#  multiplication or ZeroDivision
#  addition or subtraction

x=10+3*2
print(x)

x=10+3*2**2
print(x)

x=(10+3)*2**2
print(x)

x=(2+3) * 10 -3
print(x)