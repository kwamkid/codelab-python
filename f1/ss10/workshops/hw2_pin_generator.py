# ═══════════════════════════════════════════════════════════
# ⭐ HW2 (เก่ง · optional) · 4-Digit PIN Generator
# F1 Session 10 · Workshop Day 2  ·  ~30 นาที
# ═══════════════════════════════════════════════════════════
# 🎯 สุ่มรหัส PIN 4 หลัก (random.randint × 4)
# ───────────────────────────────────────────────────────────

import random

d1 = random.randint(0, 9)
d2 = random.randint(0, 9)
d3 = random.randint(0, 9)
# TODO: หลักที่ 4
d4 = random.randint(0, ____)      # 👈 แก้: 9

pin = f"{d1}{d2}{d3}{d4}"
print(f"🔐 PIN ของคุณ: {pin}")

# ✅ รันใหม่ → ได้ PIN ใหม่ทุกครั้ง
