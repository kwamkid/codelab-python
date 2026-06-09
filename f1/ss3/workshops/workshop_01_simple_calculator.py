# =====================================================
# 🧮 Workshop 1 — Simple Calculator
# Python Foundation 1 · Session 3 · Math Operators
# =====================================================
# 🎯 GOAL: Build a calculator that does + - * / on 2 numbers.
# ⏱️  TIME: 10 minutes
# 🔑 SKILL: 4 basic math operators
# =====================================================

print("🧮 Simple Calculator")
print("=" * 30)


# 📝 TODO 1: Ask user for 2 numbers (and cast to int!)
a = int(input("First number: "))
b = int(input("Second number: ___"))


# 📝 TODO 2: Print all 4 operations using f-string
print()
print(f"{a} + {b} = {___}")
print(f"{a} - {b} = {___}")
print(f"{a} * {b} = {___}")
print(f"{a} / {b} = {___}")


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# 🧮 Simple Calculator
# ==============================
# First number: 10
# Second number: 3
#
# 10 + 3 = 13
# 10 - 3 = 7
# 10 * 3 = 30
# 10 / 3 = 3.3333333333333335
# =====================================================


# =====================================================
# 🎁 BONUS 1: Add the 3 NEW operators
# =====================================================
# print(f"{a} // {b} = {a // b}")    # floor division
# print(f"{a} % {b} = {a % b}")      # remainder
# print(f"{a} ** {b} = {a ** b}")    # power


# =====================================================
# 🎁 BONUS 2: Round the division result
#    round(value, decimals)
# =====================================================
# result = a / b
# print(f"{a} / {b} = {round(result, 2)}")    # 2 decimals only


# =====================================================
# 🎁 BONUS 3: Ask user which operation they want
#    Use input("Which? + - * /: ") then if-else
#    (We'll learn if-else next session — but try!)
# =====================================================
