import random

num = random.randint(1, 100)
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == num:
        print("You guessed correctly!")
        break
    elif guess < num:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")
