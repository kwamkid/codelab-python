# F1 · Session 05 — Workshop Day + PyGame Intro

> รวมทุกอย่าง S1-4 + รู้จัก **random** + **PyGame** (เกมจริง) + **Replit** (deploy ให้พ่อแม่เล่นบนมือถือ!)

---

## 🎯 วันนี้เด็กจะทำได้

- รวม variables + input + math + if-else ในโจทย์เดียว
- ใช้ `import random` → `random.randint()`, `random.choice()`
- แก้ **PyGame template** (ปรับ CONFIG) ให้เป็นเกมของตัวเอง
- Upload → Run → Share เกมบน **Replit** (public link)

---

## ✨ Tool ใหม่ 2 ตัว (ต้อง onboard ก่อน)

| Tool | คืออะไร | Setup | ฟรี? |
|---|---|---|---|
| **Pygame** | library สร้างเกม 2D (sprite, keyboard, animation) | `pip install pygame` ใน VS Code Terminal | ✅ |
| **Replit** | online IDE + deploy คลิกเดียว → public link | replit.com → Sign up → New Python Repl | ✅ |

> ⚠️ Replit: เด็กอายุ < 13 ใช้ email ผู้ปกครอง + **ผู้ปกครองยินยอม** (COPPA) — แจ้งล่วงหน้า 1 สัปดาห์

---

## 📂 ไฟล์ใน Workshop นี้

| ไฟล์ | ใช้ตอน | เด็กทำอะไร |
|---|---|---|
| `workshop_01_review_quiz.py` | W1 (20 นาที) | ตอบ quiz ทบทวน S1-4 |
| `workshop_02_smart_calculator.py` | W2 (20 นาที) | เลือก operation + คำนวณ (if + math) |
| `mini_dino_run_TEMPLATE.py` | Mini (15 นาที) | แก้ CONFIG PyGame → Upload Replit |
| `project_whack_a_mole.py` | Project (20 นาที) | เกมตีตุ่น 3 รอบ (random + if) → deploy |
| `hw1_shopping_cart_v3.py` | HW1 (บังคับ) | if + math: ส่วนลด + VAT |
| `hw2_lucky_dice.py` | HW2 (เก่ง) | ทอยลูกเต๋า (random.randint) |

> ไฟล์ที่มี `# TODO` / `CONFIG` คือจุดที่เด็กแก้เอง · HW3 = แชร์ Dino Run บน Replit ให้พ่อแม่เล่น

---

## 🔑 Key Patterns

```python
import random
random.randint(1, 6)      # สุ่มเลข 1-6 (ลูกเต๋า)
random.choice(["A","B"])  # สุ่มเลือกจาก list

# PyGame — เด็กแก้แค่ CONFIG ด้านบน
DINO_SPEED = 5            # 👈 ปรับตัวเลข
# (engine ห้ามแตะ)
```

---

## 🤖 AI Policy

| งาน | ใช้ AI ได้มั้ย |
|---|---|
| Workshop ในคลาส | ❌ ห้าม |
| HW1 (บังคับ) | ❌ ห้าม |
| HW2 (เก่ง) | ⚠️ ใช้ได้หลังลองเอง 15 นาที + อธิบายได้ |
| HW3 (โชว์พ่อแม่) | ✅ ใช้ได้ |
| debug | ✅ ใช้ได้ แต่เล่าให้ครูฟัง |

---

## ⏱️ ถ้าเกินเวลา

1. ตัด **W2 (Smart Calc)** ก่อน
2. รักษา **Mini Dino Run + deploy Replit** ไว้ — คือ moment สำคัญ (เด็กมีเกมออนไลน์ครั้งแรก)
3. ❌ ห้ามตัด recap + parent reminder
