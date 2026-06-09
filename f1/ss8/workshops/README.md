# F1 · Session 08 — 📋 Lists (Light)

> เก็บของเป็น "ชุด" ในตัวแปรเดียว แทนการสร้างตัวแปร 5 ตัว — รู้จัก `list`, `append`, `remove`, `random.choice()`

---

## 🎯 วันนี้เด็กจะทำได้

- สร้าง `list = []` เก็บของหลายชิ้น
- เพิ่ม `.append()` / ลบ `.remove()` / นับ `len()`
- `print(list)` ดูทั้งหมด
- `random.choice(list)` สุ่มเลือก 1 ชิ้น

> ✨ ไม่มี tool ใหม่ · **LIGHT:** ยังไม่มี index, slicing, loop+list (เรียนใน F2)

---

## 📂 ไฟล์ใน Workshop นี้

| ไฟล์ | ใช้ตอน | เด็กทำอะไร |
|---|---|---|
| `workshop_01_shopping_list.py` | W1 (20 นาที) | สร้าง list + append/remove/len |
| `workshop_02_random_picker.py` | W2 (20 นาที) | `random.choice()` สุ่มเมนู |
| `mini_lucky_pick_TEMPLATE.py` | Mini (15 นาที) | CTk ปุ่ม "สุ่ม!" → สุ่มรางวัล |
| `project_decision_maker.py` | Project (20 นาที) | รับ 5 ตัวเลือก → สุ่มตัดสินใจ |
| `hw1_playlist_manager.py` | HW1 (บังคับ) | เพิ่ม/ลบ/สุ่มเพลง จาก list |
| `hw2_random_story.py` | HW2 (เก่ง) | 3 lists สุ่มแต่งเรื่อง (ปูพื้น F2) |

> ไฟล์ที่มี `# TODO` คือจุดที่เด็กเติม · HW3 = ส่ง Decision Maker ให้พ่อแม่ใช้เลือกเมนูเย็น

---

## 🔑 Key Patterns

```python
fruits = []                 # list ว่าง
fruits.append("แอปเปิล")    # เพิ่ม
fruits.remove("แอปเปิล")    # ลบ
len(fruits)                 # นับจำนวน
print(fruits)               # ดูทั้งหมด

import random
random.choice(fruits)       # สุ่มเลือก 1 ชิ้น
```

---

## 🤖 AI Policy

| งาน | ใช้ AI ได้มั้ย |
|---|---|
| Workshop ในคลาส | ❌ ห้าม |
| HW1 (บังคับ) | ❌ ห้าม |
| HW2 (เก่ง) | ⚠️ หลังลองเอง 15 นาที + อธิบายได้ |
| HW3 (โชว์พ่อแม่) | ✅ ได้ |
| debug | ✅ ได้ แต่เล่าให้ครูฟัง |

---

## ⏱️ ถ้าเกินเวลา

1. ตัด **W2 (Random Picker)** ก่อน
2. รักษา **W1 (Shopping List)** + **Project (Decision Maker)** ไว้
3. ❌ ห้ามตัด recap + parent reminder
