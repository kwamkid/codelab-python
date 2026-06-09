# F2 · Session 09 — String Methods + Loops

> จัดการ "ข้อความ" เป็น — วน string, แปลงตัวพิมพ์, แยกคำ, เข้ารหัส/ถอดรหัส

---

## 🎯 วันนี้เด็กจะทำได้

- วน string ด้วย `for char in text`
- ใช้ `upper()`, `lower()`, `replace()`
- ใช้ `split()`, `join()`
- เขียน/ถอดรหัสลับด้วย `chr()` / `ord()`

> ต่อยอดจาก S8: ใช้ `def` ห่อ logic การนับ/แปลง

---

## 📂 ไฟล์ใน Workshop นี้

| ไฟล์ | ใช้ตอน | เด็กทำอะไร |
|---|---|---|
| `workshop_01_count_vowels.py` | W1 (20 นาที) | วน `for char` นับสระในชื่อ |
| `workshop_02_reverse_word.py` | W2 (20 นาที) | `reverse(word)` ด้วย `char + result` |
| `mini_secret_code_TEMPLATE.py` | Mini (15 นาที) | CTk GUI — เติม encode/decode |
| `project_chat_analyzer.py` | Project (20 นาที) | นับคำ/สระ/ตัวเลข + คำยาวสุด |
| `hw1_char_counter.py` | HW1 (บังคับ) | นับ อักษร/ตัวเลข/เว้นวรรค |
| `hw2_caesar_cipher.py` | HW2 (เก่ง) | รหัสซีซาร์ encrypt/decrypt |
| `hw3_palindrome.py` | HW3 (ทุกคน) | เช็คคำอ่านกลับ + ส่งรหัสลับ |

> ไฟล์ที่มี `# TODO` คือจุดที่เด็กต้องเติมเอง

---

## 🔑 Key Patterns

```python
# วน string ทีละตัว
for char in "CodeLab":
    print(char)

# string methods
text.upper()              # ตัวพิมพ์ใหญ่
text.replace("a", "@")    # แทนที่
text.split()              # แยกเป็น list ของคำ

# เช็คชนิดตัวอักษร
char.isdigit()    # ตัวเลขไหม
char.isalpha()    # ตัวอักษรไหม

# เข้ารหัส (เลื่อนตัวอักษร)
chr(ord(char) + 3)
```

---

## 🤖 AI Policy (ChatGPT / Copilot)

| งาน | ใช้ AI ได้มั้ย |
|---|---|
| Workshop ในคลาส (W1/W2/Mini/Project) | ❌ ห้าม |
| HW1 (บังคับ) | ❌ ห้าม |
| HW2 (เก่ง) | ⚠️ ใช้ได้ *หลัง* ลองเอง 15 นาที + อธิบายได้ |
| HW3 (โชว์พ่อแม่) | ✅ ใช้ได้ (เน้น share) |
| debug error | ✅ ใช้ได้ แต่เล่าให้ครูฟังว่าถามอะไร |

---

## ⏱️ ถ้าเกินเวลา — ตัดอะไรก่อน

1. ตัด **W2 (กลับคำ)** ก่อน
2. รักษา **W1 (นับสระ)** + **Project (Chat Analyzer)** ไว้
3. ❌ ห้ามตัด recap + parent reminder (5 นาทีสุดท้าย)
