# 📂 Workshops · F1 Session 2 — Data Types & Casting

**Focus:** 3 data types (str/int/float), input() to talk with users, and casting between types

## 🖥️ Workshop Files

| # | File | Description | Time |
|---|------|-------------|------|
| W1 | [workshop_01_type_checker.py](workshop_01_type_checker.py) | 🔍 Use type() to check data types | 10 min |
| W2 | [workshop_02_chatbot.py](workshop_02_chatbot.py) | 💬 Chatbot V1 — input() + f-string | 15 min |
| Mini | [mini_next_year.py](mini_next_year.py) | 🎂 Cast string → int + add 1 | 10 min |
| 🎯 Project | [project_age_calculator.py](project_age_calculator.py) | 🗓️ Birth year (พ.ศ.) → age | 25 min |

## 🏠 Homework (2 levels)

| Level | File | Stars |
|-------|------|-------|
| HW1 Required | [hw1_hero_card_v2.py](hw1_hero_card_v2.py) — Hero Card V2 with input() | ⭐⭐ |
| HW2 Advanced | [hw2_mad_libs_v2.py](hw2_mad_libs_v2.py) — Mad Libs V2 (str + int) | ⭐⭐⭐ |

## 📦 Requirements

None — pure Python only this session.

## 🧭 Prerequisites

- F1 S1 — variables, print(), Trinket basics

## 🔑 Key Concepts

```python
# Three data types
name = "Alex"     # str  (string — text)
age  = 10         # int  (integer — whole number)
pi   = 3.14       # float (decimal)

# input() — get answer from user
answer = input("What's your name? ")
# ⚠️ input() ALWAYS returns a STRING!

# Casting — convert between types
age_text = input("Age: ")    # "10"  (string)
age = int(age_text)          # 10    (integer)
print(age + 1)               # 11    (math works!)
```

## 🎯 Big Idea

**input() always returns a string.**
If the user types `10`, you get `"10"` (text), not `10` (number).
To do math, you must `int()` it first.

This is the #1 beginner gotcha — the quizzes test it!
