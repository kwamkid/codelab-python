# =====================================================
# Stage 3 — Combo Strike
# Python Foundation 2 - Session 6 - Survival Challenge
# =====================================================
# GOAL: Combine list + loop + accumulator in one problem
# TIME: 15 minutes
# SKILL: list iteration, accumulator, min/max, slicing
# =====================================================
# Context: You are a teacher with 10 students' exam scores.
#          Must summarize the results before lunch break!
# =====================================================

# SETUP: exam scores of 10 students (do not edit)
scores = [85, 72, 90, 68, 79, 95, 55, 88, 73, 60]
names  = ["Peem", "Beau", "Faye", "Kong", "Min",
          "Prim", "Ohm", "Nut", "Ying", "Boss"]

print("--- All Scores ---")
for i in range(len(scores)):
    print(f"  {names[i]:6} -> {scores[i]}")
print()


# =====================================================
# TASK 1: Calculate the average (accumulator pattern)
# =====================================================
# Hint: total = 0 -> loop and add -> divide by len(scores)
total = ___                    # <-- start at 0
for score in ___:              # <-- loop scores
    total = ___                # <-- total + score
average = total / len(scores)
print(f"Average: {average:.1f}")


# =====================================================
# TASK 2: Find the highest score + name (tracker pattern)
# =====================================================
# Hint: use 2 variables — max_score + max_name
#       loop and compare
max_score = ___                # <-- start at 0 (or scores[0])
max_name = ""
for i in range(len(scores)):
    if scores[i] ___ max_score:    # <-- compare > max_score
        max_score = scores[i]
        max_name = names[i]
print(f"Highest score: {max_name} = {max_score}")


# =====================================================
# TASK 3: Print Top 3 scores (sorted + slicing)
# =====================================================
# Hint: sorted(scores, reverse=True) -> [:3]
# (no names linked, to keep stage simple)
top_3 = sorted(scores, reverse=___)[___]    # <-- reverse=True, [:3]
print(f"Top 3 scores: {top_3}")


# =====================================================
# TASK 4: Count students BELOW the average
# =====================================================
# Hint: count = 0 -> loop -> if score < average -> count + 1
count_below = ___                  # <-- start at 0
for score in scores:
    if score ___ average:          # <-- < average
        count_below = count_below + ___    # <-- + 1
print(f"{count_below} students scored below average")


# =====================================================
# EXPECTED OUTPUT:
# =====================================================
# --- All Scores ---
#   Peem   -> 85
#   Beau   -> 72
#   ... (10 students)
#
# Average: 76.5
# Highest score: Prim = 95
# Top 3 scores: [95, 90, 88]
# 5 students scored below average
# =====================================================


# =====================================================
# 4 PATTERNS USED IN THIS STAGE
# =====================================================
# 1. ACCUMULATOR    total = 0 -> total = total + x
# 2. TRACKER        max_val = 0 -> if x > max_val: max_val = x
# 3. SORT + SLICE   sorted(list)[:n]
# 4. COUNTER        count = 0 -> if condition: count += 1
#
# Combine these 4 patterns = you can do basic data analysis!
# =====================================================
