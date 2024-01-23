import random
print("Rock")
print("Paper")
print("Scissors")
user_choice = input("Choose your option: ")
computer = random.randint(1, 3)

if computer == 1:
    print("Computer has choosen scissors")
    if user_choice == "Paper":
        print("Computer wins")
    elif user_choice == "Scissors":
        print("Tie")
    elif user_choice == "Rock":
        print("Player Wins")

elif computer == 2:
    print("Computer has choosen Rock")
    if user_choice == "Paper":
        print("Player wins")
    elif user_choice == "Scissors":
        print("Computer Wins")
    elif user_choice == "Rock":
        print("Tie")

elif computer == 3:
    print("Computer has choosen Paper")
    if user_choice == "Paper":
        print("Tie")
    elif user_choice == "Scissors":
        print("Player Wins")
    elif user_choice == "Rock":
        print("Computer Wins ")
