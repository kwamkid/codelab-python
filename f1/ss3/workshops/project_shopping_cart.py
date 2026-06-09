# =====================================================
# 🛒 Project — Shopping Cart
# Python Foundation 1 · Session 3 · Math Operators
# =====================================================
# 🎯 GOAL: Build a real shopping calculator!
#    Quantity × Price → discount 10% → VAT 7% → total
# ⏱️  TIME: 25 minutes
# 🔑 SKILL: Math + PEMDAS + round()
# 🔗 SHARE: Trinket → parents try with their own items!
# =====================================================

print("🛒 Shopping Cart Calculator")
print("=" * 35)


# 📝 TODO 1: Get item details from user
item     = input("What are you buying? ")
quantity = int(input("How many? "))
price    = float(input("Price per item (baht): "))


# 📝 TODO 2: Calculate subtotal
#    subtotal = quantity × price
subtotal = ___ * ___


# 📝 TODO 3: Calculate discount (10% off)
#    discount = subtotal × 0.10
discount = ___ * 0.10


# 📝 TODO 4: Calculate VAT (7% on the discounted amount)
#    after_discount = subtotal - discount
#    vat = after_discount × 0.07
after_discount = subtotal - discount
vat = ___ * 0.07


# 📝 TODO 5: Calculate final total
total = after_discount + vat


# ----- Print the receipt -----
print()
print("=" * 35)
print("🧾 RECEIPT")
print("=" * 35)
print(f"Item       : {item}")
print(f"Quantity   : {quantity}")
print(f"Price each : {price:.2f} baht")
print("-" * 35)
print(f"Subtotal   : {round(subtotal, 2)} baht")
print(f"Discount   : -{round(discount, 2)} baht (10%)")
print(f"VAT        : +{round(vat, 2)} baht (7%)")
print("=" * 35)
print(f"TOTAL      : {round(total, 2)} baht 💰")
print("=" * 35)


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# What are you buying? Notebook
# How many? 5
# Price per item (baht): 80
#
# 🧾 RECEIPT
# ===================================
# Item       : Notebook
# Quantity   : 5
# Price each : 80.00 baht
# -----------------------------------
# Subtotal   : 400.0 baht
# Discount   : -40.0 baht (10%)
# VAT        : +25.2 baht (7%)
# ===================================
# TOTAL      : 385.2 baht 💰
# ===================================
# =====================================================


# =====================================================
# 💡 KEY MATH:
#   subtotal       = qty × price                = 5 × 80 = 400
#   discount       = subtotal × 0.10             = 40
#   after_discount = subtotal - discount         = 360
#   vat            = after_discount × 0.07       = 25.2
#   total          = after_discount + vat        = 385.2
# =====================================================


# =====================================================
# 🎁 BONUS 1: Different discount tiers
#   Buy ≥ 1000 baht → 15% off
#   Buy ≥ 500 baht  → 10% off
#   Else            → 5% off
#   (You'll need if-else from next session!)
# =====================================================


# =====================================================
# 🎁 BONUS 2: Compare 2 stores
#   Store A: 80 baht/item, no discount
#   Store B: 90 baht/item, 20% off
#   Which is cheaper for 10 items?
# =====================================================


# =====================================================
# 🔗 SHARE ON TRINKET.IO:
#   1. Copy this code → trinket.io → New Python
#   2. Paste → Run
#   3. Click "Share" → send link to parents!
#   4. They try with REAL prices from their shopping
# =====================================================
