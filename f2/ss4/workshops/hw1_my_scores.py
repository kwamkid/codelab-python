# =====================================================
# 📊 HW1 — My Real Scores (⭐⭐ Required)
# Python Foundation 2 · Session 4 · Loops + Lists
# =====================================================
# 🎯 GOAL: Use YOUR real test scores from school.
#    Find max, min, average, and which subject was best.
# ⏱️  TIME: 20 minutes at home
# 🔑 SKILL: enumerate + max + min + sum + index lookup
# =====================================================

# 📝 TODO 1: Fill in YOUR real scores from school!
subjects = ["Math", "English", "Science", "Thai", "Art"]
scores   = [___, ___, ___, ___, ___]   # ← your real grades


# 📝 TODO 2: Print each subject + score using enumerate
print("📊 My Real Scores")
print("=" * 30)

for i, subject in enumerate(subjects):
    print(f"  {subject:10}: {scores[i]}")


# 📝 TODO 3: Use max/min/sum
highest = max(scores)
lowest  = min(scores)
total   = sum(scores)
average = round(total / len(scores), 1)


# 📝 TODO 4: Find WHICH subject is best/worst
best_subject  = subjects[scores.index(___)]      # use highest
worst_subject = subjects[scores.index(___)]      # use lowest


# ----- Print final report -----
print("-" * 30)
print(f"🥇 Best   : {best_subject} ({highest})")
print(f"📉 Worst  : {worst_subject} ({lowest})")
print(f"📊 Total  : {total}")
print(f"🎯 Average: {average}")


# =====================================================
# 📋 EXAMPLE OUTPUT:
# =====================================================
# 📊 My Real Scores
# ==============================
#   Math      : 85
#   English   : 92
#   Science   : 78
#   Thai      : 95
#   Art       : 88
# ------------------------------
# 🥇 Best   : Thai (95)
# 📉 Worst  : Science (78)
# 📊 Total  : 438
# 🎯 Average: 87.6
# =====================================================


# =====================================================
# 🎁 BONUS 1: Pass/fail per subject (≥ 50)
# =====================================================
# for i, subject in enumerate(subjects):
#     status = "PASS ✅" if scores[i] >= 50 else "FAIL ❌"
#     print(f"  {subject}: {scores[i]} → {status}")


# =====================================================
# 🎁 BONUS 2: Compare with last semester
#    Add second list of old scores → calculate diff per subject
# =====================================================


# =====================================================
# 🔗 SUBMIT:
#   Trinket link → LINE group
#   🏠 Show parents → talk about subjects to improve!
# =====================================================
