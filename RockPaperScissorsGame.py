import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

user_score = 0
computer_score = 0

while True:
    print("\nRock-Paper-Scissors Game")
    print("Choose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    user_choice = input("Enter your choice (1/2/3/4): ")

    if user_choice == "4":
        break
    elif user_choice not in ["1", "2", "3"]:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        continue

    user_choice_text = ""
    if user_choice == "1":
        user_choice_text = "Rock"
    elif user_choice == "2":
        user_choice_text = "Paper"
    elif user_choice == "3":
        user_choice_text = "Scissors"

    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    result = determine_winner(user_choice_text, computer_choice)

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    print(f"Your choice: {user_choice_text}")
    print(f"Computer's choice: {computer_choice}")
    print(result)
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")

print("\nThanks for playing!")
