# Trivia Quiz Game — Project Prototype

This document describes the full design of the project in plain language, before any Python code. Anyone should be able to read this and rebuild the same project from scratch, in any language — not just Python.

---

## 1. Goal

Build a terminal-based trivia quiz that:
- Greets the player by name
- Lets them pick a category
- Asks multiple-choice questions from that category, in random order
- Checks each answer and tracks a score
- Shows a final score and percentage

---

## 2. Data Design

Questions are stored separately from the program logic, in a file called `questions.json`. This means questions can be added or edited without touching any code.

### Shape of one question

Each question is an object with four pieces of information:

| Field | Type | Description |
|---|---|---|
| `question` | text | The question being asked |
| `options` | list of 4 text values | The possible answers, in order |
| `answer` | one letter (A/B/C/D) | Which option is correct, by position |
| `category` | text | Which topic this question belongs to |

### Example

```json
{
    "question": "What is 2 + 2?",
    "options": ["4", "14", "16", "25"],
    "answer": "A",
    "category": "math"
}
```

The `answer` field is a **letter**, not the answer text itself — it refers to the **position** of the correct option (A = 1st option, B = 2nd, C = 3rd, D = 4th).

The full file is just a list of many of these question objects.

---

## 3. Program Flow (Step-by-Step Logic)

This is the actual "prototype" — the plan the code follows, in order:

```
1. Load all questions from questions.json into memory
   - if the file is missing or broken, show an error and stop

2. Ask the player for their name

3. Look through all loaded questions and build a list of
   unique categories (no duplicates)

4. Show the player the list of categories, numbered

5. Ask the player to pick a category by number

6. Build a new, smaller list containing only the questions
   that belong to the chosen category

7. Shuffle the order of that smaller list, so questions
   don't always appear in the same order

8. Start a score counter at 0

9. For each question in the (filtered, shuffled) list:
   a. Print the question text
   b. Print each option, labeled A, B, C, D
   c. Ask the player to type a letter
   d. Clean their answer (remove extra spaces, force uppercase)
   e. Compare it to the question's correct answer
      - if it matches: say "Correct!" and add 1 to the score
      - if it doesn't: say "Wrong!"

10. After all questions in that category are done:
    a. Count how many questions were in the filtered list
    b. Calculate percentage: (score / total) * 100
    c. Show the player's name, final score, and percentage
```

---

## 4. File Structure

```
quiz_game/
├── main.py          # the program logic (steps 1-10 above)
└── questions.json   # the question data (pure data, no code)
```

Keeping these separate is intentional — it's the core design principle of this project: **data and logic should not be mixed.** Someone can expand the quiz to hundreds of questions just by editing `questions.json`, without ever touching or risking breaking `main.py`.

---

## 5. Key Design Decisions (and why)

- **Answers are letters, not text** — this avoids issues with users typing answers in slightly different ways ("20" vs "twenty"). Picking by letter is unambiguous.
- **Categories are derived from the data, not hardcoded** — the program looks at whatever categories exist in `questions.json` and builds the menu from that automatically. Add a new category to the JSON file, and it appears in the menu with no code changes.
- **Filtering happens before shuffling** — the program narrows down to just the chosen category first, then shuffles only that smaller set. Shuffling the full list first would waste effort shuffling questions that get thrown away anyway.
- **Validation on input** — answers are cleaned with `.strip()` (removes accidental spaces) and `.upper()` (so "a" and "A" are treated the same).

---

## 6. Possible Extensions

Ideas for anyone building on this prototype further:
- Save high scores to a separate file, so they persist between runs
- Add a "replay" option instead of the program ending after one round
- Add a timer per question
- Randomize the order of the options themselves, not just the questions
- Support more than 4 options per question
 