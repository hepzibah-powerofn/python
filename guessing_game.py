import random
print("welcome to Guessing Games!")
print("----------------------------")
guessint=random.randint(1,100)
for loop in range(1,11):
    print("\nguess the number(trial "+str(loop)+" ):")
    num=int(input())
    if(num<1 or num>100):
        print("Enter a number in 1-100 range!")
    else:
        if num<guessint:
            print("your guess is too low!")
        elif num>guessint:
            print("your guess is too high")
        else:
            break
if num==guessint:
    print("\nGreat! "+str(guessint)+" is the number!\n"+"Guessed it in "+str(loop)+" guesses!")
else:
    print("\nSorry! you have exceeded the limit!\n"+str(guessint)+" is the number")
