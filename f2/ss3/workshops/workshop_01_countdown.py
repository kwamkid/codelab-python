# =====================================================
# 🎊 Workshop 1 — New Year Countdown!
# Python Foundation 2 · Session 3 · For Loops Deep
# =====================================================
# 🎯 GOAL: Count from 10 down to 1, then print "Happy New Year!"
# ⏱️  TIME: 10 minutes
# 🔑 SKILL: range(start, stop, step) with step = -1
# =====================================================

# 📝 TODO: Count 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
#    Hint: range(start, stop, step)
#      start = 10
#      stop  = 0     (NOT included — so 1 is the last number)
#      step  = -1    (go backwards!)

for i in range(___, ___, ___):
    print(i)

print("🎉 Happy New Year!")


# =====================================================
# 📋 EXPECTED OUTPUT:
# =====================================================
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 🎉 Happy New Year!
# =====================================================


# =====================================================
# 🎁 BONUS 1: Add drama — print 💥 after each number
# =====================================================
# for i in range(10, 0, -1):
#     print(f"{i} 💥")


# =====================================================
# 🎁 BONUS 2: Include 0 before "Happy New Year!"
#    Change stop to -1 so 0 is included
# =====================================================
# for i in range(10, -1, -1):
#     print(i)
# print("🎉 Happy New Year!")


# =====================================================
# 🎁 BONUS 3: Add a time delay (real countdown feeling!)
# =====================================================
# import time
# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)   # wait 1 second
# print("🎉 Happy New Year!")
# =====================================================
