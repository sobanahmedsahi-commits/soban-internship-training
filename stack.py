stack = []

stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")

removed = stack.pop()

peek = stack[-1]
if removed == "d":
    print("removed successfully")
else:
    print("try again")