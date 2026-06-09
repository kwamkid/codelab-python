# =====================================================
# 🔍 Workshop 1 — Type Checker
# Python Foundation 1 · Session 2 · Data Types & Casting
# =====================================================
# 🎯 GOAL: Use type() to check the data type of values.
# ⏱️  TIME: 10 minutes
# 🔑 SKILL: type() function · str / int / float
# =====================================================

# 📝 TODO: Use type() to print the type of each value
#    Hint: print(type(value))

# 1. A string
print(type("Hello"))     # Expected: <class 'str'>

# 2. A number (integer)
print(type(___))         # Try 42

# 3. A decimal (float)
print(type(___))         # Try 3.14

# 4. Tricky! What's this?
print(type("10"))        # Number in quotes — what type?

# 5. Add 1 more value of YOUR choice
print(type(___))


# =====================================================
# 📋 EXPECTED OUTPUT:
# =====================================================
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'str'>      ← "10" with quotes is STRING, not int!
# <class '...'>      ← your choice
# =====================================================


# =====================================================
# 🎁 BONUS 1: Check variables
# =====================================================
# name = "Alex"
# age = 10
# pi = 3.14159
#
# print(type(name))   # str
# print(type(age))    # int
# print(type(pi))     # float


# =====================================================
# 🎁 BONUS 2: Friendly message
#    Use f-string to make the output prettier
# =====================================================
# value = 42
# print(f"The value {value} is a {type(value).__name__}")
# # → "The value 42 is a int"


# =====================================================
# 💡 KEY POINT:
#   Quotes change EVERYTHING!
#   "42"  = string (just text that looks like a number)
#   42    = integer (a real number you can do math with)
# =====================================================
