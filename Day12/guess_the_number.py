import random 
from tracemalloc import stop

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
NUMBER = random.randint(1, 100)
player_won = False

difficulty = input("Choose a difficulty between 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

def guess_the_number(attempts):
    global NUMBER
    global player_won
    if attempts > 1:
        print(f"You have {attempts} attempts left!")
    elif attempts == 1:
        print(f"You have {attempts} attempt left!")
    elif attempts == 0:
        print(f"You have {attempts} attempts left! You lose!")
        stop()
    guess = int(input("Make a guess: "))
    if guess != NUMBER:
        attempts -= 1
        if NUMBER > guess:
            print("The guess is too low.")
        elif NUMBER < guess:
            print("The guess is too high.")
    else:
        print(f"You got it! The answer was {NUMBER}.")
        player_won = True
    while player_won == False:
        guess_the_number(attempts)

guess_the_number(attempts)