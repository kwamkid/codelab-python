# =====================================================
# 🔁 Workshop 2 — Same Problem, Two Ways
# Python Foundation 2 · Session 5 · While Loops + random
# =====================================================
# 🎯 GOAL: Count 1 to 10 with BOTH for and while.
#    Same output, different code — see the difference!
# ⏱️  TIME: 15 minutes
# 🔑 SKILL: Compare for vs while
# =====================================================

print("🔁 Version A: with FOR")
print("-" * 25)

# 📝 TODO 1: Use a for loop to print 1 to 10
#    Hint: range(1, 11)
for i in range(___, ___):
    print(f"  {i}")


print()
print("🔁 Version B: with WHILE")
print("-" * 25)

# 📝 TODO 2: Use a while loop to print 1 to 10
#    Hint: start i = 1, condition i <= 10, increment i inside
i = ___       # start value
while i <= ___:
    print(f"  {i}")
    i = ___ + 1   # don't forget to increment!


# =====================================================
# 📋 EXPECTED OUTPUT (both should be same!):
# =====================================================
# 🔁 Version A: with FOR
# -------------------------
#   1
#   2
#   3
#   ...
#   10
#
# 🔁 Version B: with WHILE
# -------------------------
#   1
#   2
#   3
#   ...
#   10
# =====================================================


# =====================================================
# 💡 WHICH IS BETTER HERE?
#   for is CLEANER for "count 1-10" — known count
#   while needs 3 things: start, check, increment
#   for has it all in 1 line: for i in range(1, 11)
# =====================================================


# =====================================================
# 🎁 BONUS 1: Count 10 → 1 (backwards) with BOTH
# =====================================================
# # for version:
# for i in range(10, 0, -1):
#     print(i)
#
# # while version:
# i = 10
# while i > 0:
#     print(i)
#     i = i - 1


# =====================================================
# 🎁 BONUS 2: Try a problem WHERE while is better
#   "Keep doubling 1 until it's > 1000"
# =====================================================
# n = 1
# while n <= 1000:
#     n = n * 2
#     print(n)
# # Output: 2, 4, 8, 16, ..., 1024
# # Try with for — you'd have to GUESS how many rounds!
