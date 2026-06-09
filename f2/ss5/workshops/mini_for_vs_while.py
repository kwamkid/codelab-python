# =====================================================
# 🤔 Mini — For or While?
# Python Foundation 2 · Session 5 · While Loops + random
# =====================================================
# 🎯 GOAL: For each problem, pick the right loop + EXPLAIN why.
# ⏱️  TIME: 10 minutes
# =====================================================

# For each problem below:
#   • Write "for" or "while"
#   • Add a short reason in the comment
#   • If you have time, write the actual code!


# =====================================================
# 1️⃣  Print times table 7 (1-12)
# =====================================================
# 📝 Your choice: ___
# 💭 Reason: ___

# Sample code:
# for i in range(1, 13):
#     print(f"7 × {i} = {7*i}")


# =====================================================
# 2️⃣  Ask password until correct
# =====================================================
# 📝 Your choice: ___
# 💭 Reason: ___

# Sample code:
# password = ""
# while password != "secret123":
#     password = input("Password: ")
# print("✅ Welcome!")


# =====================================================
# 3️⃣  Greet 25 students by name (you have the list)
# =====================================================
# 📝 Your choice: ___
# 💭 Reason: ___

# Sample code:
# students = [...]   # 25 names
# for s in students:
#     print(f"Hi {s}!")


# =====================================================
# 4️⃣  Save money until you have 1000 baht
#     (income each week is random)
# =====================================================
# 📝 Your choice: ___
# 💭 Reason: ___

# Sample code:
# import random
# money = 0
# week = 0
# while money < 1000:
#     income = random.randint(50, 200)
#     money += income
#     week += 1
# print(f"Saved 1000 in {week} weeks!")


# =====================================================
# 5️⃣  Sum a list of test scores
# =====================================================
# 📝 Your choice: ___
# 💭 Reason: ___

# Sample code:
# scores = [85, 92, 78, 95, 88]
# total = 0
# for s in scores:
#     total += s


# =====================================================
# 🔑 ANSWER KEY (don't peek!):
# =====================================================
# 1. for    — fixed count (1 to 12)
# 2. while  — unknown attempts
# 3. for    — fixed list, walk all
# 4. while  — unknown weeks needed
# 5. for    — walk a list
#
# Pattern: known count → for · depends on condition → while
# =====================================================


# =====================================================
# 🎁 BONUS: Discuss with a friend
#   Can you think of MORE problems for each type?
#   Each person makes 2 problems, swap, decide!
# =====================================================
