# Preparation
import random
from game_data import data
print("Welcome to HigherLower game!")
user_wrong = ""
score = 0

# Comparison
def comparison():
    global score
    global user_wrong
    user_wrong = False
    compare_a = random.choice(data)
    compare_a_name = compare_a["name"]
    compare_a_follower_count = compare_a["follower_count"]
    compare_a_description = compare_a["description"]
    compare_a_country = compare_a["country"]
    compare_b = random.choice(data)
    if compare_b == compare_a:
        compare_b = random.choice(data)
    compare_b_name = compare_b["name"]
    compare_b_follower_count = compare_b["follower_count"]
    compare_b_description = compare_b["description"]
    compare_b_country = compare_b["country"]
    print(f"Compare a: {compare_a_name}, a/an {compare_a_description}, from {compare_a_country}.")
    print("Vs.")
    print(f"compare_b: {compare_b_name}, a/an {compare_b_description}, from {compare_b_country}.")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_answer == "a":
        user_answer = compare_a_follower_count
        if compare_b_follower_count > user_answer:
            print(f"Sorry, that's wrong. Final score: {score}")
            user_wrong = True
        elif compare_b_follower_count < user_answer:
            score += 1
            print(f"You're right! Current score: {score}")
    else:
        user_answer = compare_b_follower_count
        if compare_a_follower_count > user_answer:
            print(f"Sorry, that's wrong. Final score: {score}")
            user_wrong = True
        elif compare_a_follower_count < user_answer:
            score += 1
            print(f"You're right! Current score: {score}")
    while user_wrong == "" or user_wrong == False:
        comparison()

comparison()