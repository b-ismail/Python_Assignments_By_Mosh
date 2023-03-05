customer = {
    "name" : "John Smith",
    "age" : 30,
    # "age" : 40,       key must be unique in this case we have age as key
    "is_verified" : True
}

print(customer["name"])
print(customer["age"])

# print(customer["date"])

print(customer.get("date", "Your placeholder"))

customer["name"] = "Jack Smith"

print(customer["name"])

customer.setdefault("date", "Jan, 2020")
print(customer)

customer["exp"] = "Dec, 2022"
print(customer)