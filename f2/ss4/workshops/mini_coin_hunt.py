# =====================================================
# 🪙 Mini — Coin Hunt
# Python Foundation 2 · Session 4 · Loops + Lists
# =====================================================
# 🎯 GOAL: Find total + biggest coin WITHOUT sum() or max()
#    Track stats yourself with the accumulator pattern.
# ⏱️  TIME: 15 minutes
# 🔑 SKILL: Manual accumulator + conditional update
# =====================================================

coins = [10, 25, 5, 50, 1, 100, 20, 5, 10, 50]

print("🪙 Coin Hunt — find total &amp; biggest")
print("=" * 38)


# 📝 TODO 1: Initialize trackers BEFORE the loop
total = ___
biggest = ___    # start at 0 so any coin will be bigger


# 📝 TODO 2: Loop through coins
#    For each coin:
#      • add to total
#      • if coin > biggest, update biggest
for coin in coins:
    total = ___ + coin

    if coin > ___:
        biggest = ___

    print(f"  Found 🪙 {coin}  →  total: {total}, biggest: {biggest}")


# 📝 TODO 3: Print final stats
print("=" * 38)
print(f"💰 Total : {total}")
print(f"🏆 Biggest: {biggest}")


# =====================================================
# 📋 EXPECTED OUTPUT (truncated):
# =====================================================
# 🪙 Coin Hunt — find total & biggest
# ======================================
#   Found 🪙 10  →  total: 10, biggest: 10
#   Found 🪙 25  →  total: 35, biggest: 25
#   Found 🪙 5   →  total: 40, biggest: 25
#   Found 🪙 50  →  total: 90, biggest: 50
#   ...
# ======================================
# 💰 Total : 276
# 🏆 Biggest: 100
# =====================================================


# =====================================================
# 🎁 BONUS 1: Compare with built-in functions
# =====================================================
# print(f"Built-in sum: {sum(coins)}")
# print(f"Built-in max: {max(coins)}")
# # Should match your DIY values!


# =====================================================
# 🎁 BONUS 2: Also track smallest coin
# =====================================================
# smallest = coins[0]   # start with first coin
# for coin in coins:
#     if coin < smallest:
#         smallest = coin
# print(f"🧂 Smallest: {smallest}")


# =====================================================
# 🎁 BONUS 3: Count coins ≥ 25 baht
# =====================================================
# big_count = 0
# for coin in coins:
#     if coin >= 25:
#         big_count += 1
# print(f"💎 Big coins (≥25): {big_count}")


# =====================================================
# 💡 KEY PATTERN — Accumulator:
#   1. Initialize a tracker variable BEFORE the loop
#   2. Update it inside the loop based on each item
#   3. Read the final value AFTER the loop
# =====================================================
