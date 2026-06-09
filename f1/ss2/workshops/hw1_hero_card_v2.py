# =====================================================
# 🦸 HW1 — Hero Card V2 (⭐⭐ Required)
# Python Foundation 1 · Session 2 · Data Types & Casting
# =====================================================
# 🎯 GOAL: Upgrade your Session 1 Hero Card!
#    Now ASK the user to fill in the hero details.
# ⏱️  TIME: 20 minutes at home
# 🔑 SKILL: input() + int() + f-string
# =====================================================

print("╔═══════════════════════════════════╗")
print("║      🦸 HERO CARD CREATOR 🦸      ║")
print("╚═══════════════════════════════════╝")
print()


# 📝 TODO 1: Ask user for hero details
hero_name = input("Hero name: ")
real_name = input("Real name: ")
power     = input("Super power: ")
weakness  = input("Weakness: ")
quote     = input("Hero quote: ")


# 📝 TODO 2: Ask for age (need to cast to int!)
age_text = input("Age: ")
age = int(age_text)   # convert string to int


# ----- Print the Hero Card -----
print()
print("╔═══════════════════════════════════╗")
print("║         🦸 HERO CARD 🦸          ║")
print("╠═══════════════════════════════════╣")
print(f"║ Hero Name : {hero_name}")
print(f"║ Real Name : {real_name}")
print(f"║ Age       : {age}")
print(f"║ Power     : {power}")
print(f"║ Weakness  : {weakness}")
print("╠═══════════════════════════════════╣")
print(f'║ "{quote}"')
print("╚═══════════════════════════════════╝")


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# Hero name: Lightning Girl
# Real name: Alex
# Super power: super speed
# Weakness: sleepy mornings
# Hero quote: I can do it!
# Age: 10
#
# ╔═══════════════════════════════════╗
# ║         🦸 HERO CARD 🦸          ║
# ╠═══════════════════════════════════╣
# ║ Hero Name : Lightning Girl
# ║ Real Name : Alex
# ║ Age       : 10
# ║ Power     : super speed
# ║ Weakness  : sleepy mornings
# ╠═══════════════════════════════════╣
# ║ "I can do it!"
# ╚═══════════════════════════════════╝
# =====================================================


# =====================================================
# 🎁 BONUS 1: Calculate birth year (พ.ศ.)
# =====================================================
# THIS_YEAR = 2568
# birth_year = THIS_YEAR - age
# print(f"║ Born in   : พ.ศ. {birth_year}")


# =====================================================
# 🎁 BONUS 2: Use lower() to print quote in lowercase too
# =====================================================
# print(f'║ Lowercase : "{quote.lower()}"')


# =====================================================
# 🎁 BONUS 3: Make a TEAM of heroes
#    Run input() 3 times for 3 different heroes!
# =====================================================


# =====================================================
# 🔗 SUBMIT:
#   Share on Trinket.io → let parents fill in their hero!
#   Send Trinket link OR screenshot → LINE group
#   Deadline: before next session
# =====================================================
