def emoji_converter(message):
    
    emojis = {
        ":)" : "😊",
        ":(" : "😔"
    # emojis added on windows 10, using windows logo key + semicolon key combination.
    }

    split_message = message.split(' ')
    output = ""
    for item in split_message:
        output += f'{emojis.get(item, item)} '
    
    return output

message = input("> ")
print(emoji_converter(message))