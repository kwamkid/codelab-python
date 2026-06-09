# ═══════════════════════════════════════════════════════════
# 🔨 Project · Whack-a-Mole V1 — random + if (3 รอบ ไม่ใช้ loop)
# F1 Session 05 · Workshop Day  ·  20 นาที
# ═══════════════════════════════════════════════════════════
# 🎯 เกมตีตุ่น — ตุ่นสุ่มโผล่ช่อง 1-3 ทายให้ถูก!
#    เขียน 3 รอบแบบ copy-paste (loop จะเรียนใน F2)
#    → Deploy ขึ้น Replit → ได้ public link
# ───────────────────────────────────────────────────────────

import random

print("🔨 Whack-a-Mole V1 — ตี 3 รอบ!")
score = 0

# ── รอบ 1 ──
mole = random.randint(1, 3)
guess = int(input("รอบ 1 — ตุ่นอยู่ช่องไหน? (1-3): "))
if guess == mole:
    print("ตี! +1 🔨"); score += 1
else:
    print(f"พลาด! ตุ่นอยู่ช่อง {mole}")

# ── รอบ 2 (TODO: copy รอบ 1 มาแก้) ──
mole = random.randint(1, 3)
guess = int(input("รอบ 2 — ตุ่นอยู่ช่องไหน? (1-3): "))
if guess == mole:
    # TODO: ตีถูก +1
    print("ตี! +1 🔨"); score = ____   # 👈 แก้ตรงนี้: score + 1
else:
    print(f"พลาด! ตุ่นอยู่ช่อง {mole}")

# ── รอบ 3 ──
mole = random.randint(1, 3)
guess = int(input("รอบ 3 — ตุ่นอยู่ช่องไหน? (1-3): "))
if guess == mole:
    print("ตี! +1 🔨"); score += 1
else:
    print(f"พลาด! ตุ่นอยู่ช่อง {mole}")

print(f"\n🎉 คะแนนรวม: {score}/3")
