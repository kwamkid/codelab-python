# ═══════════════════════════════════════════════════════════
# 🏠 HW1 (บังคับ) · Whack-a-Mole V2 — for loop!
# F1 Session 07 · For Loops (Light)  ·  ~20 นาที
# ═══════════════════════════════════════════════════════════
# 🎯 เกมตีตุ่นจาก S5 — แต่คราวนี้ใช้ for loop วน 5 รอบ
#    (จากเดิม copy-paste 3 รอบ → ตอนนี้ loop เดียวจบ!)
# ❌ ห้ามใช้ AI
# ───────────────────────────────────────────────────────────

import random

score = 0

# TODO: วน round จาก 1 ถึง 5
for round in range(1, ____):     # 👈 แก้ตรงนี้: 6
    mole = random.randint(1, 3)
    guess = int(input(f"รอบ {round} — ตุ่นช่องไหน? (1-3): "))
    if guess == mole:
        score += 1
        print("ตี! +1 🔨")
    else:
        print(f"พลาด! ตุ่นอยู่ช่อง {mole}")

print(f"\n🎉 คะแนนรวม: {score}/5")
