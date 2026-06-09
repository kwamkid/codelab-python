# ═══════════════════════════════════════════════════════════
# 🎲 Project · Dice Roll Simulator — for + random + accumulator
# F1 Session 07 · For Loops (Light)  ·  20 นาที
# ═══════════════════════════════════════════════════════════
# 🎯 ทอยลูกเต๋า 10 ครั้งด้วย loop → รวมคะแนนทั้งหมด
#    → Deploy ขึ้น Replit ได้ (ต่อจาก S5)
# ───────────────────────────────────────────────────────────

import random

total = 0
print("🎲 ทอยลูกเต๋า 10 ครั้ง!")

for i in range(1, 11):
    roll = random.randint(1, 6)
    print(f"รอบ {i}: ทอยได้ {roll}")
    # TODO: บวก roll เข้า total (accumulator)
    total = ____      # 👈 แก้ตรงนี้: total + roll

print(f"\n🏆 คะแนนรวม 10 รอบ: {total}")
