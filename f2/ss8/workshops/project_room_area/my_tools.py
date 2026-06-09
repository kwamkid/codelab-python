# ═══════════════════════════════════════════════════════════
# 📐 my_tools.py — กล่องเครื่องมือคำนวณพื้นที่
# F2 Session 08 · Project (Multi-file)
# ═══════════════════════════════════════════════════════════
#
# 🎯 ไฟล์นี้เก็บ "function" ไว้อย่างเดียว — ไม่มีการรันโปรแกรม
# main.py จะ import function จากไฟล์นี้ไปใช้
# 👉 นี่คือวิธีที่ programmer จริงจัดระเบียบโค้ด!
# ───────────────────────────────────────────────────────────

def area_rectangle(width, height):
    # พื้นที่สี่เหลี่ยม = กว้าง × ยาว
    return width * height

def area_triangle(base, height):
    # พื้นที่สามเหลี่ยม = 0.5 × ฐาน × สูง
    return 0.5 * base * height

def area_circle(radius, pi=3.14):
    # พื้นที่วงกลม = pi × r × r   (pi เป็น default parameter)
    # TODO: เติมสูตรพื้นที่วงกลม
    return ____   # 👈 แก้ตรงนี้: pi * radius * radius
