monday_attendees ={"ALi","ahmed","soban","tayyab","irtaza"}
wednesday_attendees= {"irtaza","ahmed","haider","taha","mustafa"}
print(f"students who were present for both days {monday_attendees & wednesday_attendees}")
print(f"students who were present on monday only {monday_attendees- wednesday_attendees}")
print(f"students who were present on either day{monday_attendees| wednesday_attendees}")
monday_attendees.add("hamood")
wednesday_attendees.discard("taha")
name_to_check = "haider"
if name_to_check in wednesday_attendees:
    print(f"{name_to_check} attended Wednesday: True")
else:
    print(f"{name_to_check} attended Wednesday: False")