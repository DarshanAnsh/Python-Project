import random

user_wins = 0
computer_wins = 0
game_tied = 0

options = ["stone", "paper", "scissors"]

while True:
    user_input = input("Type stone/paper/scissors or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "stone" and computer_pick == "scissors":
        print("You won.")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "stone":
        print("You won.")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won.")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "stone":
        print("Computer won.")
        computer_wins += 1

    elif user_input == "stone" and computer_pick == "paper":
        print("Computer won.")
        computer_wins += 1       

    elif user_input == "paper" and computer_pick == "scissors":
        print("Computer won.")
        computer_wins += 1    

    else:
        print("Game Tied.")
        game_tied += 1

print("You won", user_wins, "times.")
print("The Computersaheb won", computer_wins, "times.")
print("Match Drawn", game_tied, "times.")
print("La la la la la la la la hehehe Goodbye! ")                   