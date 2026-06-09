# =====================================================
# ✅ Workshop 2 — SOLUTION
# =====================================================

base = int(input("เลือกแม่ (2-12): "))

print(f"\n📚 สูตรคูณแม่ {base}")
print("=" * 20)

# range(1, 13) → 1, 2, ..., 12
for i in range(1, 13):
    print(f"{base} x {i} = {base * i}")

# โบนัส: ใส่ดาว ถ้าเกิน 50
# for i in range(1, 13):
#     result = base * i
#     star = " ⭐" if result > 50 else ""
#     print(f"{base} x {i} = {result}{star}")
