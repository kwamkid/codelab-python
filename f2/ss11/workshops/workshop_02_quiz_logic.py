# ═══════════════════════════════════════════════════════════
# 🖥️ W2 · Quiz Logic Functions — list + function (จาก S1-9)
# F2 Session 11 · Mini Project Build
# ═══════════════════════════════════════════════════════════
# 🎯 เขียน "สมอง" ของเกม Quiz — data + functions
#    (UI ครูเตรียมให้ใน Mini — เราเขียน logic)
# ───────────────────────────────────────────────────────────

# DATA — list of dict (แต่ละข้อ = 1 dict)
questions = [
    {"q": "2 + 3 = ?", "choices": ["4", "5", "6"], "answer": "5"},
    {"q": "เมืองหลวงไทย?", "choices": ["เชียงใหม่", "กรุงเทพ", "ภูเก็ต"], "answer": "กรุงเทพ"},
]

score = 0
current = 0

def check_answer(pick):
    global score
    # TODO: ถ้า pick ตรงกับเฉลยของข้อปัจจุบัน → score +1
    if pick == questions[current]["answer"]:
        score = ____            # 👈 แก้: score + 1
        return "✓ ถูก!"
    return "✗ ผิด"

def next_question():
    global current
    current += 1

def show_score():
    return f"คะแนน: {score}/{len(questions)}"

# ───────────────────────────────────────────────────────────
# ทดสอบ logic (จำลองการเล่น)
print(questions[0]["q"])
print(check_answer("5"))      # ✓ ถูก!
next_question()
print(questions[1]["q"])
print(check_answer("กรุงเทพ"))  # ✓ ถูก!
print(show_score())           # คะแนน: 2/2
