# F1 · Session 09 — 🐛 Review & Bug Hunt

> Programmer ตัวจริงใช้เวลา **50% ไปกับ debug!** — อ่าน error ได้ = ช่วยตัวเองได้ทันที · รู้จัก VS Code Debugger

---

## 🎯 วันนี้เด็กจะทำได้

- อ่าน **error message** เป็น
- แยก **SyntaxError / NameError / TypeError / IndentationError**
- ใช้ **VS Code Debugger** (breakpoint + step) หา bug
- แก้ bug ในโค้ดคนอื่นได้

> ✨ Tool ใหม่: **VS Code Debugger** (built-in — กด F5, ไม่ต้องลงอะไรเพิ่ม)

---

## 🐞 4 Error ที่เจอบ่อย

| Error | แปลว่า | ตัวอย่าง |
|---|---|---|
| **SyntaxError** | เขียนผิดไวยากรณ์ | ลืม `:` ท้าย if / ลืมปิดวงเล็บ |
| **NameError** | ใช้ตัวแปรที่ไม่มี | พิมพ์ชื่อตัวแปรผิด (`naem`) |
| **TypeError** | ชนิดข้อมูลไม่เข้ากัน | `"5" + 3` |
| **IndentationError** | ย่อหน้าผิด | ลืมย่อหน้าใต้ `for` / `if` |

---

## 📂 ไฟล์ใน Workshop นี้

| ไฟล์ | ใช้ตอน | เด็กทำอะไร |
|---|---|---|
| `workshop_01_spot_the_syntax.py` | W1 (20 นาที) | หา + แก้ NameError/Syntax/Indent |
| `workshop_02_type_fixer.py` | W2 (20 นาที) | แก้ TypeError (cast str↔int) |
| `mini_fix_the_quiz_TEMPLATE.py` | Mini (15 นาที) | หา bug ใน Quiz ด้วย Debugger |
| `project_debug_challenge.py` | Project (20 นาที) | แก้เครื่องคิดเงินทอนที่พัง |
| `hw1_bug_hunt.py` | HW1 (บังคับ) | แก้ 3 bug + ระบุชนิด error |
| `hw2_make_a_bug.py` | HW2 (เก่ง) | ออกข้อสอบ bug ให้เพื่อนแก้ |
| `hw3_before_after.md` | HW3 (โชว์พ่อแม่) | share quiz buggy + fixed |

> ทุกไฟล์มี `# 🐛 BUG` มาร์คจุดที่ต้องแก้ · จุด `____` คือที่เด็กเติม fix

---

## 🔍 VS Code Debugger (วิธีใช้)

1. คลิกซ้ายของเลขบรรทัด → จุดแดง (**breakpoint**)
2. กด **F5** → เลือก Python Debugger → รัน
3. โค้ดหยุดที่ breakpoint → ดู **Variables panel** (ซ้ายมือ)
4. **F10** = step over (ทีละบรรทัด) · **F11** = step into

---

## 🤖 AI Policy

| งาน | ใช้ AI ได้มั้ย |
|---|---|
| Workshop ในคลาส | ❌ ห้าม |
| HW1 (บังคับ) | ❌ ห้าม |
| HW2 (เก่ง) | ⚠️ หลังลองเอง 15 นาที |
| HW3 (โชว์พ่อแม่) | ✅ ได้ |
| **อ่าน error / debug** | ✅ ได้ (แต่เล่าให้ครูฟังว่า error บอกอะไร) |

---

## ⏱️ ถ้าเกินเวลา

1. ตัด **W2 (Type Fixer)** ก่อน
2. รักษา **Mini (Fix the Quiz + Debugger)** + **Project** ไว้ — แกนของ debugging
3. ❌ ห้ามตัด recap + parent reminder
