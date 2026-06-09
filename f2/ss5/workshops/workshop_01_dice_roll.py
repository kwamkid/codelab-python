# =====================================================
# 🎲 Workshop 1 — Roll Until Six
# Python Foundation 2 · Session 5 · While Loops + random
# =====================================================
# 🎯 GOAL: Use while + random to roll a dice until you get 6.
# ⏱️  TIME: 10 minutes
# 🔑 SKILL: while loop, random.randint
# =====================================================

import random

# 📝 TODO 1: Set up trackers BEFORE the loop
dice  = ___   # any number that's NOT 6 (try 0)
count = 0


# 📝 TODO 2: while dice is NOT 6
#    Hint: use != (not equal)
while dice ___ 6:

    # 📝 TODO 3: Roll a new dice (1-6)
    dice = random.___(1, 6)

    # 📝 TODO 4: Increment count
    count = ___ + 1

    # Print this round
    print(f"Roll {count}: 🎲 = {dice}")


# 📝 TODO 5: Final message AFTER the loop
print(f"🎉 Got 6 after {count} rolls!")


# =====================================================
# 📋 EXAMPLE OUTPUT (different every run!):
# =====================================================
# Roll 1: 🎲 = 3
# Roll 2: 🎲 = 1
# Roll 3: 🎲 = 5
# Roll 4: 🎲 = 6
# 🎉 Got 6 after 4 rolls!
# =====================================================


# =====================================================
# 🎁 BONUS 1: Roll until you get TWO 6s in a row
# =====================================================
# count_sixes = 0
# while count_sixes < 2:
#     dice = random.randint(1, 6)
#     if dice == 6:
#         count_sixes += 1
#     else:
#         count_sixes = 0   # reset!


# =====================================================
# 🎁 BONUS 2: Play 10 games — count average rolls
# =====================================================
# total_rolls = 0
# for game in range(10):
#     dice = 0
#     rolls = 0
#     while dice != 6:
#         dice = random.randint(1, 6)
#         rolls += 1
#     total_rolls += rolls
# print(f"Average: {total_rolls / 10} rolls per game")


# =====================================================
# 💡 KEY IDEAS:
# • while runs until the condition is FALSE
# • Something inside the loop MUST change the condition
# • If it doesn't → infinite loop 💥 (program freezes!)
# =====================================================
