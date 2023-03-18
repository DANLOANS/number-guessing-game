import random

# Define the range of the number to be guessed
min_num = 1
max_num = 100

# Choose a random number from the range
number = random.randint(min_num, max_num)

# Define the maximum number of guesses
max_guesses = 10

# Define a function to display the current state of the game
def display_game_state(num_guesses):
    print("Guess a number between", min_num, "and", max_num)
    print("Number of guesses remaining:", max_guesses - num_guesses)

# Define the game loop
num_guesses = 0
while num_guesses < max_guesses:
    # Display the current state of the game
    display_game_state(num_guesses)
    
    # Prompt the player to guess a number
    guess = input("Guess a number: ")
    
    # Check if the guess is valid
    try:
        guess = int(guess)
    except:
        print("Invalid guess, please enter a number.")
        continue
    
    if guess < min_num or guess > max_num:
        print("Invalid guess, please enter a number between", min_num, "and", max_num)
        continue
    
    # Increment the number of guesses
    num_guesses += 1
    
    # Check if the guess is correct
    if guess == number:
        print("Congratulations, you guessed the number in", num_guesses, "guesses!")
        break
    
    # Check if the guess is too high or too low
    if guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
else:
    print("Sorry, you ran out of guesses. The number was", number)