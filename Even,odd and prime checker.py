def is_even(number):
    return number % 2 == 0 #it will ONLY return value if its even

def is_prime(number):
    if number < 2:         #to check if number is not 1 or 0
        return False 

    for i in range(2, number):      # loop will run till the number to check factors 

        if number % i == 0:        #"%" is mod and returns remainder,meaning if the remainder is 0 between 2 and inputted number the number is not prime hence returns a False
            
            return False

    return True  #if the above IF is not completed Return is True

def main():
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))

    for num in range(start, end + 1):
        even_status = "Even" if is_even(num) else "Odd"
        prime_status = "Prime" if is_prime(num) else "Not Prime"
        print(f"{num} -> {even_status}, {prime_status}")

main()