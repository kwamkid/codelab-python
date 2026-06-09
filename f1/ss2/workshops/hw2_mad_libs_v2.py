# =====================================================
# 🎭 HW2 — Mad Libs V2 (⭐⭐⭐ Advanced)
# Python Foundation 1 · Session 2 · Data Types & Casting
# =====================================================
# 🎯 GOAL: Upgrade Mad Libs — ASK the user for words.
#    Mix STRING and INT inputs to make a silly story.
# ⏱️  TIME: 20-25 minutes at home
# 🔑 SKILL: input() + int() + f-string
# 🏠 SHARE: Have parents play it!
# =====================================================

print("=" * 45)
print("📖 MAD LIBS — Story Generator")
print("=" * 45)
print()
print("Fill in these blanks (don't peek at the story!):")
print()


# 📝 TODO 1: Ask for STRING inputs (text)
hero_name = input("A hero name: ")
place     = input("A place (e.g. forest, mall): ")
animal    = input("An animal: ")
food      = input("A food: ")
shout     = input("A short word to shout: ")


# 📝 TODO 2: Ask for INT inputs (numbers — need int() casting!)
age_text     = input("A small number (1-20): ")
age          = int(age_text)

count_text   = input("Another number (3-100): ")
count        = int(count_text)


# ----- Print the silly story -----
print()
print("=" * 45)
print("📖 YOUR SILLY STORY")
print("=" * 45)
print()
print(f"Once upon a time, {hero_name} (age {age})")
print(f"went to {place}")
print(f"and saw {count} dancing {animal}s.")
print(f'"{shout}!" shouted {hero_name}.')
print(f"They all ate {food} together for {age + count} hours.")
print(f"And lived happily ever after. 🎬")
print()
print("=" * 45)


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# A hero name: Alex
# A place (e.g. forest, mall): jungle
# An animal: banana
# A food: pizza
# A short word to shout: Wow
# A small number (1-20): 10
# Another number (3-100): 7
#
# 📖 YOUR SILLY STORY
# Once upon a time, Alex (age 10)
# went to jungle
# and saw 7 dancing bananas.
# "Wow!" shouted Alex.
# They all ate pizza together for 17 hours.
# And lived happily ever after. 🎬
# =====================================================


# =====================================================
# 💡 KEY POINTS:
#   • String inputs (name, place, food) — no casting needed
#   • Number inputs — wrap with int() to do math!
#   • age + count = math (10 + 7 = 17) ← only works with int!
# =====================================================


# =====================================================
# 🎁 BONUS 1: Add MORE silly inputs
# =====================================================
# adjective = input("A funny adjective (e.g. squishy): ")
# print(f"The {adjective} {animal} winked at {hero_name}!")


# =====================================================
# 🎁 BONUS 2: Make 2 different stories
#    Run the file twice with different inputs!
#    Or copy the print block and write a 2nd story
# =====================================================


# =====================================================
# 🎁 BONUS 3: Use str() to convert numbers back to text
# =====================================================
# total_hours = age + count
# message = "Total time: " + str(total_hours) + " hours"
# print(message)


# =====================================================
# 🔗 SUBMIT:
#   Share on Trinket → let friends/parents play with it!
#   Send Trinket link OR screenshot → LINE group
#   🎬 Bonus points: record parent's reaction!
# =====================================================
