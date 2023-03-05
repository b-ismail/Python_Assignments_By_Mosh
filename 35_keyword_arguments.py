def greet_user(first_name, last_name):  
    print(f"Hi there! {first_name} {last_name}")
    print("Welcome aboard")

#  keyword arguments, always after positional arguments
print('Start')
greet_user(first_name = 'John', last_name = 'Smith')
# greet_user(first_name = 'Mary', 'Jane')
greet_user('Jane', last_name = 'Mary')
greet_user('','')
print('Finish')