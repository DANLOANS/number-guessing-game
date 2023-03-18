import random

def guess_number():
    number = random.randint(1, 100)
    guesses = 0
    while guesses < 10:
        guess = int(input("Guess a number between 1 and 100: "))
        guesses += 1
        if guess == number:
            print("Congratulations! You guessed the number in", guesses, "tries.")
            return
        elif guess < number:
            print("Too low. Guess again.")
        else:
            print("Too high. Guess again.")
    print("Sorry, you didn't guess the number. The number was", number)

guess_number()
