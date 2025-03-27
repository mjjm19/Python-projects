import random

points = 0
computer_points = 0

options = ["rock", "paper","scissors"]

while True:
    user_input = input("Choose rock, paper, scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue   

    random_number = random.randint(0,2)
    computer_guess = options[random_number]
    print("Computer chose", computer_guess)

    if user_input == "rock" and computer_guess == "scissors":
        print("You won!")
        points += 1

    elif user_input == "paper" and computer_guess == "rock":
        print("You won!") 
        points += 1

    elif user_input == "scissors" and computer_guess == "paper":
        print("You won!")
        points += 1

    elif user_input == computer_guess:
        print("It is a tie!")
    else:
        print("Computer won!")
        computer_points += 1

print(f"You won {points} times")
print(f"Computer won {computer_points} times")
print("Goodbye!")