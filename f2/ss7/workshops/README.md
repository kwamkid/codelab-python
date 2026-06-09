# Workshops · F2 Session 7 — Loop Control + The Pain

**Focus:** `break` · `continue` · Setup for Functions (S8)
**Pedagogy:** Make students FEEL the pain of copy-paste before teaching `def`

---

## Workshop Files (in class)

| # | File | Description | Time |
|---|------|-------------|------|
| W1 | [workshop_01_stop_count.py](workshop_01_stop_count.py) | Stop the Count — break + continue compared | 15 min |
| W2 | [template_w2_defuse_bomb.py](template_w2_defuse_bomb.py) | Defuse the Bomb — PyGame template | 15 min |
| Mini | [mini_find_friend.py](mini_find_friend.py) | Find Your Friend — search with break | 15 min |
| 🔥 PROJECT | [project_5_items_pain.py](project_5_items_pain.py) | 5-Item Pricing — THE PAIN (no AI, no function) | 25 min |

---

## Homework (3 Tiers)

| Tier | File | For |
|---|---|---|
| HW1 (Required) | [hw1_atm_simulator.py](hw1_atm_simulator.py) | Everyone — ATM with break |
| HW2 (Advanced) | [hw2_password_lock.py](hw2_password_lock.py) | Challenge — 3-try password |
| HW3 🔥 (Pain + Share) | [hw3_pain_share.md](hw3_pain_share.md) | Everyone — feel the pain + share screenshot |

---

## Requirements

- Python 3 + VS Code
- PyGame (for W2): `pip install pygame`
- LINE app (for HW3 Part B)

---

## Prerequisites — from S3-S5

- `for + range()` and `for item in list`
- `while + condition`
- Indentation matters

---

## Key Code Patterns

```python
# ── BREAK — stop immediately ──
for i in range(1, 21):
    if i == 13:
        break       # exit loop NOW
    print(i)
# Output: 1, 2, ..., 12

# ── CONTINUE — skip this round, keep going ──
for i in range(1, 21):
    if i == 13:
        continue    # skip print, go to next i
    print(i)
# Output: 1, 2, ..., 12, 14, 15, ..., 20

# ── BREAK in search ──
names = ["Aim", "Bar", "Tang", "Mai"]
target = "Tang"
for i, name in enumerate(names):
    if name == target:
        print(f"Found at position {i}")
        break
else:
    print("Not found")    # only runs if break did NOT trigger
```

---

## Big Idea

**break/continue = control over loops**
**Repetitive copy-paste = the pain that makes Functions (S8) feel like magic**

If students don't feel tired today, S8 won't land.
Teacher's job: make them tired. NOT help them shortcut.

---

## AI Policy

| Situation | Allowed? |
|---|---|
| W1, W2, Mini | No |
| 🔥 Project (5-Item Pain) | **ABSOLUTELY NOT** — kills the pedagogy |
| HW1, HW2 | No |
| HW3 Part A (5-Dish Pain) | NO — must feel the pain |
| HW3 Part B (Share) | Yes (just sending message) |

---

## Teacher Reminder

The PAIN is the LESSON. If a student finishes the project in 5 minutes with a function/list comprehension/AI — they missed the whole point.

When students complain "this is so repetitive!" — that is success, not failure.
