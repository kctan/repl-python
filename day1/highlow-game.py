import random

secret = random.randint(1, 20)

for i in range(1, 7):
    guess = input("Enter a number between 1 and 20: ")
    guess = int(guess)
    
    if guess == secret:
        print("You have guessed the number correctly")
        print("you have taken %d try" % i)
        break
    elif guess > secret:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
print("End of game")