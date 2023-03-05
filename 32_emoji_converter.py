

emojis = {
    ":)" : "😊",
    ":(" : "😔"
# emojis added on windows 10, using windows logo key + semicolon key combination.
}
message = input(">")
split_message = message.split(' ')
output = ""
for item in split_message:
    output += f'{emojis.get(item, item)} '
print(output)