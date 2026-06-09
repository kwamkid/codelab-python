# =====================================================
# 💰 HW2 — Savings Tracker (⭐⭐⭐ Advanced)
# Python Foundation 2 · Session 3 · For Loops Deep
# =====================================================
# 🎯 GOAL:
#   Save 5 baht per day for 30 days.
#   Use the ACCUMULATOR pattern to track the running total.
#   Print each day's saving AND running total.
#
# 🔑 KEY SKILL: accumulator (total = total + x)
#
# ⏱️  TIME: 25-35 minutes at home
# =====================================================

# Configuration
daily_amount = 5      # saving 5 baht per day
days = 30             # for 30 days

# 📝 TODO 1: Create a variable 'total' starting at 0
#    This is the accumulator — it will grow each day
total = ___

print("💰 30-Day Savings Plan")
print("=" * 40)

# 📝 TODO 2: Loop from day 1 to day 30
#    Hint: range(1, 31)  — remember stop is EXCLUSIVE!
for day in range(___, ___):

    # 📝 TODO 3: Add daily_amount to total (ACCUMULATOR!)
    total = ___ + daily_amount

    # 📝 TODO 4: Print "Day X: +5 → total: YY"
    #    Use f-string for clean output
    print(f"Day {day}: +{daily_amount} → total: {total}")

print("=" * 40)
print(f"🎉 After 30 days, you saved {total} baht!")


# =====================================================
# 📋 EXPECTED OUTPUT:
# =====================================================
# 💰 30-Day Savings Plan
# ========================================
# Day 1: +5 → total: 5
# Day 2: +5 → total: 10
# Day 3: +5 → total: 15
# Day 4: +5 → total: 20
# ...
# Day 29: +5 → total: 145
# Day 30: +5 → total: 150
# ========================================
# 🎉 After 30 days, you saved 150 baht!
# =====================================================


# =====================================================
# 🎁 BONUS 1: Mark every 7th day with ✨ (weekly milestone)
# =====================================================
# for day in range(1, 31):
#     total = total + daily_amount
#     marker = " ✨ Weekly milestone!" if day % 7 == 0 else ""
#     print(f"Day {day}: +{daily_amount} → total: {total}{marker}")


# =====================================================
# 🎁 BONUS 2: Growing savings — save more each day
#    Day 1: 5, Day 2: 10, Day 3: 15, ...
# =====================================================
# total = 0
# for day in range(1, 31):
#     amount_today = day * 5   # grows each day!
#     total = total + amount_today
#     print(f"Day {day}: +{amount_today} → total: {total}")
#
# Can you guess the final total? (Hint: it's more than 2000!)


# =====================================================
# 🎁 BONUS 3: Use the += shortcut
# =====================================================
# total += daily_amount     # same as: total = total + daily_amount


# =====================================================
# 📸 SUBMIT:
#   Screenshot your code + output → send to LINE group
#   Deadline: before next session
# =====================================================
