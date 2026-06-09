# ═══════════════════════════════════════════════════════════
# 🎮 ด่าน 3 · FINAL BOSS L2 — รวมทุกหัวข้อ Level 2
# F2 Session 12 · Grand Showcase Level 2
# ═══════════════════════════════════════════════════════════
# ⚠️ เขียนเอง! รวม list + loop + function + string ของ Level 2
#    ห้าม AI · ครูดูอยู่
# ───────────────────────────────────────────────────────────
#
# 📋 SPEC — "Word Stats"
#   1. มี list ของคำ 5 คำ (list)
#   2. function analyze(word) → return จำนวนตัวอักษร (function+len)
#   3. for วนทุกคำ → print คำ + จำนวนตัวอักษร (loop)
#   4. หาคำที่ยาวที่สุด (if + compare)
#
# 💡 ใช้: list · function · for · len · if

words = ["python", "code", "developer", "fun", "lab"]

def analyze(word):
    return len(word)

longest = ""
for w in words:
    print(f"{w} → {analyze(w)} ตัวอักษร")
    if len(w) > len(longest):
        longest = w

print(f"\nคำที่ยาวที่สุด: {longest}")
