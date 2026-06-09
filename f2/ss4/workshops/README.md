# 📂 Workshops · F2 Session 4 — Loops + Lists

**Focus:** `for item in list`, `enumerate()`, `max/min/sum`, accumulator pattern

## 🖥️ Workshop Files

| # | File | Description | Time |
|---|------|-------------|------|
| W1 | [workshop_01_roll_call.py](workshop_01_roll_call.py) | 📋 Loop a list of friends | 10 min |
| W2 | [workshop_02_test_scores.py](workshop_02_test_scores.py) | 📊 Stats with max/min/sum | 15 min |
| Mini | [mini_coin_hunt.py](mini_coin_hunt.py) | 🪙 DIY accumulator (no built-ins) | 15 min |
| 🎯 Project | [project_snack_budget.py](project_snack_budget.py) | 🍿 7-day budget analyzer | 25 min |

## 🏠 Homework (3 levels)

| Level | File | Stars |
|-------|------|-------|
| HW1 Required | [hw1_my_scores.py](hw1_my_scores.py) — Real school scores | ⭐⭐ |
| HW2 Advanced | [hw2_seven_eleven.py](hw2_seven_eleven.py) — Real 7-11 prices | ⭐⭐⭐ |
| HW3 Expert | [hw3_grade_card.py](hw3_grade_card.py) — Class grade letters | ⭐⭐⭐⭐⭐ |

## 📦 Requirements

None — pure Python only.

## 🧭 Prerequisites

- F2 ss3 — for + range + accumulator
- F2 ss1 — list basics (append, index)

## 🔑 Key Concepts

```python
# Walk a list — no index needed
friends = ["Alex", "Bob", "Cat"]
for friend in friends:
    print(friend)

# Need both index AND value? enumerate
for i, friend in enumerate(friends):
    print(f"{i}. {friend}")

# Stats — built-in functions
scores = [85, 92, 78, 95, 88]
print(max(scores))   # 95
print(min(scores))   # 78
print(sum(scores))   # 438
avg = sum(scores) / len(scores)

# DIY accumulator (Mini exercise)
total = 0
biggest = 0
for n in scores:
    total = total + n
    if n > biggest:
        biggest = n
```

## 🎯 Big Idea

Lists + loops = **data analysis** — total spending, best score, cheapest item.
Real-world programming uses these patterns ALL THE TIME.
