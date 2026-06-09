# =====================================================
# 🍿 Project — Snack Budget Analyzer
# Python Foundation 2 · Session 4 · Loops + Lists
# =====================================================
# 🎯 GOAL: Track snack spending across 7 days → analyze!
# ⏱️  TIME: 25 minutes
# 🔑 SKILL: Loop + list.append + max/min/sum + enumerate
# 🏠 SHARE: Talk with parents about real spending
# =====================================================

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
spending = []   # we'll fill this up


print("🍿 Snack Budget — 1 week tracker")
print("=" * 40)


# 📝 TODO 1: Loop 7 days, ask user for each day's spending
for day in days:
    amount = int(input(f"How much spent on {day}? "))
    spending.append(amount)


# 📝 TODO 2: Calculate stats
total   = sum(spending)
average = round(total / len(spending), 1)
biggest = max(spending)
smallest = min(spending)


# 📝 TODO 3: Find which day was biggest / smallest
biggest_day = days[spending.index(biggest)]
smallest_day = days[spending.index(smallest)]


# 📝 TODO 4: Count how many days you spent over 50 baht
over_50 = 0
for amount in spending:
    if amount > 50:
        over_50 += 1


# ----- Print the report -----
print()
print("=" * 40)
print("📊 WEEK REPORT")
print("=" * 40)

# Per-day breakdown using enumerate
for i, day in enumerate(days):
    bar = "█" * (spending[i] // 10)   # 1 block per 10 baht
    print(f"{day} : {spending[i]:>4} baht  {bar}")

print("-" * 40)
print(f"💰 Total      : {total} baht")
print(f"🎯 Average    : {average} baht/day")
print(f"🥇 Biggest    : {biggest} baht ({biggest_day})")
print(f"🧂 Smallest   : {smallest} baht ({smallest_day})")
print(f"⚠️  Over 50: {over_50} day(s)")
print("=" * 40)


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# How much spent on Mon? 30
# How much spent on Tue? 50
# How much spent on Wed? 20
# How much spent on Thu? 100
# How much spent on Fri? 80
# How much spent on Sat? 40
# How much spent on Sun? 60
#
# 📊 WEEK REPORT
# ========================================
# Mon :   30 baht  ███
# Tue :   50 baht  █████
# Wed :   20 baht  ██
# Thu :  100 baht  ██████████
# Fri :   80 baht  ████████
# Sat :   40 baht  ████
# Sun :   60 baht  ██████
# ----------------------------------------
# 💰 Total      : 380 baht
# 🎯 Average    : 54.3 baht/day
# 🥇 Biggest    : 100 baht (Thu)
# 🧂 Smallest   : 20 baht (Wed)
# ⚠️  Over 50  : 4 day(s)
# ========================================


# =====================================================
# 🎁 BONUS 1: Predict monthly spending
#    Multiply average by 30 days
# =====================================================
# monthly = average * 30
# print(f"📅 Estimated monthly: {round(monthly, 0)} baht")


# =====================================================
# 🎁 BONUS 2: Compare weekday vs weekend spending
#    weekdays = sum of Mon-Fri, weekend = Sat + Sun
# =====================================================


# =====================================================
# 🔗 SHARE:
#   1. Trinket → send link to parents
#   2. Talk about real budget — what's reasonable?
#   3. Try again next week with REAL numbers!
# =====================================================
