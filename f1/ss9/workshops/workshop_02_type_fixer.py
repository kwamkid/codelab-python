# ═══════════════════════════════════════════════════════════
# 🐛 W2 · Type Fixer — แก้ TypeError (str + int)
# F1 Session 09 · Review & Bug Hunt
# ═══════════════════════════════════════════════════════════
# 🎯 error ยอดฮิต: เอา str มา + กับ int → TypeError
# ───────────────────────────────────────────────────────────

age = input("อายุ: ")     # input ได้ str เสมอ!

# 🐛 BUG — age เป็น str จะ + 1 ไม่ได้ (TypeError)
# แก้: แปลง age เป็น int ก่อน
next_age = int(____) + 1     # 👈 แก้ตรงนี้: age

print(f"ปีหน้าอายุ {next_age}")

# 🐛 BUG 2 — เอา str + int ตรงๆ
score = 90
# print("คะแนน: " + score)   ← TypeError!
print("คะแนน: " + str(score))   # 👈 ต้อง str(score)

# ✅ แก้แล้วรันได้ — เข้าใจว่าทำไมต้อง cast
