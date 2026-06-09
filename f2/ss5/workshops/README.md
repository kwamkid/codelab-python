# 📂 Workshops · F2 Session 5 — While Loops + random

**Focus:** `while` loop · `random.randint` / `random.choice` · for vs while

## 🖥️ Workshop Files

| # | File | Description | Time |
|---|------|-------------|------|
| W1 | [workshop_01_dice_roll.py](workshop_01_dice_roll.py) | 🎲 Roll until 6 (while + random) | 10 min |
| W2 | [workshop_02_count_two_ways.py](workshop_02_count_two_ways.py) | 🔁 Count 1-10 with for AND while | 15 min |
| Mini | [mini_for_vs_while.py](mini_for_vs_while.py) | 🤔 5 problems — pick the right loop | 10 min |
| 🎯 Project | [project_guess_number.py](project_guess_number.py) | 🎯 Guess 1-100 with hints | 25 min |

## 🏠 Homework (3 levels)

| Level | File | Stars |
|-------|------|-------|
| HW1 Required | [hw1_capital_quiz.py](hw1_capital_quiz.py) — Ask until "Bangkok" | ⭐⭐ |
| HW2 Advanced | [hw2_guess_count.py](hw2_guess_count.py) — Guess + rate performance | ⭐⭐⭐ |
| HW3 Expert | [hw3_rock_paper_scissors.py](hw3_rock_paper_scissors.py) — 5-round RPS game | ⭐⭐⭐⭐⭐ |

## 📦 Requirements

None — pure Python (uses built-in `random`).

## 🧭 Prerequisites

- F2 ss4 — for loops with lists
- F2 ss3 — for + range + accumulator

## 🔑 Key Concepts

```python
import random

# while — loops until condition is False
i = 0
while i < 10:
    print(i)
    i = i + 1     # MUST change i, or infinite loop!

# Random integers — randint(a, b) — BOTH included!
dice = random.randint(1, 6)        # 1, 2, 3, 4, 5, or 6

# Random pick from a list
move = random.choice(["rock", "paper", "scissors"])

# for vs while — when to use each
# for = known count       → for i in range(10):
# while = until condition → while guess != secret:
```

## 🎯 Big Idea

**`for` runs a known number of times. `while` runs UNTIL something is true.**
Picking the right loop makes your code shorter and clearer.

Common while use cases:
- Until user gives correct answer (login, quiz)
- Until you roll a 6 (game mechanic)
- Until you save enough money (simulation)
- Until enemy HP = 0 (game logic)
