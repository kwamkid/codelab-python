# ═══════════════════════════════════════════════════════════
# 🎨 Mini · Quiz UI — CustomTkinter Template (เชื่อม logic)
# F2 Session 11 · Mini Project Build
# ═══════════════════════════════════════════════════════════
# 🎯 ครูเตรียม UI ให้ — เด็กเอา logic จาก W2 มาเชื่อมใต้ปุ่ม
# ❌ ห้ามแตะ UI scaffold (ส่วนสร้างหน้าต่าง/ปุ่ม)
# ───────────────────────────────────────────────────────────

questions = [
    {"q": "2 + 3 = ?", "choices": ["4", "5", "6"], "answer": "5"},
    {"q": "สีของท้องฟ้า?", "choices": ["แดง", "ฟ้า", "เขียว"], "answer": "ฟ้า"},
]
score = 0
current = 0

def on_pick(pick):
    global score, current
    # TODO: เช็คคำตอบ + เพิ่มคะแนน + ไปข้อต่อไป
    if pick == questions[current]["answer"]:
        score += 1
    current += 1
    if current < len(questions):
        show_question()
    else:
        q_label.configure(text=f"จบเกม! คะแนน {score}/{len(questions)} 🎉")
        for b in btns: b.configure(state="disabled")
# ───────────────────────────────────────────────────────────


# ❌ ห้ามแตะ UI scaffold ด้านล่าง (ครูเตรียมให้)
import customtkinter as ctk
ctk.set_appearance_mode("light")
app = ctk.CTk(); app.title("🧠 Quiz Game"); app.geometry("420x340")
q_label = ctk.CTkLabel(app, text="", font=("IBM Plex Sans Thai", 22), wraplength=380)
q_label.pack(pady=24)
btns = [ctk.CTkButton(app, text="", width=260, command=lambda i=i: on_pick(btns[i].cget("text"))) for i in range(3)]
for b in btns: b.pack(pady=6)

def show_question():
    q = questions[current]
    q_label.configure(text=q["q"])
    for i, c in enumerate(q["choices"]):
        btns[i].configure(text=c)

show_question()
app.mainloop()
