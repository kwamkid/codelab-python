# ═══════════════════════════════════════════════════════════
# 🎨 Project · Quiz เรื่องที่ชอบ — เกมเต็มของหนู!
# F2 Session 11 · Mini Project Build  ·  รวมทุกอย่าง S1-9
# ═══════════════════════════════════════════════════════════
# 🎯 Quiz 10 ข้อ เรื่องที่หนูสนใจ (เกม/การ์ตูน/กีฬา)
#    Logic + content = ของเด็ก · → deploy ขึ้น Replit
# 💡 เวอร์ชัน console (รันง่าย) — ต่อยอดเป็น CTk จาก Mini ได้
# ───────────────────────────────────────────────────────────

# TODO: เปลี่ยนเป็นคำถามเรื่องที่หนูชอบ (อย่างน้อย 5 ข้อ)
questions = [
    {"q": "ตัวเอกใน Minecraft ชื่อ?", "choices": ["Steve", "Mario", "Sonic"], "answer": "Steve"},
    {"q": "สีของ Pikachu?", "choices": ["แดง", "เหลือง", "ฟ้า"], "answer": "เหลือง"},
    {"q": "กีฬาที่ใช้แร็กเกต?", "choices": ["ฟุตบอล", "แบดมินตัน", "ว่ายน้ำ"], "answer": "แบดมินตัน"},
]

score = 0
print("🧠 QUIZ เรื่องที่ชอบ — ตอบให้ถูก!\n")

for i, item in enumerate(questions, start=1):
    print(f"ข้อ {i}: {item['q']}")
    for c in item["choices"]:
        print(f"   - {c}")
    pick = input("ตอบ: ")
    if pick == item["answer"]:
        print("✓ ถูก!\n")
        score += 1
    else:
        print(f"✗ ผิด (เฉลย: {item['answer']})\n")

print(f"🎉 จบเกม! คะแนน {score}/{len(questions)}")
