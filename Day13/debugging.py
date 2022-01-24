# #Describe Problem
# def my_function():
#     for i in range(1, 20):
#         if i == 19:
#             print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

# # Fix the Error
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}")

# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
print(f"Pages = {pages}")
print(f"word_per_page = {word_per_page}")
total_words = pages * word_per_page
print(total_words)