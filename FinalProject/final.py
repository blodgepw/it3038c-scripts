#This will be a random number guessing game
#import what you will need for the game
import random
attempts_list = []
#We need to define our variables
def show_score():
    if len(attempts_list) <= 0:
        print("No high score yet, play the game to get a new high score.")
    else:
        print("Current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 10))
    print("Welcome to the Number Guessing Game! Thanks for trying it out.")
    player_name = input("What is your name?: ")
    wanna_play = input("Hello, {}, did you want to play the number guessing game? (Enter Yes/No): ".format(player_name))
    attempts = 0
    show_score()
#this is the code for the random number game
#Write your try/if statements
    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10: ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Correct! This is the right number.")
                attempts += 1
                attempts_list.append(attempts)
                print("You had {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No): ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("Thanks for playing.")
                    break
#Import elif statements to give the user hints if their first guess is wrong.
            elif int(guess) > random_number:
                print("The number is lower.")
                attempts += 1
            elif int(guess) < random_number:
                print("The number is higher.")
                attempts += 1
#Import error code incase the user inputs the wrong values.
        except ValueError as err:
            print("What you entered is not a valid value. Please try again.")
            print("({})".format(err))
#for when the user doesn't want to play the game.
    else:
        print("Have a good day.")
if __name__ == '__main__':
    start_game()
        
