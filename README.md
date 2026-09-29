# Trivia Quiz Game 🎯

A terminal-based, multiple-choice trivia game built in Python. This is part of my ongoing journey to strengthen my Python fundamentals by building real, working projects from scratch — no tutorials copy-pasted, every line understood.

---

## 🧠 Why This Project Is Different

Every feature here was built the slow way: understand the problem → write the smallest version → run it → read the error when it broke → fix it → move to the next piece. The full design is documented in [PROTOTYPE.md](PROTOTYPE.md) — a plain-language blueprint of the project, written so anyone could rebuild it in any language, not just Python.

---

## 📌 What It Does

- Greets the player by name
- Loads questions from a separate `questions.json` file — no editing code needed to add questions
- Lets the player pick a category
- Asks multiple-choice questions (A/B/C/D), in random order
- Checks each answer and tracks a running score
- Shows a final score and percentage at the end

---

## 🗂️ Categories

Math · Programming · Science · General Knowledge

---

## 🛠️ Built With

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

- Core Python (no external libraries required)
- Lists, dictionaries, functions, and loops
- `json` for loading questions from a separate data file
- `random` for shuffling question order

---

## 🚀 How to Run

1. Make sure you have Python 3 installed
2. Clone or download this repository
3. In your terminal, run:

```bash
python3 main.py
```

4. Enter your name, pick a category, and answer the questions

---

## 📂 Project Structure

```
quiz_game/
├── main.py          # Main script — the quiz logic
├── questions.json   # All quiz questions, kept separate from the code
├── PROTOTYPE.md      # Full design blueprint, explained in plain language
└── README.md         # Project documentation
```

---

## 📋 Example

```
What is your name? Zainab
Welcome, Zainab! Let's begin.
Choose a category:
1. math
2. programming
3. science
4. general knowledge
Enter category number: 1
What is 2 + 2?
A. 4
B. 14
C. 16
D. 25
Enter your answer: A
Correct!
```

---

## 🌱 Future Improvements

- Save high scores to a file, so they persist between runs
- Add a "play again" option
- Add a timer per question
- Randomize the order of the answer options, not just the questions

---

## 👩🏾‍💻 Author

**Zainab Toyin** — Learning Python, one project at a time
[LinkedIn](https://www.linkedin.com/zainabtoyin)