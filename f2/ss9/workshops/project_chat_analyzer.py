# ═══════════════════════════════════════════════════════════
# 💬 Project · วิเคราะห์ข้อความ Chat
# F2 Session 09 · String Methods  ·  20 นาที
# ═══════════════════════════════════════════════════════════
#
# 🎯 รวมทุกอย่าง: string + loop + function (S4 + S8 + S9)
# เอาข้อความแชทจริงมาใส่ แล้วดูสถิติ!
# ───────────────────────────────────────────────────────────

def analyze(text):
    words = text.split()          # แยกประโยคเป็นคำ
    vowel_count = 0
    digit_count = 0

    for char in text.lower():
        if char in "aeiou":
            vowel_count += 1
        # TODO 1: ถ้า char เป็นตัวเลข ให้ digit_count เพิ่ม 1
        if char.isdigit():
            digit_count = ____   # 👈 แก้ตรงนี้: digit_count + 1

    # TODO 2: หาคำที่ยาวที่สุด
    longest = ""
    for w in words:
        if len(w) > len(longest):
            longest = ____   # 👈 แก้ตรงนี้: w

    print("=== รายงานวิเคราะห์ข้อความ ===")
    print("จำนวนคำ      :", len(words))
    print("จำนวนสระ     :", vowel_count)
    print("จำนวนตัวเลข  :", digit_count)
    print("คำที่ยาวสุด  :", longest)


# ───────────────────────────────────────────────────────────
msg = input("วางข้อความแชทที่อยากวิเคราะห์: ")
analyze(msg)
