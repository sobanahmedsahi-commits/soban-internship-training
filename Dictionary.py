
phone_book = {
    "Ahmed": "11212121212",
    "Taha": "2323232323223",
    "Soban": "343443343434",
    "Ali": "45454545454545",
}
phone_book["syed"] = "6767677676767"
phone_book["hamood"] = "856484563345"
phone_book.pop("Ali")
print("Phone Book:")
for name, number in phone_book.items():
    print(f"{name}: {number}")
name_to_check = "Sara"
if name_to_check in phone_book:
    print(f"{name_to_check} found! Number: {phone_book[name_to_check]}")
else:
    print(f"{name_to_check} not found!")