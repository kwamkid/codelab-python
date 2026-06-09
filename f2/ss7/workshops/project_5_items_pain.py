# =====================================================
# 🔥 PROJECT — 5-Item Pricing (THE PAIN)
# Python Foundation 2 - Session 7 - Loop Control
# =====================================================
# GOAL: Calculate price for 5 items in a drink shop
#       — by COPY-PASTING the same logic 5 times.
# TIME: 25 minutes
# NO ChatGPT. NO function (def). NO list trickery.
# This file is intentionally REPETITIVE.
# =====================================================
#
# WHY THIS PAIN?
#   - Today you'll write the same logic 5 times.
#   - You'll get bored, frustrated, tired.
#   - THAT IS THE LESSON.
#   - Next session (S8) we'll learn Functions —
#     and you'll feel "ahhh, this is the cure!"
#
# Teacher rules:
#   - You may NOT ask "is there a shorter way?"
#   - You may NOT use def, list comprehension, or AI.
#   - You MUST write all 5 blocks by hand (copy-paste OK).
# =====================================================


# ── Constants for the whole shop ─────────────────────
VAT_RATE      = 0.07    # 7% VAT
DISCOUNT_RATE = 0.10    # 10% discount


# =====================================================
# ITEM 1: Soda
# =====================================================
name_1     = "Soda"
price_1    = float(input(f"Price of {name_1}: "))
quantity_1 = int(input(f"How many {name_1}: "))

subtotal_1 = price_1 * quantity_1
vat_1      = subtotal_1 * VAT_RATE
discount_1 = subtotal_1 * DISCOUNT_RATE
total_1    = subtotal_1 + vat_1 - discount_1

print(f"{name_1}: subtotal={subtotal_1:.2f}, vat={vat_1:.2f}, discount={discount_1:.2f}, total={total_1:.2f}")


# =====================================================
# ITEM 2: Coffee  (copy-paste from above and adjust!)
# =====================================================
name_2     = "Coffee"
price_2    = float(input(f"Price of {name_2}: "))
quantity_2 = int(input(f"How many {name_2}: "))

subtotal_2 = price_2 * quantity_2
vat_2      = subtotal_2 * VAT_RATE
discount_2 = subtotal_2 * DISCOUNT_RATE
total_2    = subtotal_2 + vat_2 - discount_2

print(f"{name_2}: subtotal={subtotal_2:.2f}, vat={vat_2:.2f}, discount={discount_2:.2f}, total={total_2:.2f}")


# =====================================================
# ITEM 3: Tea  (yes, copy-paste again — feeling tired?)
# =====================================================
# YOUR TURN: paste blocks 1-2 above, change all the "_2" to "_3", and the name


# =====================================================
# ITEM 4: Juice  (one more time — almost there)
# =====================================================
# YOUR TURN


# =====================================================
# ITEM 5: Water  (last one! exhausted yet?)
# =====================================================
# YOUR TURN


# =====================================================
# GRAND TOTAL
# =====================================================
grand_total = total_1 + total_2 + ___ + ___ + ___    # <-- total_3, total_4, total_5

print()
print(f"========================================")
print(f"GRAND TOTAL: {grand_total:.2f}")
print(f"========================================")


# =====================================================
# REFLECTION — answer in your head (or out loud)
# =====================================================
# 1. How many lines did you write? ____
# 2. If the shop had 50 items, how many lines? ____
# 3. If you needed to change the VAT rate, how many
#    places would you have to update? ____
# 4. How does it FEEL to write the same thing 5 times?
#    ___________________________________
# =====================================================


# =====================================================
# A WHISPER FROM THE FUTURE...
# =====================================================
# In Session 8, we'll learn:
#
#     def calculate_total(name, price, quantity):
#         subtotal = price * quantity
#         vat      = subtotal * 0.07
#         discount = subtotal * 0.10
#         total    = subtotal + vat - discount
#         print(f"{name}: total={total:.2f}")
#         return total
#
# That's it. Three lines per item -> 1 line per item.
# But for now... keep feeling the pain.
# It's the medicine.
# =====================================================
