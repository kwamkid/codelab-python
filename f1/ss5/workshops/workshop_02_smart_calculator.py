# ═══════════════════════════════════════════════════════════
# 🖥️ W2 · Smart Calculator — if + math รวมกัน
# F1 Session 05 · Workshop Day
# ═══════════════════════════════════════════════════════════
# 🎯 เลือก operation (+, -, *, /) แล้วคำนวณ — รวม S2+S3+S4
# ───────────────────────────────────────────────────────────

a = int(input("เลขที่ 1: "))
op = input("เลือก (+, -, *, /): ")
b = int(input("เลขที่ 2: "))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    # TODO: คูณ
    result = ____     # 👈 แก้ตรงนี้: a * b
elif op == "/":
    result = a / b
else:
    result = "ไม่รู้จัก operation นี้"

print(f"ผลลัพธ์: {a} {op} {b} = {result}")
