choice = ''
is_started = False
help_message = '''

start - to start the car
stop - to stop the car
quit - to exit

'''
while choice.lower() != 'quit':
    choice = input("> ")
    if choice.lower() == 'help':
        print(help_message)
    elif choice.lower() == 'start':
        if is_started:
            print("Already started!")
        else:
            is_started = True
            print('Car started....Ready to go!')
    elif choice.lower() == 'stop':
        if is_started:
            is_started = False
            print('Car stopped!')
        else:
            print('Car already stopped!')
    else:
        print("I don't understand that...")
else :
    print('Game Exited!')
