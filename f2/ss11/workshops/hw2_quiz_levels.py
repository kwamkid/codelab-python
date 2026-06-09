# ═══════════════════════════════════════════════════════════
# ⭐ HW2 (เก่ง · optional) · Quiz Levels — Easy/Medium/Hard
# F2 Session 11 · Mini Project Build  ·  30 นาที
# ═══════════════════════════════════════════════════════════
# 🎯 กรองคำถามตามระดับความยาก (for + if)
# ───────────────────────────────────────────────────────────

questions = [
    {"q": "1+1?", "answer": "2", "level": "easy"},
    {"q": "12 x 12?", "answer": "144", "level": "hard"},
    {"q": "7 x 8?", "answer": "56", "level": "medium"},
    {"q": "2+2?", "answer": "4", "level": "easy"},
]

def pick_question(level):
    result = []
    for item in questions:
        # TODO: เก็บเฉพาะข้อที่ level ตรงกับที่เลือก
        if item["level"] == ____:      # 👈 แก้: level
            result.append(item)
    return result

chosen = input("เลือกระดับ (easy/medium/hard): ")
quiz = pick_question(chosen)
print(f"มี {len(quiz)} ข้อระดับ {chosen}")
for item in quiz:
    print("-", item["q"])
