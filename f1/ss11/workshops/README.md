# F1 · Session 11 — Mini Project: Text Adventure

> รวมความรู้ทั้งหมด S1-10 → เขียน **เกมผจญภัยเลือกเส้นทาง** (5 ฉาก, 3 ตอนจบ) ของตัวเอง!

---

## 🎯 วันนี้เด็กจะทำได้

- วาด **flowchart** ก่อนเขียนโค้ด (วางแผน)
- เขียนเกมผจญภัย 5 ฉาก + 2-3 ตอนจบ
- ใช้ **if-else chain ยาวๆ** ตามการเลือก
- ใช้ `time.sleep()` เพิ่ม dramatic pause

> ✨ Tool ใหม่: **`time`** (Python built-in — `import time` → `time.sleep(1.5)`)

---

## 📂 ไฟล์ใน Workshop นี้

| ไฟล์ | ใช้ตอน | เด็กทำอะไร |
|---|---|---|
| `workshop_01_story_planning.py` | W1 (20 นาที) | วาด flowchart เรื่อง (วางแผน) |
| `workshop_02_scene1.py` | W2 (20 นาที) | ฉากเปิด + ทางเลือก (if-else) |
| `mini_multiple_endings.py` | Mini (15 นาที) | ตอนจบ 2-3 แบบ |
| `project_the_adventure.py` | Project (20 นาที) | RPG เต็ม 5 ฉาก 3 จบ → deploy |
| `hw1_decorate_story.py` | HW1 (บังคับ) | ตกแต่งด้วย time.sleep + emoji |
| `hw2_presentation_prep.md` | HW2 (เก่ง) | เตรียม present สำหรับ SS12 |

> ไฟล์ที่มี `# TODO` คือจุดที่เด็กเติม · HW3 = แชร์เกมบน Replit ให้พ่อแม่เลือกทางเล่น

---

## 🔑 Key Patterns

```python
import time

print("เปิดประตู...")
time.sleep(1.5)        # หยุด 1.5 วินาที (ลุ้น!)
print("เจอมังกร! 🐉")

choice = input("สู้ หรือ หนี: ")
if choice == "สู้":
    ...
else:
    ...
```

---

## 🤖 AI Policy
Workshop/HW1 ❌ · HW2 (present prep) ✅ ช่วยจัดได้ · HW3 ✅ · debug ✅

## ⏱️ ถ้าเกินเวลา
1. ลด project เหลือ 3 ฉาก 2 จบ
2. รักษา **flowchart + Project + deploy** ไว้
3. ❌ ห้ามตัด recap + parent reminder
