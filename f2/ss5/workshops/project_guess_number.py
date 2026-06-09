# =====================================================
# 🎯 Project — Guess the Number
# Python Foundation 2 · Session 5 · While Loops + random
# =====================================================
# 🎯 GOAL: Computer picks 1-100. Player guesses until correct.
#    Give "too high" / "too low" hints.
# ⏱️  TIME: 25 minutes
# 🔑 SKILL: while + random + if-elif
# 🏠 SHARE: Play with parents — challenge them!
# =====================================================

import random

print("🎯 Guess the Number!")
print("=" * 35)
print("I'm thinking of a number from 1 to 100...")
print()


# 📝 TODO 1: Computer picks a secret number
secret = random.___(1, 100)    # use randint


# 📝 TODO 2: Set up trackers
attempts = 0
guess = 0       # not the secret (so loop starts)


# 📝 TODO 3: Loop while guess is NOT secret
while guess != ___:

    # Ask user (cast to int!)
    guess = ___(input("Your guess: "))
    attempts = attempts + ___

    # Give hint
    if guess < secret:
        print("  📉 Too low!")
    elif guess > secret:
        print("  📈 Too high!")
    else:
        print("  ✅ Correct!")


# 📝 TODO 4: Final message
print()
print("=" * 35)
print(f"🎉 You got it in {attempts} attempts!")


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# 🎯 Guess the Number!
# ===================================
# I'm thinking of a number from 1 to 100...
#
# Your guess: 50
#   📈 Too high!
# Your guess: 25
#   📉 Too low!
# Your guess: 35
#   📉 Too low!
# Your guess: 42
#   ✅ Correct!
#
# ===================================
# 🎉 You got it in 4 attempts!
# =====================================================


# =====================================================
# 🎁 BONUS 1: Rate the performance
# =====================================================
# if attempts <= 5:
#     print("🏆 AMAZING!")
# elif attempts <= 10:
#     print("👍 Good job!")
# else:
#     print("💪 Keep practicing!")


# =====================================================
# 🎁 BONUS 2: Limit attempts (game over after 10)
# =====================================================
# attempts = 0
# while guess != secret and attempts < 10:
#     ...
# if attempts >= 10:
#     print(f"😅 Game over! It was {secret}.")


# =====================================================
# 🎁 BONUS 3: Range with difficulty
# =====================================================
# level = input("easy / medium / hard? ")
# if level == "easy":  max_num = 50
# elif level == "medium": max_num = 100
# else: max_num = 1000
# secret = random.randint(1, max_num)


# =====================================================
# 🔗 SHARE:
#   Trinket link → parents → challenge them!
#   Whoever guesses in fewest tries wins 🏆
# =====================================================
