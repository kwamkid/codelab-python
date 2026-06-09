# =====================================================
# ➕ Workshop 2 — Sum of Even Numbers (Accumulator)
# Python Foundation 2 · Session 3 · For Loops Deep
# =====================================================
# 🎯 GOAL:
#   1) Use range(start, stop, step) with step=2
#   2) Apply the accumulator pattern: total = total + n
#
# ⏱️  TIME: 15 minutes
# =====================================================

# 📝 TODO 1: Create variable 'total' starting at 0
#    (This is the ACCUMULATOR — it collects the sum)
total = ___

print("🔢 Sum of even numbers 2 to 20")
print("=" * 35)

# 📝 TODO 2: Use range(start, stop, step) to get 2, 4, 6, ..., 20
#    Hint: start=2, stop=21 (exclusive!), step=2
for n in range(___, ___, ___):

    # 📝 TODO 3: Add n to total (the ACCUMULATOR!)
    total = ___ + n

    # Print progress each round
    print(f"Added {n} → total: {total}")

print("=" * 35)
print(f"💰 Grand total = {total}")


# =====================================================
# 📋 EXPECTED OUTPUT:
# =====================================================
# 🔢 Sum of even numbers 2 to 20
# ===================================
# Added 2 → total: 2
# Added 4 → total: 6
# Added 6 → total: 12
# Added 8 → total: 20
# Added 10 → total: 30
# Added 12 → total: 42
# Added 14 → total: 56
# Added 16 → total: 72
# Added 18 → total: 90
# Added 20 → total: 110
# ===================================
# 💰 Grand total = 110
# =====================================================


# =====================================================
# 🎁 BONUS 1: Use the += shortcut
#    total += n   is short for   total = total + n
# =====================================================


# =====================================================
# 🎁 BONUS 2: Sum odd numbers 1 to 19 instead
#    Just change range(2, 21, 2) to range(1, 20, 2)
# =====================================================


# =====================================================
# 🎁 BONUS 3: Compute the average
# =====================================================
# total = 0
# count = 0
# for n in range(2, 21, 2):
#     total += n
#     count += 1
# average = total / count
# print(f"Average = {average}")   # should print 11.0
# =====================================================
