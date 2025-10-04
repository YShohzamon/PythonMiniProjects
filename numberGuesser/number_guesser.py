import random

top_of_number = input("Please enter a number: ")

if top_of_number.isdigit():
    top_of_number = int(top_of_number)

    if top_of_number <= 0:
        print("Please enter a number that is larger than 0.")
        quit()
else:
    print("Please enter a number next time.")
    quit()

random_number = random.randint(0, top_of_number)

guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please enter a number next time.")
        continue

    if user_guess == random_number:
        print("You guessed right!")
        break
    elif(user_guess < random_number):
        print("Your guess is lower.")
    else:
        print("Your guess is higher.")

print("you guessed it in", guesses, "guesses")

