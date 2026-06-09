# =====================================================
# 👥 HW1 — Classroom Roll Call (⭐⭐ Required)
# Python Foundation 2 · Session 3 · For Loops Deep
# =====================================================
# 🎯 GOAL:
#   Print 30 students with their IDs using a for loop.
#   Use range(1, 31) to count from 1 to 30.
#
# ⏱️  TIME: 20-30 minutes at home
# =====================================================

# Option A: Using simple placeholder names
# (Replace "Student" with real classmate names if you want!)

# 📝 TODO 1: Create a for loop from 1 to 30
#    Hint: range(1, 31)  -- remember stop is EXCLUSIVE!
for i in range(___, ___):

    # 📝 TODO 2: Print "Student #X: Name"
    #    Use f-string: f"Student #{i}: ..."
    print(___)


# =====================================================
# 📋 EXPECTED OUTPUT:
# =====================================================
# Student #1: Alice
# Student #2: Bob
# Student #3: Charlie
# Student #4: Diana
# ...
# Student #30: Emma
# =====================================================


# =====================================================
# 🎁 BONUS 1: Use a real list of classmate names
# =====================================================
# classmates = ["Alice", "Bob", "Charlie", "Diana", ...]  # 30 names
#
# for i in range(1, 31):
#     name = classmates[i - 1]   # list is 0-indexed, so -1
#     print(f"Student #{i}: {name}")


# =====================================================
# 🎁 BONUS 2: Group them by 5 (Group A = 1-5, Group B = 6-10, ...)
# =====================================================
# for i in range(1, 31):
#     print(f"Student #{i}: Name")
#     if i % 5 == 0:
#         print(f"   ↑ End of Group {chr(64 + i//5)}")   # A, B, C, D, E, F
#         print()


# =====================================================
# 📸 SUBMIT:
#   Screenshot your code + output → send to LINE group
#   Deadline: before next session
# =====================================================
