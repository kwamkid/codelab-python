# ═══════════════════════════════════════════════════════════
# 🏠 HW1 (บังคับ) · Quiz Shuffle — เพิ่ม 10 ข้อ + random.shuffle
# F2 Session 11 · Mini Project Build  ·  30 นาที
# ═══════════════════════════════════════════════════════════
# 🎯 ทำให้ Quiz สุ่มลำดับข้อไม่ซ้ำกันทุกรอบ (เน้น data + logic)
# ❌ ห้ามใช้ AI
# ───────────────────────────────────────────────────────────

import random

questions = [
    {"q": "1+1?", "answer": "2"},
    {"q": "สีกล้วยสุก?", "answer": "เหลือง"},
    {"q": "ดาวที่เราอยู่?", "answer": "โลก"},
    # ... เพิ่มให้ครบ 10 ข้อ
]

# TODO: สลับลำดับข้อแบบสุ่ม (ไม่ซ้ำเดิม)
random.shuffle(____)        # 👈 แก้: questions

score = 0
for item in questions:
    pick = input(item["q"] + " ")
    if pick == item["answer"]:
        score += 1
print(f"คะแนน {score}/{len(questions)} · รันใหม่ → ลำดับเปลี่ยน!")
