# =====================================================
# 🎂 Project — Birthday Party Budget
# Python Foundation 2 · Session 3 · For Loops Deep
# =====================================================
# 🎯 GOAL: Loop through 5 items → ask price → sum → check budget
# ⏱️  TIME: 25 minutes
# 🏠 AT HOME: Ask your parents — what's a realistic party budget?
# =====================================================

print("🎂 Birthday Party Budget Calculator")
print("=" * 40)

# 5 items to buy for the party
items = ["🎂 Cake", "🍭 Candy", "🥤 Drinks", "🎈 Balloons", "🎁 Gifts"]
total = 0

# 📝 TODO 1: Loop through each item → ask price → add to total
for item in items:
    price = int(input(f"{item} price: "))
    total = total + price


# 📝 TODO 2: Print the grand total
print()
print("=" * 40)
print(f"💰 Grand Total: {total} baht")


# 📝 TODO 3: Check if over budget (set budget limit)
#    If total > 1000 → warn the user
if total > ___:
    print("⚠️  Over budget! What can you cut?")
else:
    print("✅ Within budget — good planning!")


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# 🎂 Cake price: 500
# 🍭 Candy price: 200
# 🥤 Drinks price: 100
# 🎈 Balloons price: 150
# 🎁 Gifts price: 300
#
# 💰 Grand Total: 1250 baht
# ⚠️  Over budget! What can you cut?
# =====================================================


# =====================================================
# 🎁 BONUS 1: Track prices in a list, find the most expensive
# =====================================================
# prices = []
# for item in items:
#     price = int(input(f"{item} price: "))
#     prices.append(price)
#     total += price
#
# max_price = max(prices)
# max_item = items[prices.index(max_price)]
# print(f"😱 Most expensive: {max_item} ({max_price} baht)")


# =====================================================
# 🎁 BONUS 2: Ask parents for their real budget
# =====================================================
# budget = int(input("\nWhat's your parents' budget? "))
# remaining = budget - total
# if remaining >= 0:
#     print(f"💚 {remaining} baht remaining")
# else:
#     print(f"💔 Over by {abs(remaining)} baht")
# =====================================================
