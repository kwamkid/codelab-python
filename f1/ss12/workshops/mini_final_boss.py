# ═══════════════════════════════════════════════════════════
# 🎮 ด่าน 3 · FINAL BOSS — รวมทุกหัวข้อ Level 1 (20 นาที)
# F1 Session 12 · Grand Showcase
# ═══════════════════════════════════════════════════════════
# ⚠️ เขียนเอง! รวม variable + input + math + if + for + random + list
#    พิสูจน์ว่าเป็น "Coder" ตัวจริง — ห้าม AI ครูดูอยู่
# ───────────────────────────────────────────────────────────
#
# 📋 SPEC — "Lucky Number Game"
#   1. มี list ของรางวัล 5 ชิ้น (list)
#   2. ให้ผู้เล่นทายเลข 1-5 (input + int)
#   3. สุ่มเลขลับ 1-5 (random)
#   4. for วน 3 รอบ ให้ทาย (for)
#   5. ถ้าทายถูก → ได้รางวัลจาก list ตามเลข (if + list)
#   6. print ผลลัพธ์
#
# 💡 ใช้: list · input · random · for · if · f-string

import random

prizes = ["🍫", "✏️", "📚", "🎮", "🎁"]
secret = random.randint(1, 5)

# เริ่มเขียนด้านล่างนี้ (เขียนเอง!):
for round in range(1, 4):
    guess = int(input(f"รอบ {round} — ทายเลข 1-5: "))
    if guess == secret:
        print(f"🎉 ถูก! ได้รางวัล {prizes[secret - 1]}")
        break
    else:
        print("ยังไม่ใช่ ลองใหม่!")
