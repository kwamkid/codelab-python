# =====================================================
# 🗓️ Project — Age Calculator (พ.ศ.)
# Python Foundation 1 · Session 2 · Data Types & Casting
# =====================================================
# 🎯 GOAL: Calculate age from Buddhist year (พ.ศ.) of birth.
# ⏱️  TIME: 25 minutes
# 🔑 SKILL: input() + int() + math
# 🔗 SHARE: Send Trinket link to parents → they try it!
# =====================================================

# Current Buddhist year
THIS_YEAR_BE = 2568

print("=" * 40)
print("🗓️  AGE CALCULATOR (Thai Buddhist Year)")
print("=" * 40)
print()


# 📝 TODO 1: Ask user for their birth year (พ.ศ.)
birth_year_text = input("In which year (พ.ศ.) were you born? ")


# 📝 TODO 2: Convert string to integer
birth_year = int(___)


# 📝 TODO 3: Calculate age
age = ___ - birth_year


# 📝 TODO 4: Print result with f-string
print()
print(f"🎂 You are {___} years old in พ.ศ. {THIS_YEAR_BE}")


# 📝 TODO 5 (Bonus): Calculate age next year
next_age = age + 1
print(f"🎉 Next year you'll be {next_age} years old!")


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# ========================================
# 🗓️  AGE CALCULATOR (Thai Buddhist Year)
# ========================================
#
# In which year (พ.ศ.) were you born? 2558
#
# 🎂 You are 10 years old in พ.ศ. 2568
# 🎉 Next year you'll be 11 years old!
# =====================================================


# =====================================================
# 💡 KEY CONCEPTS:
#   • input() returns text (string)
#   • int() converts text to a number
#   • Math: 2568 - 2558 = 10  (your age!)
# =====================================================


# =====================================================
# 🎁 BONUS CHALLENGES (try one!):
# =====================================================
#
# 🎁 1. Convert พ.ศ. → ค.ศ. (Christian year)
#       ค.ศ. = พ.ศ. - 543
#       christian_year = birth_year - 543
#       print(f"In English calendar: {christian_year}")
#
# 🎁 2. How many days old are you?
#       days = age * 365
#       print(f"You're about {days:,} days old!")
#
# 🎁 3. Calculate parent's age too
#       parent_birth = int(input("Parent's birth year (พ.ศ.)? "))
#       parent_age = THIS_YEAR_BE - parent_birth
#       print(f"Your parent is {parent_age} years old.")
#       print(f"Age difference: {parent_age - age} years.")
# =====================================================


# =====================================================
# 🔗 SHARE ON TRINKET.IO:
#   1. Copy ALL this code
#   2. Go to trinket.io → New Python Trinket
#   3. Paste → Run → Click Share
#   4. Send link to parents — they try it on their phone!
# =====================================================
