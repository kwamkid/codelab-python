# =====================================================
# 📋 Workshop 1 — Roll Call
# Python Foundation 2 · Session 4 · Loops + Lists
# =====================================================
# 🎯 GOAL: Loop through a list of names → greet each one.
# ⏱️  TIME: 10 minutes
# 🔑 SKILL: for item in list
# =====================================================

# 📝 TODO 1: Create a list of 10 friend names
friends = [
    "Alex", "Bob", "Charlie", "Diana", "Eve",
    "___",  "___", "___",     "___",    "___",
]


# 📝 TODO 2: Loop through the list with for item in list
print("📋 Roll Call — Good morning class!")
print("=" * 35)

for friend in ___:
    print(f"Hi {___}! 👋")

print("=" * 35)
print(f"Total students: {len(friends)}")


# =====================================================
# 📋 EXPECTED OUTPUT:
# =====================================================
# 📋 Roll Call — Good morning class!
# ===================================
# Hi Alex! 👋
# Hi Bob! 👋
# Hi Charlie! 👋
# ... (10 lines total)
# ===================================
# Total students: 10
# =====================================================


# =====================================================
# 🎁 BONUS 1: Add the index
#    Use enumerate to print "1. Alex", "2. Bob", ...
# =====================================================
# for i, friend in enumerate(friends, start=1):
#     print(f"{i}. {friend}")


# =====================================================
# 🎁 BONUS 2: Custom messages per name
#    Use if-else to give VIP greeting to first friend
# =====================================================
# for friend in friends:
#     if friend == friends[0]:
#         print(f"⭐ Class president: {friend}!")
#     else:
#         print(f"Hi {friend}!")


# =====================================================
# 🎁 BONUS 3: Use the input()
#    Ask user for their name → if in list → "Welcome back!"
# =====================================================
