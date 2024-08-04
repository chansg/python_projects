import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
moves = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)
print(moves[computer_choice])
print("Computer chose:")
print(moves[player_choice])

if player_choice == 0:
    if computer_choice == 1:
        print("You lose") # Rock < Paper
    elif computer_choice == 2:
        print("You win") # Rock > Scissors
elif player_choice == 1:
    if computer_choice == 0:
        print("You win") # Paper > Rock
    elif computer_choice == 2:
        print("You lose") # Paper > Scissors
elif player_choice == 2:
    if computer_choice == 0:
        print("You lose") # Scissors < Rock
    elif computer_choice == 1:
        print("You win") # Scissors > Paper
else:
    print("You draw")


