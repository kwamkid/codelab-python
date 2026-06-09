# Workshops · F2 Session 6 — Survival Challenge

**Focus:** Review S1-5 · 3 Stages + 1 Boss Battle · NO ChatGPT

---

## Goal of this Session

Review 5 concepts from S1-S5 (lists, slicing, for, while, accumulator) through **mixed problems** — not topic by topic.

Everyone must finish "Boss Battle: Guess Master" → deploy on Trinket → share the link with someone special before leaving the room.

---

## Stage Files (in class)

| # | File | Description | Time |
|---|------|-------------|------|
| Stage 1 | [template_stage_01_playlist.py](template_stage_01_playlist.py) | Playlist Mayhem — list ops | 15 min |
| Stage 2 | [template_stage_02_loop_lab.py](template_stage_02_loop_lab.py) | Loop Lab — 5 missions | 15 min |
| Stage 3 | [template_stage_03_combo.py](template_stage_03_combo.py) | Combo Strike — list + loop | 15 min |
| BOSS | [boss_guess_master.py](boss_guess_master.py) | Guess Master — no template | 30 min |

---

## Homework (3 Tiers)

| Tier | File | For |
|---|---|---|
| HW1 (Required) | [hw1_finish_stage.py](hw1_finish_stage.py) | Everyone — finish the stage you missed |
| HW2 (Advanced) | [hw2_boss_v2_score.py](hw2_boss_v2_score.py) | Students who want a challenge |
| HW3 (Share with someone special) | [hw3_share_someone.md](hw3_share_someone.md) | Everyone — share Trinket link |

---

## Requirements

- **Python 3** (built-in `random` is enough)
- **Trinket account** (class account — teacher provides)
- **LINE app** (for HW3)

---

## Prerequisites — already know from S1-S5

- **S1-S2:** Lists — `append`, `remove`, `pop`, indexing, slicing, `in`, `len`
- **S3:** `for + range(start, stop, step)`, accumulator pattern
- **S4:** `for item in list`, `enumerate`, min/max/sum
- **S5:** `while loop`, `random.randint`, `random.choice`, for vs while

---

## Key Code Patterns (review)

```python
import random

# ── LIST OPERATIONS ──
playlist = ["song1", "song2", "song3"]
playlist.append("new_song")        # add to end
playlist.remove("song1")           # remove by value
top_5 = playlist[:5]               # slicing
exists = "song2" in playlist       # check membership

# ── FOR LOOP + ACCUMULATOR ──
total = 0
for score in [80, 75, 90, 85, 70]:
    total = total + score
average = total / 5

# ── WHILE LOOP + RANDOM ──
secret = random.randint(1, 100)
guess = 0
count = 0
while guess != secret:
    guess = int(input("Guess: "))
    count = count + 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print(f"You got it in {count} tries!")
```

---

## Big Idea

**Master these 5 basics = ready for Functions (S7-9)**

If you are not yet fluent — finish HW1 first. Do not rush into S7 (`break`, `continue`, `def`).

---

## AI Policy for this Session

| Situation | Allowed? |
|---|---|
| 3 Stages in class | No |
| Boss Battle (30 min) | NO (teacher walks around) |
| HW1 (Required) | No |
| HW2 (Advanced) | Maybe — only after trying yourself for 15 min |
| HW3 (Share) | Yes (focus is on sharing, not skill) |
