# =====================================================
# 🛒 Workshop 1 — 7-Eleven List
# Python Foundation 2 · Session 1 · Lists Intro
# =====================================================
# 🎯 GOAL: Build a shopping list using append + remove.
# ⏱️  TIME: 10 minutes
# 🔑 SKILL: List creation, append(), remove(), len()
# =====================================================

# 📝 TODO 1: Start with 3 items
shopping = ["___", "___", "___"]
print("Start  :", shopping)


# 📝 TODO 2: Append 2 more items
shopping.append("___")
shopping.append("___")
print("After +:", shopping)


# 📝 TODO 3: Remove 1 item
shopping.remove("___")
print("After -:", shopping)


# 📝 TODO 4: Print count
print("Total  :", len(shopping), "items")


# =====================================================
# 📋 EXPECTED OUTPUT (example):
# =====================================================
# Start  : ['Milk', 'Bread', 'Eggs']
# After +: ['Milk', 'Bread', 'Eggs', 'Snack', 'Juice']
# After -: ['Milk', 'Eggs', 'Snack', 'Juice']
# Total  : 4 items
# =====================================================


# =====================================================
# 🎁 BONUS 1: Use pop() to remove last
# =====================================================
# last = shopping.pop()
# print(f"Removed last: {last}")


# =====================================================
# 🎁 BONUS 2: Print each item with a number
# =====================================================
# for i, item in enumerate(shopping, start=1):
#     print(f"  {i}. {item}")
