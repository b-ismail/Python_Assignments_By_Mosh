choice = ''
help_message = '''
start - to start the car
stop - to stop the car
quit - to exit
'''
while choice.lower() != 'quit':
    choice = input()
    if choice.lower() == 'help':
        print(help_message)
    elif choice.lower() == 'start':
        print('Car started....Ready to go!')
    elif choice.lower() == 'stop':
        print('Car stopped!')
    else:
        print("I don't understand that...")
else :
    print('Game Exited!')
