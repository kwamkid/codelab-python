# =====================================================
# 💪 HW1 — BMI Calculator (⭐⭐ Required)
# Python Foundation 1 · Session 3 · Math Operators
# =====================================================
# 🎯 GOAL: Calculate Body Mass Index (BMI)
#    Formula: BMI = weight / (height × height)
# ⏱️  TIME: 15 minutes at home
# 🔑 SKILL: float input, ** (power), round()
# 🔗 SHARE: Trinket → let parents try with their own data!
# =====================================================

print("💪 BMI Calculator")
print("=" * 30)


# 📝 TODO 1: Ask for weight (kg) — float because of decimals
weight = float(input("Weight (kg): "))


# 📝 TODO 2: Ask for height (m) — also float
#    Example: 1.4 not 140
height = float(input("Height (m, e.g. 1.4): "))


# 📝 TODO 3: Calculate BMI
#    BMI = weight / (height × height)
#    Or: weight / height ** 2
bmi = ___ / (___ ** 2)


# 📝 TODO 4: Round to 1 decimal place
#    round(value, 1)
bmi_rounded = round(___, 1)


# 📝 TODO 5: Print result
print()
print(f"Your BMI: {bmi_rounded}")


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# 💪 BMI Calculator
# ==============================
# Weight (kg): 35
# Height (m, e.g. 1.4): 1.4
#
# Your BMI: 17.9
# =====================================================


# =====================================================
# 💡 BMI MATH:
#   BMI = weight / height²
#   Example: 35 / (1.4 × 1.4) = 35 / 1.96 = 17.857...
#   Round to 1 decimal: 17.9
# =====================================================


# =====================================================
# 🎁 BONUS 1: Accept height in cm
#    cm to m: divide by 100
# =====================================================
# height_cm = float(input("Height (cm): "))
# height_m = height_cm / 100
# bmi = weight / (height_m ** 2)


# =====================================================
# 🎁 BONUS 2: Print body category
#    BMI < 18.5  → underweight
#    BMI < 25    → normal
#    BMI < 30    → overweight
#    Else        → obese
#    (Uses if-else from next session!)
# =====================================================


# =====================================================
# 🎁 BONUS 3: Calculate ideal weight for your height
#    Ideal = 22 × height² (using BMI 22 as ideal)
# =====================================================
# ideal_weight = 22 * (height ** 2)
# print(f"Ideal weight: {round(ideal_weight, 1)} kg")


# =====================================================
# 🔗 SUBMIT:
#   1. Share code on Trinket.io
#   2. Send link to LINE group
#   3. 🏠 Let parents try with their own weight/height!
#
#   Deadline: before next session
# =====================================================
