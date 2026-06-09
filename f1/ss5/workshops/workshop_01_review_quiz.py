# ═══════════════════════════════════════════════════════════
# 🖥️ W1 · Review Quiz — ทบทวน S1-4
# F1 Session 05 · Workshop Day + PyGame
# ═══════════════════════════════════════════════════════════
# 🎯 ตอบคำถามทบทวน variables / input / math / if-else
# ───────────────────────────────────────────────────────────

score = 0
print("📝 Review Quiz — ทบทวน S1 ถึง S4")

a1 = input("Q1: input() คืนค่าชนิดอะไรเสมอ? (str/int) ")
if a1.lower() == "str":
    print("✓ ถูก!"); score += 1
else:
    print("✗ คำตอบ: str")

a2 = int(input("Q2: 2 + 3 * 4 = ? "))
# TODO: เช็คว่าตอบ 14 มั้ย (PEMDAS)
if a2 == ____:        # 👈 แก้ตรงนี้: 14
    print("✓ ถูก!"); score += 1
else:
    print("✗ คำตอบ: 14 (คูณก่อน)")

a3 = input("Q3: คำสั่งตัดสินใจใน Python? (if/for) ")
if a3.lower() == "if":
    print("✓ ถูก!"); score += 1

print(f"\n🎉 คะแนนรวม: {score}/3")
