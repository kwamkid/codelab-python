# =====================================================
# 📊 Workshop 2 — Test Scores
# Python Foundation 2 · Session 4 · Loops + Lists
# =====================================================
# 🎯 GOAL: Analyze 5 subject scores → max, min, sum, avg.
# ⏱️  TIME: 15 minutes
# 🔑 SKILL: enumerate() + max() / min() / sum()
# =====================================================

subjects = ["Math", "English", "Science", "Thai", "Art"]
scores   = [85, 92, 78, 95, 88]

print("📊 Score Report")
print("=" * 35)


# 📝 TODO 1: Loop with enumerate to print "1. Math: 85"
for i, subject in enumerate(subjects, start=1):
    print(f"{i}. {subject:10} : {___[i-1]}")
    # Hint: scores[i-1] gives the matching score


# 📝 TODO 2: Use built-in functions
total   = ___(scores)         # sum()
highest = ___(scores)         # max()
lowest  = ___(scores)         # min()
average = total / ___(scores) # use len()


# 📝 TODO 3: Print the stats
print("-" * 35)
print(f"📊 Total   : {total}")
print(f"🥇 Highest : {highest}")
print(f"📉 Lowest  : {lowest}")
print(f"🎯 Average : {round(average, 1)}")


# =====================================================
# 📋 EXPECTED OUTPUT:
# =====================================================
# 📊 Score Report
# ===================================
# 1. Math       : 85
# 2. English    : 92
# 3. Science    : 78
# 4. Thai       : 95
# 5. Art        : 88
# -----------------------------------
# 📊 Total   : 438
# 🥇 Highest : 95
# 📉 Lowest  : 78
# 🎯 Average : 87.6
# =====================================================


# =====================================================
# 🎁 BONUS 1: Find WHICH subject was highest
#    Use scores.index(highest) to get the position
# =====================================================
# best_idx = scores.index(highest)
# best_subject = subjects[best_idx]
# print(f"🏆 Best subject: {best_subject}")


# =====================================================
# 🎁 BONUS 2: Pass/Fail per subject (≥ 50)
# =====================================================
# for subj, score in zip(subjects, scores):
#     status = "PASS ✅" if score >= 50 else "FAIL ❌"
#     print(f"{subj}: {score} → {status}")
