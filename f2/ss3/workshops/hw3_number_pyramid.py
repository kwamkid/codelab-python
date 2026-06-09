# =====================================================
# 🔺 HW3 — Number Pyramid (⭐⭐⭐⭐⭐ Expert)
# Python Foundation 2 · Session 3 · For Loops Deep
# =====================================================
# 🎯 GOAL:
#   Build a NUMBER PYRAMID using NESTED FOR LOOPS
#   (a for loop inside another for loop).
#
# 🔑 KEY SKILL: nested loops
#   - Outer loop  = rows (how many lines to print)
#   - Inner loop  = numbers on each line
#
# 🏠 SHARE: Show this to your parents when done!
#
# ⏱️  TIME: 30-40 minutes at home
# =====================================================

# Configuration
rows = 5   # try changing to 7 or 10 later!

# 📝 TODO 1: Outer loop — each row from 1 to rows
#    Hint: range(1, rows + 1) gives 1, 2, 3, 4, 5 when rows=5
for i in range(1, rows + 1):

    # 📝 TODO 2: Inner loop — print numbers 1 to i on this row
    #    Example: row 3 should print "1 2 3"
    #    Hint: range(1, ___)  — what should stop be?
    for j in range(___, ___):
        print(j, end=" ")   # end=" " means DON'T go to next line — use space

    # 📝 TODO 3: After inner loop finishes, go to next line
    #    Hint: print() with no arguments prints a newline
    print()


# =====================================================
# 📋 EXPECTED OUTPUT (when rows=5):
# =====================================================
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# =====================================================


# =====================================================
# 🎁 BONUS 1: Inverted Pyramid (5 rows → 1 row)
# =====================================================
# for i in range(rows, 0, -1):           # <-- reverse!
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
#
# Expected:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1


# =====================================================
# 🎁 BONUS 2: Centered Pyramid (add spaces on the left)
# =====================================================
# for i in range(1, rows + 1):
#     print("  " * (rows - i), end="")   # leading spaces
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
#
# Expected:
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5


# =====================================================
# 🎁 BONUS 3: Let the user pick the height
# =====================================================
# rows = int(input("How many rows? "))
# (then run the same pyramid code)


# =====================================================
# 📸 SUBMIT:
#   Screenshot your code + output → send to LINE group
#   Deadline: before next session
#   BONUS POINTS: record a short video showing it to
#                 your parents & their reaction! 🎬
# =====================================================
