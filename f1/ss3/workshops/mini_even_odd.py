# =====================================================
# 🎲 Mini — Even or Odd?
# Python Foundation 1 · Session 3 · Math Operators
# =====================================================
# 🎯 GOAL: Check if a number is even or odd using %.
# ⏱️  TIME: 10 minutes
# 🔑 SKILL: % (modulo) + (preview of if-else)
# =====================================================

# 📝 TODO 1: Ask user for a number
n = int(input("Pick any number: "))


# 📝 TODO 2: Use % 2 to check if it divides evenly
#    n % 2 == 0  means even
#    n % 2 == 1  means odd
remainder = n % 2


# 📝 TODO 3: Print the remainder for now
print(f"{n} % 2 = {remainder}")


# 📝 TODO 4: Check + print result (preview of if-else)
if remainder == 0:
    print(f"{n} is EVEN ✅")
else:
    print(f"{n} is ODD 🎲")


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# Pick any number: 7
# 7 % 2 = 1
# 7 is ODD 🎲
#
# Pick any number: 12
# 12 % 2 = 0
# 12 is EVEN ✅
# =====================================================


# =====================================================
# 💡 KEY IDEA:
#   Any number divided by 2 has remainder 0 or 1.
#   • Remainder 0 → it's a multiple of 2 → EVEN
#   • Remainder 1 → it's NOT a multiple of 2 → ODD
#
#   This trick works for ANY divisor:
#   • n % 3 == 0  →  divisible by 3
#   • n % 5 == 0  →  divisible by 5
# =====================================================


# =====================================================
# 🎁 BONUS 1: Multiple of 3?
# =====================================================
# if n % 3 == 0:
#     print(f"{n} is a multiple of 3!")


# =====================================================
# 🎁 BONUS 2: FizzBuzz preview!
#    Multiple of 3 → "Fizz"
#    Multiple of 5 → "Buzz"
#    Multiple of both → "FizzBuzz"
# =====================================================
# if n % 3 == 0 and n % 5 == 0:
#     print("FizzBuzz!")
# elif n % 3 == 0:
#     print("Fizz")
# elif n % 5 == 0:
#     print("Buzz")
# else:
#     print(n)
