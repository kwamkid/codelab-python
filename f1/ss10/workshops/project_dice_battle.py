# ═══════════════════════════════════════════════════════════
# 🎲 Project · Dice Battle (Best of 3) — เด็ก vs คอม
# F1 Session 10 · Workshop Day 2  ·  20 นาที
# ═══════════════════════════════════════════════════════════
# 🎯 ทอย 3 ครั้ง รวมแต้ม → ใครมากกว่าชนะ (for + random + if)
# ───────────────────────────────────────────────────────────

import random

me = 0
cpu = 0

for round in range(1, 4):
    my_roll = random.randint(1, 6)
    cpu_roll = random.randint(1, 6)
    print(f"รอบ {round}: เรา {my_roll} | คอม {cpu_roll}")
    me = me + my_roll
    # TODO: บวกแต้มคอม
    cpu = ____            # 👈 แก้: cpu + cpu_roll

print(f"\nแต้มรวม — เรา {me} : คอม {cpu}")
if me > cpu:
    print("🏆 เราชนะ!")
elif me < cpu:
    print("😢 คอมชนะ")
else:
    print("🤝 เสมอ!")
