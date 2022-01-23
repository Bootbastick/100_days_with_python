print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
q = input("There is a crossroad in front of you. Where do you want to go? Left or right?\n").lower()
if q == "left" or q == 'l':
  q = input("You come to the lake, that crosses the river. The road continues on the other side. What will you do? Swim or wait?\n").lower()
  if q == "w" or q == "wait":
    print("You wait some time and you see a raft coming to you. The man on the raft takes you on the other side and tells you about the crocodiles in the river. You're happy you waited some time.")
    q = input("You follow the road, untill it stops in front of the big building. The building has 3 doors. Which one will you choose? Red, blue or yellow?\n").lower()
    if q == "y" or q == "yellow":
      print("You entered the room with the yellow door. In the middle of the room is a treasure chest. You've done it! You have found the treasure! You won!")
    elif (q == "r" or q == "red") or (q == "b" or q == "blue"):
      print("You enetr a normal room, but you step on the trap door and you fall a long way down. When you hit the ground, you aren't there anymore. Game over!")
  elif q == "s" or "swim":
    print("You start swimming across the river. All of a sudden you see a crocodile. You turn around and swim to the nearest shore, but it's too late. Game over!")
elif q == "r" or q == "right":
  q = input("You enter a small town. It's getting dark. You can stay in the town or go on the road. What will you choose - stay or go?").lower()
  if q == "s" or "stay":
    q = input("You stay in the town for one night. What to do now? You can peacfuly live in the village or you can proceed with the mission.").lower()
    if q == "l" or q == "live":
      print("You live in the village for several weeks. One evening you see a paper on your table. On the paper there are only two words:'The mission'. You ignore it, because you're drunk and go to bed. On the next day you don't wake up. Game over!")
    elif q == "m" or "mission":
      print("Part 3 is coming!")
  elif q == "g" or q == "go":
    print("You go on the road. Once you went far from the town, you see a campfire. You think there's somebody near it and that you can spend the night with them, but when you go near it - there's nobody there. In the same moment you hear an arrow flying and turn around. The arrow's for your head. Game over!")