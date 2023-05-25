# import moudles
import random

attempts_list = []
attempts = 0

def show_score():
    if not attempts_list:
        print("don't have any score, goodbye!")
    else:
        print(f"the current high score is {min(attempts_list)} attempts")

# (pc)we will choose a random number between 1 and 10
rand_guess = random.randint(1,10)

print("hello player, welcome to the guessing game!")

player_name = input("What's your name?: ")

wanna_play = input(

    f"Hi, {player_name} would you like to play Guessing Game? "
    "enter(yes/no): "
).lower()

if wanna_play == "yes":
   print("Nice, let's go to the game...")

else:
    show_score()
    exit()

# the logic of the guessing game 
while wanna_play == "yes":

    try:

        player_guess = int(input(f"{player_name}, pick a number between 1 and 10: "))
        
        # create Value Error
        if player_guess < 0 or player_guess > 10 :
            raise ValueError("please guess a number within the given range.")
                              
        attempts += 1

        if player_guess == rand_guess:
            print(f"it's nice, {player_name} Well you guessed ")
            print(f"It took you {attempts} attempts")
            wanna_play = input("would you like to play again enter(yes/no): ").lower()

            attempts_list.append(attempts)

            if wanna_play == "no":
                print(f"that's cool,{player_name} have a good day")
            else:
                attempts = 0
                rand_guess = random.randint(1,10) 
                show_score()
                continue               
        elif player_guess < rand_guess:
            print("it's lower")

        else:
            print("it's higher")
        
    except ValueError as err:
        print(err)

     

   


