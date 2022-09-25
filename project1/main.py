import random
randNumber=random.randint(1,100)
userGuess=None
guesses=0

while (userGuess !=randNumber):
    userGuess=int(input("Enter your guess:"))
    guesses+=1
    if(userGuess==randNumber):
        print("you guessesd it right!")
    else:
        if (userGuess>randNumber):
            print("you guessed it wrong! Enter a smaller number")
        else:
            print("you guessesd it wrong! Enter a large number")

print(f"you guessed the number in {guesses} guesses")