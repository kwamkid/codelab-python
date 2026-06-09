# ═══════════════════════════════════════════════════════════
# 🐛 Mini · Fix the Quiz! — หา 5 bug ด้วย VS Code Debugger
# F1 Session 09 · Review & Bug Hunt
# ═══════════════════════════════════════════════════════════
# 🎯 โปรแกรม Quiz นี้มี bug 5 จุด! ใช้ Debugger หา + แก้
#    💡 วาง breakpoint (จุดแดงข้างเลขบรรทัด) → กด F5 → ดู Variables
# ───────────────────────────────────────────────────────────

print("🧠 Math Quiz — ตอบให้ถูก!")

score = 0

# 🐛 BUG 1 — input ได้ str ต้อง int() ก่อนเทียบ
answer1 = int(input("2 + 3 = ? "))
if answer1 == 5:
    score = score + 1
    print("✓ ถูก!")
else:
    print("✗ ผิด")

# 🐛 BUG 2 — ใช้ = แทน == (ต้องเทียบด้วย ==)
answer2 = int(input("10 - 4 = ? "))
if answer2 == 6:          # 👈 เทียบใช้ == ไม่ใช่ =
    score = score + 1
    print("✓ ถูก!")

# 🐛 BUG 3 — ชื่อตัวแปรต้องตรงกัน (score ไม่ใช่ scor)
print(f"คะแนนรวม: {____} / 2")     # 👈 แก้: score

# ✅ แก้ครบ → quiz รันได้ + นับคะแนนถูก
