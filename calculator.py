print("enter 1st number: ")
num1=float(input("num1"))
print("enter second number: ")
num2=float(input("num2"))
print("enter which operation +,-,/,*")
choice=input("choice")
if choice== "+":
    result= num1 + num2 
    print("your answer is",result)
elif choice== "-":
    result= num1 - num2
    print("your answer is",result)
elif choice=="*":
    result= num1 * num2
    print("your answer is",result)
elif choice == "/":
        result= num1 / num2
        print("your answer is",result)
    

