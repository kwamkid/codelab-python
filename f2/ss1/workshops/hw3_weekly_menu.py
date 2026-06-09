# =====================================================
# 🍜 HW3 — Weekly Menu (⭐⭐⭐⭐⭐ Expert)
# Python Foundation 2 · Session 1 · Lists Intro
# =====================================================
# 🎯 Plan 7 days of dinner. Use len() + if to enforce 7 max.
# ⏱️  TIME: 25-30 minutes
# 🔑 SKILL: List + len + if + loop
# =====================================================

menu = []
MAX_MENUS = 7


print("🍜 Weekly Menu Planner (max 7 dinners)")
print("=" * 40)


# 📝 TODO 1: Loop ask user for menus
#    Try to add 8 (one will be rejected!)
for i in range(1, 9):
    food = input(f"Menu #{i}: ")

    # 📝 TODO 2: Check the limit BEFORE adding
    if len(menu) ___ MAX_MENUS:    # use < (less than)
        menu.append(food)
        print(f"  ✓ Added")
    else:
        print(f"  ❌ Full! Cannot add '{food}'.")


# 📝 TODO 3: Print final menu
print()
print("=" * 40)
print(f"📋 Final menu ({len(menu)} / {MAX_MENUS}):")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i, food in enumerate(menu):
    print(f"  {days[i]}: {food}")


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# 🍜 Weekly Menu Planner (max 7 dinners)
# ========================================
# Menu #1: Pad Thai
#   ✓ Added
# Menu #2: Tom Yum
#   ✓ Added
# Menu #3: Green Curry
#   ✓ Added
# ...
# Menu #7: Pizza
#   ✓ Added
# Menu #8: Sukiyaki
#   ❌ Full! Cannot add 'Sukiyaki'.
#
# ========================================
# 📋 Final menu (7 / 7):
#   Mon: Pad Thai
#   Tue: Tom Yum
#   Wed: Green Curry
#   ...
#   Sun: Pizza
# =====================================================


# =====================================================
# 🎁 BONUS 1: Don't allow duplicates
# =====================================================
# if food in menu:
#     print(f"  ⚠️  Already on menu!")
# elif len(menu) < MAX_MENUS:
#     menu.append(food)
# else:
#     print(f"  ❌ Full!")


# =====================================================
# 🎁 BONUS 2: Ask parents for 1-2 menus they want
#    Show them the final week!
# =====================================================


# =====================================================
# 🔗 SUBMIT:
#   Trinket link → LINE group
#   🏠 Show parents → use it for real meal planning!
# =====================================================
