# ═══════════════════════════════════════════════════════════
# 🖥️ W2 · กลับคำ (Reverse) — string + function
# F2 Session 09 · String Methods
# ═══════════════════════════════════════════════════════════
#
# 🎯 หน้าที่ของเด็ก: เติม logic การกลับคำ (# TODO)
# Trick: ต่อตัวอักษรไว้ "ข้างหน้า" ของผลลัพธ์เดิม
# ───────────────────────────────────────────────────────────

def reverse(word):
    result = ""
    for char in word:
        # TODO: ต่อ char ไว้ "ข้างหน้า" result
        # (char + result ไม่ใช่ result + char นะ!)
        result = ____   # 👈 แก้ตรงนี้: char + result
    return result


# ───────────────────────────────────────────────────────────
# ทดสอบ + เล่นทายกับเพื่อน
print(reverse("hello"))     # ควรได้ "olleh"
print(reverse("codelab"))   # ควรได้ "baledoc"

secret = input("\nพิมพ์คำลับ แล้วให้เพื่อนทาย: ")
print("คำกลับหลังคือ:", reverse(secret))
