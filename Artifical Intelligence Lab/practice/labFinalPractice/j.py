from random import randint

for i in range(1,6):
    n=int(input("Enter the guessed number = "))
    random = randint(1,5)

    if n==random :
        print("you have won the game.")
    else:
        print("You have lost.")
        print("Random Number is = ",random)


