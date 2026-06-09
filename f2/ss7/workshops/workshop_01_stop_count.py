# =====================================================
# W1 — Stop the Count
# Python Foundation 2 - Session 7 - Loop Control
# =====================================================
# GOAL: Understand break vs continue by SEEING the difference
# TIME: 15 minutes
# SKILL: break, continue, indentation
# =====================================================


# =====================================================
# TASK 1: Use BREAK to stop at 13
# =====================================================
# Count 1 to 20, but stop the moment you hit 13.
# Expected output: 1, 2, 3, ..., 12  (no 13, no more)

print("--- TASK 1: BREAK at 13 ---")
for i in range(1, ___):       # <-- 1 to 21 (so range includes 20)
    if i == ___:              # <-- 13
        ___                   # <-- break
    print(i)

print()


# =====================================================
# TASK 2: Use CONTINUE to skip 13
# =====================================================
# Count 1 to 20, but skip just the number 13.
# Expected output: 1, 2, ..., 12, 14, 15, ..., 20  (13 missing)

print("--- TASK 2: CONTINUE skips 13 ---")
for i in range(1, ___):       # <-- 1 to 21
    if i == ___:              # <-- 13
        ___                   # <-- continue
    print(i)

print()


# =====================================================
# TASK 3: BREAK on first number divisible by 7
# =====================================================
# Loop 1 to 50, stop at the first multiple of 7.
# Hint: use i % 7 == 0

print("--- TASK 3: BREAK at first multiple of 7 ---")
for i in range(1, ___):       # <-- 1 to 51
    if i % ___ == 0:          # <-- 7
        print(f"Found {i} — stopping!")
        ___                   # <-- break

print()


# =====================================================
# TASK 4: CONTINUE on every multiple of 3
# =====================================================
# Loop 1 to 20, but skip every multiple of 3.
# Expected: 1, 2, 4, 5, 7, 8, 10, 11, ...

print("--- TASK 4: CONTINUE on multiples of 3 ---")
for i in range(1, ___):       # <-- 1 to 21
    if i % ___ == 0:          # <-- 3
        ___                   # <-- continue
    print(i)


# =====================================================
# WRITE A COMMENT — in your own words
# =====================================================
# How would you explain the difference to a friend?
#
# break    = ___________________________________________
# continue = ___________________________________________


# =====================================================
# KEY IDEAS
# =====================================================
# - break    exits the loop NOW (no more rounds)
# - continue skips the REST of this round, goes to next i
# - Both must be INSIDE an if (otherwise loops break/skip every time)
# - Indentation matters: break/continue must be under the if
# =====================================================
