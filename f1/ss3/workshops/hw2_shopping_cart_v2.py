# =====================================================
# 🛒 HW2 — Shopping Cart V2 "Buy 3 Get 1" (⭐⭐⭐ Advanced)
# Python Foundation 1 · Session 3 · Math Operators
# =====================================================
# 🎯 GOAL: Calculate "buy 3, get 1 free" discount
#    Use // (floor division) to count free items
# ⏱️  TIME: 20 minutes at home
# 🔑 SKILL: // (floor division) for grouping
# =====================================================

print("🛒 Shopping V2 — Buy 3 Get 1 Free!")
print("=" * 38)


# 📝 TODO 1: Ask user how many items + price per item
quantity = int(input("How many items? "))
price    = float(input("Price per item (baht): "))


# 📝 TODO 2: Calculate FREE items
#    Every 3 items → 1 free
#    Use // floor division: quantity // 3
free_items = ___ // 3


# 📝 TODO 3: Calculate items to PAY for
#    pay_items = quantity − free_items
pay_items = quantity - ___


# 📝 TODO 4: Calculate total
total = pay_items * price


# ----- Print receipt -----
print()
print("=" * 38)
print("🧾 RECEIPT")
print("=" * 38)
print(f"You bought       : {quantity} items")
print(f"Free items       : {free_items} 🎁  (every 3 → 1 free)")
print(f"Pay for          : {pay_items} items")
print(f"Price each       : {price:.2f} baht")
print("-" * 38)
print(f"TOTAL            : {round(total, 2)} baht 💰")
print("=" * 38)


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# How many items? 10
# Price per item (baht): 50
#
# 🧾 RECEIPT
# ======================================
# You bought       : 10 items
# Free items       : 3 🎁  (every 3 → 1 free)
# Pay for          : 7 items
# Price each       : 50.00 baht
# --------------------------------------
# TOTAL            : 350.0 baht 💰
# ======================================
# =====================================================


# =====================================================
# 💡 KEY MATH (Why // works):
#   Buy 10 items → 10 // 3 = 3 free
#   Buy 12 items → 12 // 3 = 4 free
#   Buy  5 items → 5  // 3 = 1 free
#   Buy  2 items → 2  // 3 = 0 free
# =====================================================


# =====================================================
# 🎁 BONUS 1: Add VAT 7% on top
# =====================================================
# vat = total * 0.07
# total_with_vat = total + vat
# print(f"VAT 7%           : +{round(vat, 2)} baht")
# print(f"GRAND TOTAL      : {round(total_with_vat, 2)} baht")


# =====================================================
# 🎁 BONUS 2: Try different deals — change ONE number!
#    "Buy 5 Get 2": free_items = quantity // 5 * 2
#    "Buy 4 Get 1": free_items = quantity // 4
# =====================================================


# =====================================================
# 🎁 BONUS 3: Compare with normal price
#    no_discount = quantity * price
#    saved = no_discount - total
#    print(f"You saved        : {saved} baht!")
# =====================================================


# =====================================================
# 🔗 SUBMIT:
#   Share Trinket link OR screenshot → LINE group
#   Deadline: before next session
# =====================================================
