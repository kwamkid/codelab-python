# ═══════════════════════════════════════════════════════════
# 🖥️ W2 · Grade Function — function + return หลายทาง
# F2 Session 08 · Functions
# ═══════════════════════════════════════════════════════════
#
# 🎯 หน้าที่ของเด็ก: เติม return ในแต่ละเงื่อนไข (# TODO)
# function รับคะแนน → คืนเกรด (เหมือนระบบของโรงเรียน!)
# ───────────────────────────────────────────────────────────

def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        # TODO 1: return "B"
        return ____
    elif score >= 60:
        # TODO 2: return "C"
        return ____
    elif score >= 50:
        return "D"
    else:
        return "F"


# ───────────────────────────────────────────────────────────
# ทดสอบ function
print("คะแนน 85 ได้เกรด:", get_grade(85))   # ควรได้ B
print("คะแนน 95 ได้เกรด:", get_grade(95))   # ควรได้ A
print("คะแนน 45 ได้เกรด:", get_grade(45))   # ควรได้ F

# ✨ Bonus: วน list คะแนนทั้งห้อง แล้ว print เกรดทุกคน
scores = [92, 78, 55, 63, 41, 88]
print("\n--- เกรดทั้งห้อง ---")
for s in scores:
    print("คะแนน", s, "=>", get_grade(s))
