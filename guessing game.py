import random
attempt=0
secretnumber=random.randint(1,100)
print("welcome to the guessing game")
guessed=False
while not guessed: 
    print("enter a number")
    number=int(input(""))
    if number < secretnumber:
        print("guessed wrong number too low")
        attempt=attempt+1
    elif number > secretnumber:
        print("guessed wrong too high")
        attempt=attempt+1
    elif number == secretnumber:
        print("u guessed correct")
        print("your total attempts are",attempt)
