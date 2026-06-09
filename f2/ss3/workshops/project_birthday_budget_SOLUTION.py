# =====================================================
# ✅ Project Birthday Budget — SOLUTION
# =====================================================

print("🎂 ยินดีต้อนรับสู่ระบบคำนวณงบปาร์ตี้วันเกิด!")
print("=" * 40)

items = ["🎂 เค้ก", "🍭 ขนม", "🥤 น้ำ", "🎈 ลูกโป่ง", "🎁 ของขวัญ"]
prices = []
total = 0

for item in items:
    price = int(input(f"{item} ราคา: "))
    prices.append(price)
    total = total + price

print()
print("=" * 40)
print(f"💰 ยอดรวม: {total} บาท")

# เช็คงบ
if total > 1000:
    print("⚠️ เกินงบแล้ว! ตัดอะไรได้บ้าง?")
else:
    print("✅ ใช้งบได้ ไม่เกินที่คุยกับพ่อแม่!")

# โบนัส: ของแพงสุด
max_price = max(prices)
max_item = items[prices.index(max_price)]
print(f"😱 ของแพงสุด: {max_item} ({max_price} บาท)")

# โบนัส: งบที่พ่อแม่ให้
budget = int(input("\nพ่อแม่ให้งบเท่าไหร่: "))
remaining = budget - total
if remaining >= 0:
    print(f"💚 เหลือ {remaining} บาท")
else:
    print(f"💔 เกินงบ {abs(remaining)} บาท")
