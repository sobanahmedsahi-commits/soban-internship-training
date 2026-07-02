def si(principle,rate,time):# function for calculating simple interest
    si=(principle * rate * time) / 100
    return si
def emi(principle,rate,time): # function for calculating EMI
    emi=(principle * rate *(1 + rate)**time) / (1 + rate)**time -1
    return emi #allows to call the function whenever we want without needing to rewrite the whole block of code"
def main():
    print("welcome to Simple interest and EMI calculator")
    print("press 1 for Simple interest calculator and 2 for EMI calculator")
    choice = int(input("Choose an option (1 or 2): "))


    principal = float(input("Enter Principal amount: "))
    rate = float(input("enter yearly rate: "))
    time = float(input("enter time in years")) 

    if choice == 1:
        result = si(principal, rate, time)
        print("your simple interest is :",result)
    elif choice ==2:
        result = emi(principal , rate, time)
        print("your EMI is", result)
    else: 
        print("invalid choice enter again!")
main()