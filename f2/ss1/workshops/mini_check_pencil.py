# =====================================================
# 🔍 Mini — Check Pencil
# Python Foundation 2 · Session 1 · Lists Intro
# =====================================================
# 🎯 GOAL: Use `in` to check if an item is in a list.
# ⏱️  TIME: 10 minutes
# =====================================================

bag = ["📕 Book", "✏️ Pencil", "📐 Ruler", "🖊️ Pen"]

print("🎒 Bag contents:", bag)
print()


# 📝 TODO 1: Ask user what to look for
item = input("What do you want to check? ")


# 📝 TODO 2: Use if-in to check
if item ___ bag:
    print(f"✅ Yes! {item} is in the bag.")
else:
    print(f"❌ No, you forgot {item}!")


# 📝 TODO 3: Print bag size
print(f"\nTotal items: ___(bag)")   # use len()


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# 🎒 Bag contents: ['📕 Book', '✏️ Pencil', '📐 Ruler', '🖊️ Pen']
#
# What do you want to check? ✏️ Pencil
# ✅ Yes! ✏️ Pencil is in the bag.
#
# Total items: 4
# =====================================================


# =====================================================
# 🎁 BONUS 1: Check multiple items in a row
#   while True: ... (we'll learn while loops in S5)
# =====================================================


# =====================================================
# 🎁 BONUS 2: Check what's MISSING
#    needed = ["Book", "Pencil", "Eraser", "Calculator"]
#    for item in needed:
#        if item not in bag:
#            print(f"⚠️ Forgot: {item}")
# =====================================================
