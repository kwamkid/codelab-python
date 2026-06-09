# =====================================================
# 🎂 Mini — Next Year
# Python Foundation 1 · Session 2 · Data Types & Casting
# =====================================================
# 🎯 GOAL: Ask user's age → tell them their age next year.
# ⏱️  TIME: 10 minutes
# 🔑 SKILL: int() casting
# =====================================================

# 📝 TODO 1: Ask the user for their age (as text first)
age_text = input("How old are you? ")


# 📝 TODO 2: Convert (cast) the text to an integer
#    Hint: int(age_text)
age = int(___)


# 📝 TODO 3: Calculate next year's age
next_age = ___ + 1


# 📝 TODO 4: Print the result with f-string
print(f"Next year, you'll be ___ years old! 🎂")


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# How old are you? 10
# Next year, you'll be 11 years old! 🎂
# =====================================================


# =====================================================
# ❌ COMMON MISTAKE:
#   Don't try to add 1 to age_text directly!
#   "10" + 1  →  Error 💥 (can't add string + int)
#   int("10") + 1  →  11 ✅
# =====================================================


# =====================================================
# 🎁 BONUS 1: Print 5 future ages (with for loop concept)
# =====================================================
# print(f"In 1 year:  {age + 1}")
# print(f"In 2 years: {age + 2}")
# print(f"In 5 years: {age + 5}")
# print(f"In 10 years: {age + 10}")


# =====================================================
# 🎁 BONUS 2: Calculate birth year from age (พ.ศ.)
# =====================================================
# this_year = 2568
# birth_year = this_year - age
# print(f"You were born in พ.ศ. {birth_year}")
# =====================================================
