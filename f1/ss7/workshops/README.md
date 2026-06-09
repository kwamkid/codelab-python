# F1 · Session 07 — 🔁 For Loops (Light)

> ทำซ้ำ 100 รอบ ไม่ต้องเขียน 100 บรรทัด! — รู้จัก `for` + `range()` (แบบ light: ยังไม่มี while/break/continue/step)

---

## 🎯 วันนี้เด็กจะทำได้

- ใช้ `for i in range(n)` ทำซ้ำอัตโนมัติ
- เข้าใจ `range(start, stop)`
- เข้าใจว่า **ทำไมต้องมี loop** (ขี้เกียจ copy-paste = ดี!)
- ท่องสูตรคูณ + ทอยลูกเต๋าด้วยโค้ด

> ✨ ไม่มี tool ใหม่ · ปูทาง loop ขั้นลึกใน F2

---

## 📂 ไฟล์ใน Workshop นี้

| ไฟล์ | ใช้ตอน | เด็กทำอะไร |
|---|---|---|
| `workshop_01_count_up.py` | W1 (20 นาที) | `for i in range(1,6)` นับ 1→5 |
| `workshop_02_times_table.py` | W2 (20 นาที) | สูตรคูณ เลือกแม่ได้ (for) |
| `mini_number_display_TEMPLATE.py` | Mini (15 นาที) | CTk slider → print 1 ถึง N |
| `project_dice_roll.py` | Project (20 นาที) | ทอยเต๋า 10 ครั้ง + รวมคะแนน (accumulator) |
| `hw1_whack_a_mole_v2.py` | HW1 (บังคับ) | Whack-a-Mole จาก S5 → ใช้ loop แทน copy-paste |
| `hw2_fizzbuzz.py` | HW2 (เก่ง) | FizzBuzz 1-30 (for + if) |

> ไฟล์ที่มี `# TODO` คือจุดที่เด็กเติม · HW3 = แข่งทอยลูกเต๋ากับพ่อแม่ (`project_dice_roll.py`)

---

## 🔑 Key Patterns

```python
# วนซ้ำ n รอบ
for i in range(1, 6):    # i = 1,2,3,4,5 (ไม่รวม 6!)
    print(i)

# accumulator — เก็บผลรวม
total = 0
for i in range(1, 11):
    total = total + i    # บวกสะสม
```

> ⚠️ `range(1, 6)` ได้ 1-5 (ไม่รวมตัวท้าย) — เด็กพลาดบ่อย!

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

1. ตัด **W2 (Times Table)** ก่อน
2. รักษา **W1 (Count Up)** + **Project (Dice Roll)** ไว้ — แกนของ for loop
3. ❌ ห้ามตัด recap + parent reminder
