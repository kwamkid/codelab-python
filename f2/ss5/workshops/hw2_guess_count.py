# =====================================================
# 🎯 HW2 — Guess + Count (⭐⭐⭐ Advanced)
# Python Foundation 2 · Session 5 · While Loops + random
# =====================================================
# 🎯 Like the project — but RATE the player:
#    ≤ 5 attempts → "🎉 Amazing!"
#    else        → "Good try!"
# ⏱️  TIME: 20 minutes
# 🔑 SKILL: while + random + if-elif + counting
# =====================================================

import random

print("🎯 Guess the Number — Pro version")
print("=" * 38)
print("I'm thinking of a number 1-100...")
print()


# 📝 TODO 1: Pick secret, setup counters
secret = random.randint(___, ___)
attempts = ___
guess = -1   # any value not in 1-100


# 📝 TODO 2: while guess != secret
while guess != ___:

    guess = int(input("Your guess: "))
    attempts = ___ + 1

    if guess < secret:
        print("  📉 Too low!")
    elif guess > secret:
        print("  📈 Too high!")
    else:
        print("  ✅ Correct!")


# 📝 TODO 3: Rate the performance
print()
print("=" * 38)
print(f"You finished in {attempts} attempts!")

if attempts <= ___:
    print("🎉 Amazing — you're a mind reader!")
elif attempts <= ___:
    print("👍 Good try!")
else:
    print("💪 Keep practicing!")


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# 🎯 Guess the Number — Pro version
# ======================================
# I'm thinking of a number 1-100...
#
# Your guess: 50  → 📈 Too high!
# Your guess: 25  → 📉 Too low!
# Your guess: 40  → 📉 Too low!
# Your guess: 42  → ✅ Correct!
#
# ======================================
# You finished in 4 attempts!
# 🎉 Amazing — you're a mind reader!
# =====================================================


# =====================================================
# 🎁 BONUS 1: Give up after 10 attempts
# =====================================================
# while guess != secret and attempts < 10:
#     ...
# if attempts >= 10 and guess != secret:
#     print(f"😅 The number was {secret}.")


# =====================================================
# 🎁 BONUS 2: Best of 3 rounds
# =====================================================
# total_attempts = 0
# for round_num in range(1, 4):
#     # play one game
#     total_attempts += attempts
# average = total_attempts / 3
# print(f"📊 Average: {average} attempts per game")


# =====================================================
# 🔗 SUBMIT:
#   Trinket link OR screenshot → LINE group
#   🏠 Challenge parents — who scores lower?
# =====================================================
