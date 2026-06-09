# F2 · Session 08 — ✨ Functions ทำทีเดียวจบ! + Multi-file

> เฉลย "ความเหนื่อย" จาก S7 — เอาโค้ดซ้ำๆ มาห่อด้วย `function` เหลือนิดเดียว

---

## 🎯 วันนี้เด็กจะทำได้

- เขียน `def` + parameters + `return`
- ใช้ `default parameters` (เช่น `pi=3.14`)
- แยกโค้ดเป็นหลายไฟล์ — `from my_tools import ...`
- เข้าใจ **DRY** (Don't Repeat Yourself)

---

## 📂 ไฟล์ใน Workshop นี้

| ไฟล์ | ใช้ตอน | เด็กทำอะไร |
|---|---|---|
| `workshop_01_calc_price.py` | W1 (20 นาที) | เอาโค้ดร้านน้ำ S7 มาเขียนเป็น `calc_price()` |
| `workshop_02_grade_function.py` | W2 (20 นาที) | `get_grade(score)` → return เกรดหลายทาง |
| `mini_unit_converter_TEMPLATE.py` | Mini (15 นาที) | CTk GUI — เติมแค่ function แปลงหน่วย |
| `project_room_area/my_tools.py` | Project (20 นาที) | กล่อง function คำนวณพื้นที่ |
| `project_room_area/main.py` | Project | import จาก `my_tools.py` → วัดห้องจริง |
| `hw1_money_converter.py` | HW1 (บังคับ) | 2 function บาท↔USD |
| `hw2_bmi_function.py` | HW2 (เก่ง) | BMI + เรียก function ซ้อน |
| `hw3_menu_rewrite.py` | HW3 (ทุกคน) | เขียนเมนู 5 จาน S7 ใหม่ + share เทียบเก่า/ใหม่ |

> ไฟล์ที่มี `# TODO` คือจุดที่เด็กต้องเติมเอง

---

## 🔑 Key Patterns

```python
# โครงสร้าง function
def ชื่อ(parameter):     # ทางเข้า
    ผลลัพธ์ = ...
    return ผลลัพธ์        # ทางออก

# เรียกใช้
คำตอบ = ชื่อ(ค่าที่ส่งเข้า)

# default parameter
def area_circle(radius, pi=3.14):
    return pi * radius * radius

# แยกไฟล์ (multi-file)
# ── ใน main.py ──
from my_tools import area_rectangle
```

---

## 🤖 AI Policy (ChatGPT / Copilot)

| งาน | ใช้ AI ได้มั้ย |
|---|---|
| Workshop ในคลาส (W1/W2/Mini/Project) | ❌ ห้าม |
| HW1 (บังคับ) | ❌ ห้าม |
| HW2 (เก่ง) | ⚠️ ใช้ได้ *หลัง* ลองเอง 15 นาที + อธิบายโค้ดได้ |
| HW3 (โชว์พ่อแม่) | ✅ ใช้ได้ (เน้น share) |
| debug error | ✅ ใช้ได้ แต่เล่าให้ครูฟังว่าถามอะไร |

---

## ⏱️ ถ้าเกินเวลา — ตัดอะไรก่อน

1. ตัด **W2 (Grade Function)** ก่อน
2. รักษา **W1 (Calc Price)** ไว้เสมอ — มันคือ payoff ของ S7
3. ❌ ห้ามตัด recap + parent reminder (5 นาทีสุดท้าย)
