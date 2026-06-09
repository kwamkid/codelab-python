# =====================================================
# ❓ HW1 — Capital Quiz (⭐⭐ Required)
# Python Foundation 2 · Session 5 · While Loops + random
# =====================================================
# 🎯 Ask "What's the capital of Thailand?" → keep asking
#    until the user types "Bangkok".
# ⏱️  TIME: 15 minutes
# 🔑 SKILL: while + string comparison
# =====================================================

print("🏛️  Quick Quiz!")
print("=" * 30)

answer = ""    # start empty so loop runs


# 📝 TODO 1: while answer is NOT "Bangkok"
while answer != "___":

    # Ask the user
    answer = input("What's the capital of Thailand? ")

    # Give feedback
    if answer == "Bangkok":
        print("✅ Correct! 🎉")
    else:
        print("❌ Try again!")


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# 🏛️  Quick Quiz!
# ==============================
# What's the capital of Thailand? Phuket
# ❌ Try again!
# What's the capital of Thailand? Chiang Mai
# ❌ Try again!
# What's the capital of Thailand? Bangkok
# ✅ Correct! 🎉
# =====================================================


# =====================================================
# 🎁 BONUS 1: Accept lowercase/uppercase variations
#    "BANGKOK", "bangkok", "Bangkok" → all OK
# =====================================================
# while answer.lower() != "bangkok":
#     answer = input("What's the capital? ")
#     ...


# =====================================================
# 🎁 BONUS 2: Count attempts → give hint after 3 tries
# =====================================================
# attempts = 0
# while answer.lower() != "bangkok":
#     answer = input("Capital? ")
#     attempts += 1
#     if attempts == 3:
#         print("💡 Hint: starts with B!")
# print(f"Got it in {attempts} tries.")


# =====================================================
# 🎁 BONUS 3: Make it 3 questions!
# =====================================================
# questions = [
#     ("Capital of Thailand?", "Bangkok"),
#     ("Capital of Japan?", "Tokyo"),
#     ("Capital of France?", "Paris"),
# ]
# for q, correct in questions:
#     ans = ""
#     while ans.lower() != correct.lower():
#         ans = input(q + " ")
#     print("✅ Correct!")


# =====================================================
# 🔗 SUBMIT:
#   Trinket link OR screenshot → LINE group
# =====================================================
