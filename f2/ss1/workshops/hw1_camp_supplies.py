# =====================================================
# 🏕️ HW1 — Camp Supplies (⭐⭐ Required)
# Python Foundation 2 · Session 1 · Lists Intro
# =====================================================
# 🎯 Pack for 5-day camp! Append 10 items, then remove 3.
# ⏱️  TIME: 20 minutes
# =====================================================

camp_bag = []


# 📝 TODO 1: Append 10 items one by one
camp_bag.append("___")
camp_bag.append("___")
camp_bag.append("___")
camp_bag.append("___")
camp_bag.append("___")
camp_bag.append("___")
camp_bag.append("___")
camp_bag.append("___")
camp_bag.append("___")
camp_bag.append("___")

print("📦 Packed all 10 items:")
print(camp_bag)
print(f"Total: {len(camp_bag)}")


# 📝 TODO 2: Remove 3 things you don't need
camp_bag.remove("___")
camp_bag.remove("___")
camp_bag.remove("___")

print()
print("🎒 After cleanup:")
print(camp_bag)
print(f"Total: {len(camp_bag)}")


# =====================================================
# 📋 EXAMPLE OUTPUT:
# =====================================================
# 📦 Packed all 10 items:
# ['tent', 'sleeping bag', 'flashlight', 'food', 'water',
#  'map', 'jacket', 'phone', 'book', 'snacks']
# Total: 10
#
# 🎒 After cleanup:
# ['tent', 'sleeping bag', 'flashlight', 'food', 'water',
#  'map', 'jacket']
# Total: 7
# =====================================================


# =====================================================
# 🎁 BONUS 1: Use a loop to ask user for inputs
# =====================================================
# camp_bag = []
# for i in range(1, 11):
#     item = input(f"Item #{i}: ")
#     camp_bag.append(item)


# =====================================================
# 🎁 BONUS 2: Don't allow duplicates
# =====================================================
# for i in range(1, 11):
#     item = input(f"Item #{i}: ")
#     if item in camp_bag:
#         print("Already packed!")
#     else:
#         camp_bag.append(item)


# =====================================================
# 🔗 SUBMIT:
#   Trinket link OR screenshot → LINE group
# =====================================================
