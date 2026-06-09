# ═══════════════════════════════════════════════════════════
# 🔥 HW3 (ทุกคน) · Palindrome + ส่งรหัสลับให้คนสำคัญ
# F2 Session 09 · String Methods  ·  15 + 5 นาที
# ═══════════════════════════════════════════════════════════
#
# ── PART A (15 นาที): เช็คคำอ่านกลับ ────────────────────────
# Palindrome = คำที่อ่านหน้าไปหลัง กับ หลังมาหน้า เหมือนกัน
# เช่น madam, racecar, level
# 💡 ใช้ trick reverse จาก W2!

def reverse(word):
    result = ""
    for char in word:
        result = char + result
    return result

def is_palindrome(word):
    # TODO: คืน True ถ้า word เท่ากับ word กลับหลัง
    return word == ____   # 👈 reverse(word)


# ทดสอบ
print("madam   ->", is_palindrome("madam"))     # True
print("racecar ->", is_palindrome("racecar"))   # True
print("hello   ->", is_palindrome("hello"))     # False

# ───────────────────────────────────────────────────────────
# ── PART B (5 นาที): SHARE รหัสลับ ─────────────────────────
#
#  1. เปิดโปรแกรมเข้ารหัสลับ (Mini) ใน Trinket
#  2. กด Share -> copy link
#  3. ส่งให้คนสำคัญใน LINE + ข้อความที่เข้ารหัสแล้ว:
#     "ลองถอดรหัสนี้ดูสิ! หนูเขียนโปรแกรมเข้ารหัสเองนะ 🔐"
#
# ✅ เกณฑ์เสร็จ:
#   - Part A is_palindrome ถูกทั้ง 3 คำ
#   - Part B ส่ง link + ข้อความเข้ารหัสจริง + คนสำคัญตอบกลับ
