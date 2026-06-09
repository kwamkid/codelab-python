# =====================================================
# Stage 2 — Loop Lab
# Python Foundation 2 - Session 6 - Survival Challenge
# =====================================================
# GOAL: Pick the right loop (for vs while) for each context
# TIME: 15 minutes
# SKILL: for vs while, accumulator, while + condition
# =====================================================
# RULE: For each mission, add a comment explaining
#       "I chose for/while because ___"
# =====================================================

import random


# =====================================================
# MISSION 1: Print numbers 1 to 100
# =====================================================
# Do you know the count? __________
# Pick: for / while?
#
# Write your code:
for i in range(___, ___):    # <-- 1 to 100 (first 101)
    print(i)
# COMMENT: I chose for because ___________________


# =====================================================
# MISSION 2: Roll a dice until you get 6 (count tries)
# =====================================================
# Do you know the count? __________
# Pick: for / while?
#
# Write your code:
dice = 0
count = 0
while dice ___ 6:                # <-- roll until 6
    dice = random.___(1, 6)      # <-- random 1-6
    count = count + 1
    print(f"Try {count}: dice = {dice}")
print(f"Got 6 in {count} tries!")
# COMMENT: I chose while because ___________________


# =====================================================
# MISSION 3: Print odd numbers from 1 to 50
# =====================================================
# Do you know the count? __________
# Pick: for / while?
#
# Write your code:
for i in range(___, ___, ___):    # <-- 1, 51, 2 (step=2 = odd)
    print(i)
# COMMENT: I chose for because ___________________


# =====================================================
# MISSION 4: Ask for password until correct (password is "codelab")
# =====================================================
# Do you know the count? __________
# Pick: for / while?
#
# Write your code:
PASSWORD = "codelab"
input_text = ""
while input_text ___ PASSWORD:    # <-- ask until correct
    input_text = input("Password: ")
print("Access granted!")
# COMMENT: I chose while because ___________________


# =====================================================
# MISSION 5: Sum 5 test scores (accumulator)
# =====================================================
# Do you know the count? __________
# Pick: for / while?
#
# Write your code:
scores = [85, 72, 90, 68, 79]
total = ___                    # <-- start at 0
for score in ___:              # <-- loop scores
    total = total + ___        # <-- add score to total
average = total / len(scores)
print(f"Total: {total}, Average: {average}")
# COMMENT: I chose for because ___________________


# =====================================================
# EXPECTED OUTPUT (partial):
# =====================================================
# Mission 1: 1, 2, 3, ..., 100
# Mission 2: (random each run) e.g. "Got 6 in 4 tries!"
# Mission 3: 1, 3, 5, ..., 49
# Mission 4: ask until input is "codelab"
# Mission 5: Total 394, Average 78.8
# =====================================================


# =====================================================
# RULE TO REMEMBER
# =====================================================
# - for   = "repeat a known number of times"    -> range, list
# - while = "repeat until a condition changes"  -> condition
#
# Wrong pick = code still runs, but hard to read / verbose
# Right pick = short + clear code
# =====================================================
