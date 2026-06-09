# =====================================================
# 🏖️ Project — Holiday Plan
# Python Foundation 2 · Session 1 · Lists Intro
# =====================================================
# 🎯 GOAL: Plan dream destinations using all list operations.
# ⏱️  TIME: 25 minutes
# 🔑 SKILL: Empty list + append + remove + in + len
# 🏠 SHARE: Talk with parents about real plans
# =====================================================

print("🏖️  Holiday Plan Builder")
print("=" * 35)


# 📝 TODO 1: Start with an empty list
destinations = []


# 📝 TODO 2: Loop ask 5 destinations + append
for i in range(1, 6):
    place = input(f"Destination #{i}: ")
    destinations.append(place)


# 📝 TODO 3: Print full list
print()
print("✈️  YOUR PLAN:")
for i, place in enumerate(destinations, start=1):
    print(f"  {i}. {place}")


# 📝 TODO 4: Ask for one to remove
print()
to_remove = input("Which one to remove? ")
if to_remove in destinations:
    destinations.remove(to_remove)
    print(f"❌ Removed: {to_remove}")
else:
    print(f"⚠️  '{to_remove}' is not in the plan")


# 📝 TODO 5: Check if a place is in plan
print()
to_check = input("Is anywhere in your plan? Type a place: ")
if to_check in destinations:
    print(f"✅ Yes — {to_check} is in your plan!")
else:
    print(f"❌ No — {to_check} is not planned.")


# 📝 TODO 6: Final summary
print()
print("=" * 35)
print(f"📋 Final plan ({len(destinations)} places):")
for place in destinations:
    print(f"  • {place}")


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# 🏖️  Holiday Plan Builder
# ===================================
# Destination #1: Phuket
# Destination #2: Chiang Mai
# Destination #3: Tokyo
# Destination #4: Paris
# Destination #5: Bali
#
# ✈️  YOUR PLAN:
#   1. Phuket
#   2. Chiang Mai
#   3. Tokyo
#   4. Paris
#   5. Bali
#
# Which one to remove? Bali
# ❌ Removed: Bali
#
# Is anywhere in your plan? Type a place: Tokyo
# ✅ Yes — Tokyo is in your plan!
#
# ===================================
# 📋 Final plan (4 places):
#   • Phuket
#   • Chiang Mai
#   • Tokyo
#   • Paris
# =====================================================


# =====================================================
# 🎁 BONUS 1: Don't allow duplicates
#   if place not in destinations: append
#   else: print "Already added!"
# =====================================================


# =====================================================
# 🎁 BONUS 2: Ask parent's wishlist too
#   Combine 2 lists with .extend()
# =====================================================
# parent_list = ["Hokkaido", "Switzerland"]
# destinations.extend(parent_list)
# print("Combined:", destinations)


# =====================================================
# 🔗 SHARE:
#   Trinket → send link to parents → discuss real plan!
# =====================================================
