# ═══════════════════════════════════════════════════════════
# ⭐ HW2 (เก่ง · optional) · รหัสซีซาร์ (Caesar Cipher)
# F2 Session 09 · String Methods  ·  ~30 นาที
# ═══════════════════════════════════════════════════════════
#
# 🎯 Challenge: 2 function เข้ารหัส/ถอดรหัส (เลื่อน 3 ตำแหน่ง)
# 💡 Hint: chr(ord(char) + 3) เพื่อเลื่อนตัวอักษร
#          encrypt แล้ว decrypt ต้องได้ข้อความเดิม
# ───────────────────────────────────────────────────────────

def encrypt(text):
    result = ""
    for char in text:
        result = result + chr(ord(char) + 3)
    return result

def decrypt(text):
    result = ""
    for char in text:
        # TODO: เลื่อนกลับ -3
        result = result + ____   # 👈 chr(ord(char) - 3)
    return result


# ───────────────────────────────────────────────────────────
secret = encrypt("abc")
print("เข้ารหัส 'abc' ->", secret)        # def
print("ถอดรหัสกลับ   ->", decrypt(secret)) # abc

# ✨ ส่งข้อความลับให้เพื่อน! (ให้เพื่อนใช้ decrypt ถอด)
my_msg = input("\nพิมพ์ข้อความที่จะส่งลับ: ")
print("ส่งรหัสนี้ให้เพื่อน:", encrypt(my_msg))
