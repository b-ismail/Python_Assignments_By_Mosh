digits = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five",
    6 : "Six",
    7 : "Seven",
    8 : "Eight",
    9 : "Nine"
}

phone = input("Phone: ")
string = ""
for item in phone:
    string += f'{digits.get(int(item), "!")} '
print(string)

#  another way
# phone = input("Phone: ")
# string = ""
# for item in range(len(phone)):
#     string += f'{digits.get(int(phone[item]))} '
# print(string)