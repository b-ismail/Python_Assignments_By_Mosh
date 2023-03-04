# name = input('Enter the name.')
name = 'J'
no_of_character = len(name)
if no_of_character < 3:
    print('name must be atleast 3 characters long.')
elif no_of_character > 50:
    print('name can be maximum 50 characters.')
else:
    print('name looks good!')