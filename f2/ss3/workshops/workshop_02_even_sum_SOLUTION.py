# =====================================================
# ✅ Workshop 2 — SOLUTION
# =====================================================

total = 0

print("🔢 รวมเลขคู่ 2 ถึง 20")
print("=" * 30)

for n in range(2, 21, 2):
    total = total + n    # หรือ total += n
    print(f"เพิ่ม {n} → รวม {total}")

print("=" * 30)
print(f"💰 ยอดรวมสุดท้าย = {total}")
# Output: 110

# โบนัส: ใช้ += shortcut
# total += n

# โบนัส: ค่าเฉลี่ย
# count = 0
# for n in range(2, 21, 2):
#     total += n
#     count += 1
# print(f"ค่าเฉลี่ย = {total / count}")
