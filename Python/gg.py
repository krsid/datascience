"Random Number guess game"
import random

num = random.randint(1,20)

tries = 0

while True:
    guess = int(input('Guess your number between 1 to 20 :- '))

    if num == guess:
        tries += 1
        print(f"Great!, You have guessed the correct number in {tries} tries")
        break
    elif num > guess:
        tries += 1
        print("You are close guess a little higher")
    elif num < guess:
        tries += 1
        print("You are close guess a little lower")
    else:
        tries+=1
        print("You have guessed the wrong number, Try again!!")