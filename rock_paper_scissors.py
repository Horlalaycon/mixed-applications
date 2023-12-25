import random


# user input
user_action = input('Choose either rock, paper, or scissors: ')
# list to use to pick random options
possible_choice = ['rock', 'paper', 'scissors']
computer_random = random.randint(0, len(possible_choice) - 1)
computer_action = possible_choice[computer_random]
print(f"Computer Picked: {computer_action}")
# condition statement
# rock
if user_action == 'rock' and computer_action == 'paper':
    print("=-" * 30)
    print(f"paper cover's rock You Lose!!")
    print("=-" * 30)
elif user_action == 'rock' and computer_action == 'scissors':
    print("=-" * 30)
    print(f"rock smashes scissors You Win!!")
    print("=-" * 30)
# paper
elif user_action == 'paper' and computer_action == 'rock':
    print("=-" * 30)
    print(f"paper cover's rock You Win!!")
    print("=-" * 30)
elif user_action == 'paper' and computer_action == 'scissors':
    print("=-" * 30)
    print(f"Scissors cut paper You Lose!!")
    print("=-" * 30)
# scissors
elif user_action == 'scissors' and computer_action == 'rock':
    print("=-" * 30)
    print(f"rock smashes scissors You Lose!!")
    print("=-" * 30)
elif user_action == 'scissors' and computer_action == 'paper':
    print("=-" * 30)
    print(f"Scissors cut paper You Win!!")
    print("=-" * 30)
# draw
elif user_action == 'rock' and computer_action == 'rock':
    print("=-" * 30)
    print(f"it's a Tie")
    print("=-" * 30)
elif user_action == 'paper' and computer_action == 'paper':
    print("=-" * 30)
    print(f"it's a Tie")
    print("=-" * 30)
elif user_action == 'scissors' and computer_action == 'scissors':
    print("=-" * 30)
    print(f"it's a Tie")
    print("=-" * 30)
# else
else:
    print("=-" * 30)
    print(f"Invalid option!! choose either rock, paper, or scissor")
    print("=-" * 30)
