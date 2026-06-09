# F1 · Session 04 — If-Else + Logic

> โปรแกรมเริ่ม "ตัดสินใจ" ได้ — รหัสถูก/ผิด, อายุพอซื้อตั๋วมั้ย (พื้นฐานของ AI ทุกตัว)

---

## 🎯 วันนี้เด็กจะทำได้

- เปรียบเทียบด้วย `==`, `!=`, `>`, `<` → ได้ True / False
- เขียน `if`, `if-else`, `if-elif-else`
- รวมเงื่อนไขด้วย `and`, `or`, `not`
- เข้าใจ **indentation** (ย่อหน้าสำคัญมากใน Python)

---

## 📂 ไฟล์ใน Workshop นี้

| ไฟล์ | ใช้ตอน | เด็กทำอะไร |
|---|---|---|
| `workshop_01_password_check.py` | W1 (20 นาที) | `if-else` เช็ครหัสถูก/ผิด |
| `workshop_02_ticket_price.py` | W2 (20 นาที) | `if-elif-else` ราคาตั๋วตามอายุ |
| `mini_magic_door_TEMPLATE.py` | Mini (15 นาที) | CTk GUI 3 ประตู → แก้ `check_door()` |
| `project_login_system.py` | Project (20 นาที) | `and` — user + password ถูกทั้งคู่ |
| `hw1_number_guessing.py` | HW1 (บังคับ) | ทายเลขครั้งเดียว (ยังไม่มี loop) |
| `hw2_discount_calculator.py` | HW2 (เก่ง) | ส่วนลดตามยอด (if-elif + math) |

> ไฟล์ที่มี `# TODO` คือจุดที่เด็กต้องเติมเอง · HW3 = ส่ง `hw1` ให้พ่อแม่ลองทาย

---

## 🔑 Key Patterns

```python
# เปรียบเทียบ → True / False
age >= 13          # True ถ้าอายุ 13 ขึ้นไป

# if / elif / else (ระวัง indentation + : )
if score >= 80:
    print("A")
elif score >= 70:
    print("B")
else:
    print("ตก")

# รวมเงื่อนไข
if user == "admin" and pw == "1234":   # ต้องจริงทั้งคู่
    print("เข้าได้")
```

---

## 🤖 AI Policy

| งาน | ใช้ AI ได้มั้ย |
|---|---|
| Workshop ในคลาส (W1/W2/Mini/Project) | ❌ ห้าม |
| HW1 (บังคับ) | ❌ ห้าม |
| HW2 (เก่ง) | ⚠️ ใช้ได้ *หลัง* ลองเอง 15 นาที + อธิบายได้ |
| HW3 (โชว์พ่อแม่) | ✅ ใช้ได้ |
| debug error | ✅ ใช้ได้ แต่เล่าให้ครูฟัง |

---

## ⏱️ ถ้าเกินเวลา — ตัดอะไรก่อน

1. ตัด **W2 (Ticket Price)** ก่อน
2. รักษา **W1 (Password)** + **Project (Login)** ไว้ — แกนของ if-else
3. ❌ ห้ามตัด recap + parent reminder (5 นาทีสุดท้าย)
