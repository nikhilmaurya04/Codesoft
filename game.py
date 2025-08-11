import random

def rock_paper_scissors():
    # Score tracking
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.")

    while True:
        # User input
        user_choice = input("\nChoose Rock, Paper, or Scissors: ").strip().lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        # Computer selection
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer_choice.capitalize()}")

        # Game logic
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Display scores
        print(f"Score -> You: {user_score}, Computer: {computer_score}")

        # Play again prompt
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Run the game
rock_paper_scissors()
