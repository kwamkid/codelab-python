# 📂 Workshops · F2 Session 1 — Lists Intro

**Focus:** Create lists, append/remove/pop, len(), in operator

## 🖥️ Workshop Files

| # | File | Description | Time |
|---|------|-------------|------|
| W1 | [workshop_01_seven_eleven.py](workshop_01_seven_eleven.py) | 🛒 Shopping list (append + remove) | 10 min |
| W2 | [workshop_02_school_bag_TEMPLATE.py](workshop_02_school_bag_TEMPLATE.py) | 🎒 CTk GUI bag manager | 15 min |
| Mini | [mini_check_pencil.py](mini_check_pencil.py) | 🔍 Use `in` to find an item | 10 min |
| 🎯 Project | [project_holiday_plan.py](project_holiday_plan.py) | 🏖️ All ops: build + edit + check | 25 min |

## 🏠 Homework (3 levels)

| Level | File | Stars |
|-------|------|-------|
| HW1 Required | [hw1_camp_supplies.py](hw1_camp_supplies.py) — 10 items + remove 3 | ⭐⭐ |
| HW2 Advanced | [hw2_playlist.py](hw2_playlist.py) — Songs + check exists | ⭐⭐⭐ |
| HW3 Expert | [hw3_weekly_menu.py](hw3_weekly_menu.py) — 7-item limit (len + if) | ⭐⭐⭐⭐⭐ |

## 📦 Requirements

```bash
pip install customtkinter
```

(only for Workshop 2)

## 🧭 Prerequisites

- F1 complete — variables, input, casting, math, if-else, light loops & lists

## 🔑 Key Concepts

```python
# Create
friends = ["Alex", "Bob", "Cat"]

# Add to end
friends.append("Dan")

# Remove by name
friends.remove("Bob")

# Drop the last
last = friends.pop()

# Check membership
if "Alex" in friends:
    print("Found!")

# Count items
print(len(friends))
```
