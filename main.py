import random
import json

FILE_NAME = "questions.json"
LETTERS = ["A", "B", "C", "D"]


def load_questions():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("questions.json not found. Cannot start the quiz.")
        return []
    except json.JSONDecodeError:
        print("questions.json is corrupted.")
        return []


def get_categories(questions):
    categories = []
    for item in questions:
        if item["category"] not in categories:
            categories.append(item["category"])
    return categories


def choose_category(categories):
    print("Choose a category:")
    for i in range(len(categories)):
        print(f"{i + 1}. {categories[i]}")

    while True:
        choice = input("Enter category number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]
        print("Invalid choice. Try again.")


def filter_questions(questions, category):
    filtered = []
    for item in questions:
        if item["category"] == category:
            filtered.append(item)
    random.shuffle(filtered)
    return filtered


def ask_question(item):
    """Show one question, return True if answered correctly."""
    print(f"\n{item['question']}")

    valid_letters = LETTERS[:len(item["options"])]

    for i, option in enumerate(item["options"]):
        print(f"{LETTERS[i]}. {option}")

    while True:
        answer = input("Enter your answer: ").strip().upper()

        if answer in valid_letters:
            break
        print(f"Invalid input. Please enter one of: {', '.join(valid_letters)}")

    if answer == item["answer"].strip().upper():
        print("Correct!")
        return True
    else:
        print("Wrong!")
        return False

def run_quiz(questions):
    """Ask all questions, return the score."""
    score = 0
    for item in questions:
        if ask_question(item):
            score += 1
    return score


def show_results(player_name, score, total):
    percentage = (score / total) * 100
    print(f"\n{player_name}, you scored {score} out of {total}")
    print("Your percentage is:", round(percentage), "%")


def main():
    player_name = input("What is your name? ")

    questions = load_questions()
    if len(questions) == 0:
        print("No questions available. Exiting.")
        return

    print(f"Welcome, {player_name}! Let's begin.")

    categories = get_categories(questions)
    chosen_category = choose_category(categories)
    filtered_questions = filter_questions(questions, chosen_category)

    score = run_quiz(filtered_questions)
    show_results(player_name, score, len(filtered_questions))

if __name__ == "__main__":
    main()