# =====================================================
# 📜 HW3 — Grade Card (⭐⭐⭐⭐⭐ Expert)
# Python Foundation 2 · Session 4 · Loops + Lists
# =====================================================
# 🎯 GOAL: Convert scores → letter grades (A/B/C/D/F)
#    Count pass/fail, show grade distribution.
# ⏱️  TIME: 30 minutes at home
# 🔑 SKILL: Loop + if-elif chain + count by category
# =====================================================

# 📝 TODO 1: Fill in scores from a class (real or made up)
scores = [95, 85, 72, 55, 88, 67, 91, 45, 78, 82]


print("📜 Class Grade Card")
print("=" * 35)


# 📝 TODO 2: Initialize grade counters
count_A = 0
count_B = 0
count_C = 0
count_D = 0
count_F = 0
pass_count = 0
fail_count = 0


# 📝 TODO 3: For each score, assign letter + count it
for i, score in enumerate(scores, start=1):

    # Grading rules:
    #   ≥ 80 → A
    #   ≥ 70 → B
    #   ≥ 60 → C
    #   ≥ 50 → D
    #   else → F
    if score >= 80:
        grade = "A"
        count_A += 1
    elif score >= 70:
        grade = "B"
        count_B += 1
    elif score >= ___:
        grade = "C"
        count_C += 1
    elif score >= ___:
        grade = "D"
        count_D += 1
    else:
        grade = ___
        count_F += 1

    # Pass = anything not F (≥ 50)
    if score >= 50:
        pass_count += 1
    else:
        fail_count += 1

    # Print this student's result
    print(f"  Student #{i:2d}: {score:>3} → {grade}")


# 📝 TODO 4: Summary
print("-" * 35)
print(f"✅ Pass: {pass_count} / {len(scores)}")
print(f"❌ Fail: {fail_count} / {len(scores)}")


# 📝 TODO 5: Grade distribution mini-chart (use * blocks)
print()
print("📊 Distribution:")
print(f"  A : {'★' * count_A:8} ({count_A})")
print(f"  B : {'★' * count_B:8} ({count_B})")
print(f"  C : {'★' * count_C:8} ({count_C})")
print(f"  D : {'★' * count_D:8} ({count_D})")
print(f"  F : {'★' * count_F:8} ({count_F})")


# =====================================================
# 📋 EXAMPLE OUTPUT:
# =====================================================
# 📜 Class Grade Card
# ===================================
#   Student # 1:  95 → A
#   Student # 2:  85 → A
#   Student # 3:  72 → B
#   Student # 4:  55 → D
#   Student # 5:  88 → A
#   ...
# -----------------------------------
# ✅ Pass: 9 / 10
# ❌ Fail: 1 / 10
#
# 📊 Distribution:
#   A : ★★★★     (4)
#   B : ★★       (2)
#   C : ★★       (2)
#   D : ★        (1)
#   F : ★        (1)
# =====================================================


# =====================================================
# 🎁 BONUS 1: Class average + median
# =====================================================
# avg = sum(scores) / len(scores)
# print(f"📊 Class average: {round(avg, 1)}")


# =====================================================
# 🎁 BONUS 2: Highlight top 3 + bottom 3
# =====================================================
# top3 = sorted(scores, reverse=True)[:3]
# print(f"🏆 Top 3 scores: {top3}")


# =====================================================
# 🎁 BONUS 3: Use a dictionary for grades (preview F3)
# =====================================================
# grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
# for score in scores:
#     if score >= 80: grades["A"] += 1
#     elif ...
# print(grades)


# =====================================================
# 🔗 SUBMIT:
#   Trinket link → LINE group
#   🏠 Show parents → discuss class trend!
# =====================================================
