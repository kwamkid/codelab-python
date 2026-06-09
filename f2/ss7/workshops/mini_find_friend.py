# =====================================================
# Mini — Find Your Friend
# Python Foundation 2 - Session 7 - Loop Control
# =====================================================
# GOAL: Use break to stop searching once you find the target
# TIME: 15 minutes
# SKILL: enumerate + break + for-else
# =====================================================
# CONTEXT: You have a class list of 30 names.
#          Find a friend by name, print their position,
#          and STOP searching (don't waste time).
# =====================================================

# ── 30 student names ────────────────────────────────
class_list = [
    "Aim",   "Bar",   "Tang",  "Mai",   "Nut",
    "Ohm",   "Pim",   "Que",   "Run",   "Som",
    "Top",   "Una",   "Vee",   "Win",   "Xan",
    "Yim",   "Zee",   "Ann",   "Boss",  "Cam",
    "Dao",   "Eve",   "Faye",  "Gan",   "Hong",
    "Ice",   "Jib",   "Ken",   "Lala",  "Moo"
]


# =====================================================
# TASK 1: Ask user for a name to find
# =====================================================
target = input("Find a friend (type a name): ")


# =====================================================
# TASK 2: Search with for + enumerate + break
# =====================================================
# Hint: enumerate gives (index, value)
#       break the moment you find it

found = False
for i, name in enumerate(class_list):
    if name == ___:                       # <-- target
        print(f"Found '{name}' at position {i + 1} of {len(class_list)}")
        found = ___                       # <-- True
        ___                               # <-- break

if not found:
    print(f"'{target}' is not in the class list")


# =====================================================
# TASK 3 (BONUS): for-else pattern
# =====================================================
# Python has a special 'else' that runs only if the loop
# completes WITHOUT a break. Try this version:

print("\n--- Bonus: for-else version ---")
target2 = input("Find another friend: ")

for i, name in enumerate(class_list):
    if name == target2:
        print(f"Found '{name}' at position {i + 1}")
        break
___:                                       # <-- else
    # This runs only if break did NOT happen
    print(f"'{target2}' is not in the class list")


# =====================================================
# EXPECTED OUTPUT (example):
# =====================================================
# Find a friend (type a name): Tang
# Found 'Tang' at position 3 of 30
#
# --- Bonus: for-else version ---
# Find another friend: Ohm
# Found 'Ohm' at position 6
# =====================================================


# =====================================================
# WHY BREAK?
# =====================================================
# Without break:
#   - Loop continues even after finding the match
#   - With 30 names, you waste up to 29 extra checks
#   - With 1 million names, you waste 999,999 checks
#
# With break:
#   - Stop as soon as you find it
#   - This is the foundation of "linear search" algorithm
# =====================================================
