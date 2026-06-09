# F1 · Session 10 — Workshop Day 2 + PyGame

> รวม logic ทุกอย่าง S1-9 + เล่น PyGame template ใหญ่ขึ้น (Flappy Bird!) → deploy ให้พ่อแม่เล่นบนมือถือ

---

## 🎯 วันนี้เด็กจะทำได้

- รวม if-elif + and + for + random ในโจทย์จริง
- แก้ PyGame template ที่ใหญ่ขึ้น (Flappy Bird)
- คุมตัวแปรหลายตัวพร้อมกัน
- Deploy Replit รอบ 2 (เร็วขึ้น)

> ✨ ไม่มี tool ใหม่ (Pygame/Replit จาก SS5)

---

## 📂 ไฟล์ใน Workshop นี้

| ไฟล์ | ใช้ตอน | เด็กทำอะไร |
|---|---|---|
| `workshop_01_age_category.py` | W1 (20 นาที) | if-elif จัดกลุ่มอายุ |
| `workshop_02_flappy_bird_TEMPLATE.py` | W2 (20 นาที) | แก้ CONFIG Flappy Bird → deploy |
| `mini_age_height_verifier.py` | Mini (15 นาที) | if + and (2 เงื่อนไข) |
| `project_dice_battle.py` | Project (20 นาที) | Dice Battle เด็ก vs คอม (Best of 3) |
| `hw1_lucky_words.py` | HW1 (บังคับ) | random.choice × 3 |
| `hw2_pin_generator.py` | HW2 (เก่ง) | random.randint × 4 (PIN) |

> ไฟล์ที่มี `# TODO` / `CONFIG` คือจุดที่เด็กแก้ · HW3 = แชร์ Flappy Bird บน Replit

---

## 🔑 Key Patterns

```python
# if-elif หลายช่วง
if age < 13: ...
elif age < 20: ...
else: ...

# and — ต้องจริงทั้งคู่
if age >= 18 and height >= 150: ...

# Flappy Bird — เด็กแก้แค่ CONFIG
GRAVITY = 0.5   # 👈 ปรับความยาก
```

---

## 🤖 AI Policy

Workshop/HW1 ❌ · HW2 ⚠️ หลังลองเอง · HW3 ✅ · debug ✅ (เล่าให้ครูฟัง)

---

## ⏱️ ถ้าเกินเวลา

1. ตัด **W1 (Age Category)** ก่อน
2. รักษา **W2 Flappy Bird + deploy** ไว้ — moment สำคัญ (เด็กมีเกมโชว์)
3. ❌ ห้ามตัด recap + parent reminder
