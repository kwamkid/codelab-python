# ═══════════════════════════════════════════════════════════
# ⭐ HW2 (เก่ง · optional) · FizzBuzz — for + if (คลาสสิก!)
# F1 Session 07 · For Loops (Light)  ·  ~30 นาที
# ═══════════════════════════════════════════════════════════
# 🎯 วน 1 ถึง 30:
#    หารด้วย 3 ลงตัว → "Fizz" · หารด้วย 5 → "Buzz"
#    หารทั้ง 3 และ 5 → "FizzBuzz" · นอกนั้น → เลขนั้น
# 💡 โจทย์สัมภาษณ์งาน programmer ที่ดังที่สุด!
# ───────────────────────────────────────────────────────────

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        # TODO: print "Buzz"
        print(____)        # 👈 แก้ตรงนี้: "Buzz"
    else:
        print(i)

# ✅ 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz ...
