#Import the required modules.

import random

# Define a function to display the current high score.

def show_score(attempts_list):
    """
    Display the current high score.
    
    Parameters:
        attempts_list (list): List of integers representing the number of attempts made in previous games.
    """
    if not attempts_list:
        print("No scores yet. Goodbye!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts.")

def play_game():
    """
    Play the guessing game.
    """
    attempts_list = []
    rand_guess = random.randint(1, 10)
    player_name = input("What's your name?: ")
    wanna_play = input(f"Hi, {player_name}, would you like to play Guessing Game? (yes/no): ").lower()

    if wanna_play != "yes":
        show_score(attempts_list)
        return

    print("Nice! Let's start the game...")

    while True:
        try:
            player_guess = int(input(f"{player_name}, pick a number between 1 and 10: "))
            
            if player_guess < 1 or player_guess > 10:
                raise ValueError("Please guess a number within the given range.")
                                  
            attempts = 1

            while player_guess != rand_guess:
                if player_guess < rand_guess:
                    print("It's higher.")
                else:
                    print("It's lower.")
                
                player_guess = int(input(f"{player_name}, pick another number: "))
                attempts += 1

            print(f"It's nice, {player_name}! You guessed it!")
            print(f"It took you {attempts} attempts.")

            wanna_play = input("Would you like to play again? (yes/no): ").lower()

            attempts_list.append(attempts)

            if wanna_play != "yes":
                print(f"That's cool, {player_name}. Have a good day!")
                show_score(attempts_list)
                break

            rand_guess = random.randint(1, 10)
            print("Let's go again!")

        except ValueError as err:
            print(err)

# Play the game
play_game()
