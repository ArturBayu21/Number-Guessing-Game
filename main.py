import random
import os
import art


# =================== Function needed ====================

def lives_generator(difficulty):
    '''return lives based on difficulty that the user choose'''
    lives = 0
    if difficulty == 'easy':
        lives = 10
    else:
        lives = 5
    return lives


def decrease_a_live(lives):
    '''return lives that decreased by 1'''
    lives -= 1
    return lives


def check_position(user_number, random):
    '''return a string that tells the user wheather their guess is too high or too low'''
    if user_number > random:
        print("Too high!")
    else:
        print("Too low!")

# ==========================================================


def play_the_game():
    print(art.logo)
    random_number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thingking of a number between 1 too 100.")
    user_difficulty = input(
        "Choose a difficulty: type 'easy' or 'hard' : ").lower()
    user_lives = lives_generator(user_difficulty)

    should_continue = True
    while should_continue == True:
        if user_lives != 0:
            print(
                f"You have {user_lives} attempts remaining to guess the number")
            guess = int(input("Make a guess : "))
            if guess == random_number:
                print(f"You got it! the answer was {random_number}")
                should_continue = False
                play_again = input(
                    "Type 'yes' to play again, otherwise type 'no' : ").lower()
                if play_again == 'yes':
                    os.system('cls')
                    play_the_game()
            else:
                check_position(guess, random_number)
                user_lives = decrease_a_live(user_lives)
        else:
            print(f"You've run out of lives, game over.")
            should_continue = False
            play_again = input(
                "Type 'yes' to play again, otherwise type 'no' : ").lower()
            if play_again == 'yes':
                os.system('cls')
                play_the_game()


play_the_game()
