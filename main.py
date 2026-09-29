import random
import json

FILE_NAME = "questions.json"


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


player_name = input("What is your name? ")

Question = load_questions()

if len(Question) == 0:
    print("No questions available. Exiting.")
else:
    categories = []
    for item in Question:
        if item["category"] not in categories:
            categories.append(item["category"])

    print(f"Welcome, {player_name}! Let's begin.")

    print("Choose a category:")
    for i in range(len(categories)):
        print(f"{i + 1}. {categories[i]}")

    category_choice = input("Enter category number: ").strip()
    chosen_category = categories[int(category_choice) - 1]

    filtered_questions = []
    for item in Question:
        if item["category"] == chosen_category:
            filtered_questions.append(item)

    random.shuffle(filtered_questions)

    score = 0
    letters = ["A", "B", "C", "D"]

    for item in filtered_questions:
        print(item["question"])

        for i in range(len(item["options"])):
            print(f"{letters[i]}. {item['options'][i]}")

        answer = input("Enter your answer: ").strip().upper()

        if answer == item["answer"]:
            print("Correct!")
            score = score + 1
        else:
            print("Wrong!")

    total_question = len(filtered_questions)
    percentage = (score / total_question) * 100

    print(f"\n{player_name}, you scored {score} out of {total_question}")
    print("Your percentage is: ", round(percentage), "%")