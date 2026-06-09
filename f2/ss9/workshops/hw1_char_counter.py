# ═══════════════════════════════════════════════════════════
# 🏠 HW1 (บังคับ) · Character Counter
# F2 Session 09 · String Methods  ·  ~20 นาที
# ═══════════════════════════════════════════════════════════
#
# 🎯 โจทย์: นับ ตัวอักษร / ตัวเลข / เว้นวรรค แยกกัน
# ❌ ห้ามใช้ AI / ChatGPT ในการบ้านบังคับ
# ───────────────────────────────────────────────────────────

text = input("พิมพ์ข้อความ: ")

letters = 0
digits = 0
spaces = 0

for char in text:
    if char.isalpha():
        # TODO 1: นับตัวอักษร
        letters = ____      # 👈 letters + 1
    elif char.isdigit():
        # TODO 2: นับตัวเลข
        digits = ____       # 👈 digits + 1
    elif char == " ":
        spaces = spaces + 1

print("อักษร:", letters, "| ตัวเลข:", digits, "| เว้นวรรค:", spaces)

# ✅ ทดสอบ: "Code 123" -> อักษร: 4, ตัวเลข: 3, เว้นวรรค: 1
