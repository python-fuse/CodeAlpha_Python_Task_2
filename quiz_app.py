# Define default quizzes and answers in a dictionary
default_quizzes = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Which gas do plants absorb from the atmosphere?": "Carbon dioxide",
    "What is the chemical symbol for gold?": "Au",
    "How many continents are there on Earth?": "7",
    "What is the largest mammal in the world?": "Blue whale",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the smallest prime number?": "2",
    "What is the chemical symbol for water?": "H2O",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare"
}

# Initialize points and quizzes dictionary with default values
points = 0
quizzes = default_quizzes.copy()

# Function to add a new quiz question and answer to the dictionary
def add_quiz():
    global quizzes

    # Ask if the admin wants to use default quizzes or clear them
    choice_default = input("Do you want to use default quizzes? (Y/N): ")
    if choice_default.lower() == "y":
        quizzes = default_quizzes.copy()
        print("Default quizzes loaded.")
    else:
        quizzes.clear()
        print("Cleared out existing quizzes. You can add new ones.")

    # Allow the admin to add new quizzes
    while True:
        new_quiz = input("Enter a new quiz question (or press Enter to stop adding): ")
        if not new_quiz:
            break

        new_quiz_answer = input("Enter the quiz's answer: ")
        quizzes[new_quiz] = new_quiz_answer

    choice()

# Function to ask if the user wants to add another quiz or return to the menu
def choice():
    choice = input("Enter 'A' to add another or 'Q' to return to the menu: ")
    if choice.lower() == "a":
        add_quiz()
    elif choice.lower() == "q":
        main()
    else:
        print("Invalid choice. Please enter 'A' or 'Q'.")
        choice()

# Function to play the quiz and calculate points
def quiz_app():
    global points

    for question, correct_answer in quizzes.items():
        print(f"Question: {question}")
        attempt = input("Enter answer: ")
        if attempt.lower() == correct_answer.lower():
            print("Correct")
            points += 1
        else:
            print("Wrong Answer")
            print(f"The correct answer is {correct_answer}")
    player_choice()

# Function to ask the player if they want to play again or return to the menu
def player_choice():
    choice = input("Would you like to play again? (Y/N): ")
    if choice.lower() == "y":
        play_quiz()
    elif choice.lower() == "n":
        main()
    else:
        print("Invalid choice. Please enter 'Y' or 'N'.")
        player_choice()

# Function to start playing the quiz
def play_quiz():
    print("Welcome to the quiz task!")
    print("Enter 'S' to start or 'Q' to exit to the menu")
    command = input("Enter the command: ")
    if command.lower() == "s":
        quiz_app()
    elif command.lower() == "q":
        main()
    else:
        print("Invalid choice. Please enter 'S' or 'Q'.")
        play_quiz()

# Main function to handle admin or player choices
def main():
    global points
    print('Enter "Q" at any point to quit')
    ask = input("Admin or Player: ")
    if ask.lower() == "admin":
        add_quiz()
    elif ask.lower() == "player":
        play_quiz()
    elif ask.lower() == "q":
        print(f"Thanks for playing. You scored {points} points.")
    else:
        print("Invalid choice. Please enter 'Admin', 'Player', or 'Q'.")
        main()

if __name__ == "__main__":
    main()
