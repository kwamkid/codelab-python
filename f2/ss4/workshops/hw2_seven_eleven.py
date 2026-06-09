# =====================================================
# 🏪 HW2 — 7-Eleven Prices (⭐⭐⭐ Advanced)
# Python Foundation 2 · Session 4 · Loops + Lists
# =====================================================
# 🎯 GOAL: 10 real 7-11 snack prices.
#    Find cheapest, priciest, total, average, count under 20.
# ⏱️  TIME: 25 minutes at home
# 🔑 SKILL: Multiple stats + counting with condition
# =====================================================

# 📝 TODO 1: Real prices from 7-Eleven (go check!)
items = [
    "🥤 Milk",
    "🍫 KitKat",
    "🍪 Cookie",
    "🍙 Onigiri",
    "🍜 Cup noodle",
    "🍌 Banana",
    "🥯 Sandwich",
    "🧃 Juice box",
    "🍡 Mochi",
    "🍩 Donut",
]

prices = [___, ___, ___, ___, ___, ___, ___, ___, ___, ___]  # baht


print("🏪 7-Eleven Price Report")
print("=" * 40)

# 📝 TODO 2: Print each item + price
for i, item in enumerate(items):
    print(f"  {item:20} {prices[i]:>4} baht")


# 📝 TODO 3: Use built-ins
total     = sum(prices)
cheapest  = min(prices)
priciest  = max(prices)
average   = round(total / len(prices), 1)


# 📝 TODO 4: Count items under 20 baht
cheap_count = 0
for price in prices:
    if price < 20:
        cheap_count += ___


# ----- Print stats -----
print("-" * 40)
print(f"💰 Total     : {total} baht")
print(f"🎯 Average   : {average} baht")
print(f"🟢 Cheapest  : {cheapest} baht ({items[prices.index(cheapest)]})")
print(f"🔴 Priciest  : {priciest} baht ({items[prices.index(priciest)]})")
print(f"💚 Under 20  : {cheap_count} items")


# =====================================================
# 📋 EXAMPLE OUTPUT:
# =====================================================
# 🏪 7-Eleven Price Report
# ========================================
#   🥤 Milk                25 baht
#   🍫 KitKat              35 baht
#   🍪 Cookie              15 baht
#   🍙 Onigiri             40 baht
#   ...
# ----------------------------------------
# 💰 Total     : 387 baht
# 🎯 Average   : 38.7 baht
# 🟢 Cheapest  : 8 baht (🍌 Banana)
# 🔴 Priciest  : 95 baht (🍙 Onigiri)
# 💚 Under 20  : 4 items
# =====================================================


# =====================================================
# 🎁 BONUS 1: With 100 baht — how many items can I buy?
#    Sort prices ascending, buy from cheapest until 100 used up
# =====================================================
# budget = 100
# spent = 0
# bought = 0
# for price in sorted(prices):
#     if spent + price <= budget:
#         spent += price
#         bought += 1
# print(f"💵 Can buy {bought} items with 100 baht")


# =====================================================
# 🎁 BONUS 2: Filter — list only items under your daily budget
# =====================================================
# my_budget = 30
# affordable = []
# for i, price in enumerate(prices):
#     if price <= my_budget:
#         affordable.append(items[i])
# print(f"💚 Affordable items: {affordable}")


# =====================================================
# 🔗 SUBMIT:
#   Trinket link → LINE group
#   🏠 Compare prices with parents — they'll be surprised!
# =====================================================
