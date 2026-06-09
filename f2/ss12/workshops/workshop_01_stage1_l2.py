# ═══════════════════════════════════════════════════════════
# 🎤 ด่าน 1 · Lists + Loops — Showcase L2 (โจทย์สด 15 นาที)
# F2 Session 12 · Grand Showcase Level 2
# ═══════════════════════════════════════════════════════════
# 🎯 พิสูจน์ว่าจบ Level 2! แก้ให้รันได้ใน 15 นาที
# ───────────────────────────────────────────────────────────

scores = [85, 72, 90, 68, 95]

# โจทย์ 1: วน list หาผลรวม + เฉลี่ย (for + accumulator)
total = 0
for s in scores:
    total = total + s
# TODO: หาค่าเฉลี่ย
avg = ____ / len(scores)        # 👈 แก้: total
print(f"รวม {total} · เฉลี่ย {avg}")

# โจทย์ 2: หาคะแนนสูงสุด (loop เอง ไม่ใช้ max)
biggest = scores[0]
for s in scores:
    if s > biggest:
        biggest = s
print(f"สูงสุด: {biggest}")
