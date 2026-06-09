# ═══════════════════════════════════════════════════════════
# 🔐 Project · Login System — and (รวมเงื่อนไข)
# F1 Session 04 · If-Else + Logic  ·  20 นาที
# ═══════════════════════════════════════════════════════════
# 🎯 ต้องถูกทั้ง username AND password ถึงเข้าได้
#    (เหมือน login จริงของทุก app!)
# ───────────────────────────────────────────────────────────

USERNAME = "admin"
PASSWORD = "1234"

user = input("Username: ")
pw = input("Password: ")

# TODO: ต้องถูกทั้งคู่ → ใช้ and
if user == USERNAME and pw == ____:   # 👈 แก้ตรงนี้: PASSWORD
    print("🎉 ยินดีต้อนรับ admin!")
else:
    print("⛔ เข้าระบบไม่สำเร็จ")

# ✅ ทดสอบ: admin/1234 -> สำเร็จ / อย่างใดอย่างหนึ่งผิด -> ไม่สำเร็จ
