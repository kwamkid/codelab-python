# ═══════════════════════════════════════════════════════════
# ⭐ HW2 (เก่ง · optional) · BMI + function ประเมินผล
# F2 Session 08 · Functions  ·  เวลา ~30 นาที
# ═══════════════════════════════════════════════════════════
#
# 🎯 Challenge: เขียน 2 function แล้วเรียกซ้อนกัน!
#   1) calc_bmi(weight, height)  → คืนค่า BMI
#   2) bmi_result(bmi)           → คืนข้อความ ผอม/ปกติ/อ้วน
#
# 💡 Hint: เรียกซ้อน — bmi_result(calc_bmi(w, h))
# ───────────────────────────────────────────────────────────

def calc_bmi(weight, height):
    # BMI = น้ำหนัก / (ส่วนสูง ยกกำลัง 2)   ส่วนสูงหน่วยเมตร
    bmi = weight / (height ** 2)
    return round(bmi, 1)

def bmi_result(bmi):
    if bmi < 18.5:
        return "น้ำหนักน้อย"
    elif bmi <= 25:
        return "น้ำหนักปกติ 👍"
    else:
        return "น้ำหนักเกิน"


# ───────────────────────────────────────────────────────────
# ทดสอบ — เรียก function ซ้อนกัน
my_bmi = calc_bmi(50, 1.6)
print("BMI =", my_bmi, "->", bmi_result(my_bmi))   # 19.5 -> ปกติ

# ✅ เกณฑ์เสร็จ: 2 function แยกหน้าที่ชัด + ครบ 3 ช่วง
