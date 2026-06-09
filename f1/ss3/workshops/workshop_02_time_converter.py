# =====================================================
# ⏱ Workshop 2 — Time Converter
# Python Foundation 1 · Session 3 · Math Operators
# =====================================================
# 🎯 GOAL: Convert seconds → minutes + seconds
#    Example: 500 seconds = 8 min 20 sec
# ⏱️  TIME: 15 minutes
# 🔑 SKILL: // (floor division) and % (modulo)
# =====================================================

print("⏱  Time Converter")
print("=" * 30)


# 📝 TODO 1: Ask user for total seconds
total = int(input("Total seconds: "))


# 📝 TODO 2: Use // to get whole minutes
#    500 // 60 = 8 minutes
minutes = ___ // 60


# 📝 TODO 3: Use % to get leftover seconds
#    500 % 60 = 20 seconds
seconds = ___ % 60


# 📝 TODO 4: Print result
print()
print(f"{total} seconds = {minutes} min {seconds} sec")


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# ⏱  Time Converter
# ==============================
# Total seconds: 500
#
# 500 seconds = 8 min 20 sec
# =====================================================


# =====================================================
# 🤔 WHY does this work?
# =====================================================
#   500 // 60 = 8         ← How many full 60-sec chunks?
#   500  % 60 = 20        ← What's left after 8 chunks?
#   Check: 8 * 60 + 20 = 500 ✓


# =====================================================
# 🎁 BONUS 1: Convert seconds → hours + minutes + seconds
# =====================================================
# total = 3725  # 1 hour 2 min 5 sec
# hours = total // 3600
# remaining = total % 3600
# minutes = remaining // 60
# seconds = remaining % 60
# print(f"{hours} hr {minutes} min {seconds} sec")


# =====================================================
# 🎁 BONUS 2: Convert hours → days + hours
#    1 day = 24 hours
# =====================================================
# total_hours = int(input("Total hours: "))
# days = total_hours // 24
# hours = total_hours % 24
# print(f"{days} days {hours} hours")


# =====================================================
# 🎁 BONUS 3: Convert money — 250 baht → ?
#    100-baht notes + 50-baht coins + 10-baht coins + 1-baht coins
# =====================================================
# money = 376
# notes_100 = money // 100         # 3 notes
# remaining = money % 100          # 76 baht
# coins_50  = remaining // 50      # 1 coin
# remaining = remaining % 50       # 26 baht
# # ... and so on!
