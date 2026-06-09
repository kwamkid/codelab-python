"""
🎒 กระเป๋านักเรียน (School Bag App)
Workshop 2 — Lists Intro (LV2 Session 1)

📌 คำสั่ง:
   1. อ่านโค้ดทั้งหมดก่อน
   2. หา TODO แล้วเขียนโค้ดให้ครบ
   3. ทดสอบ: เพิ่มของ → ลบของ → ดูจำนวน
"""

import customtkinter as ctk

# ============================================================
# ตั้งค่าหน้าตา
# ============================================================
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🎒 กระเป๋านักเรียน")
app.geometry("400x520")
app.resizable(False, False)

# ============================================================
# ตัวแปรเก็บของในกระเป๋า  ← ใช้ List!
# ============================================================
bag = []        # list เปล่า — เดี๋ยวจะเพิ่มของเข้าไป

# ============================================================
# ฟังก์ชัน — แก้โค้ดตรงนี้!
# ============================================================

def update_display():
    """อัปเดตหน้าจอให้แสดงของในกระเป๋า"""
    # ลบข้อความเก่าออก
    listbox.configure(state="normal")
    listbox.delete("0.0", "end")

    if len(bag) == 0:
        listbox.insert("0.0", "  (กระเป๋าว่าง)")
    else:
        for i, item in enumerate(bag, 1):
            listbox.insert("end", f"  {i}. {item}\n")

    listbox.configure(state="disabled")

    # อัปเดตจำนวน
    # ============================================
    # TODO 3: ใช้ len() นับจำนวนของในกระเป๋า
    #         แล้วแสดงใน count_label
    #
    # ตัวอย่าง: count_label.configure(text=f"...")
    # ============================================
    count_label.configure(text=f"จำนวน: ... ชิ้น")   # ← แก้ตรงนี้!


def add_item():
    """เพิ่มของเข้ากระเป๋า"""
    item = entry.get().strip()     # อ่านข้อความจากช่อง input

    if item == "":
        return  # ถ้าไม่พิมพ์อะไร ไม่ต้องทำอะไร

    # ============================================
    # TODO 1: เพิ่ม item เข้าไปใน bag
    #
    # Hint: ใช้ .append()
    # ============================================
    pass   # ← ลบ pass แล้วเขียนโค้ดตรงนี้!

    entry.delete(0, "end")         # เคลียร์ช่อง input
    update_display()               # อัปเดตหน้าจอ


def remove_item():
    """ลบของชิ้นล่าสุดออกจากกระเป๋า"""
    # ============================================
    # TODO 2: ลบของชิ้นล่าสุดออกจาก bag
    #
    # Hint: ใช้ .pop()
    # ⚠️  ระวัง! ถ้า bag ว่าง จะ pop ไม่ได้
    #     → เช็คก่อนว่า len(bag) > 0
    # ============================================
    pass   # ← ลบ pass แล้วเขียนโค้ดตรงนี้!

    update_display()               # อัปเดตหน้าจอ


# ============================================================
# สร้างหน้าจอ (ไม่ต้องแก้ส่วนนี้)
# ============================================================

# หัวข้อ
title_label = ctk.CTkLabel(
    app, text="🎒 กระเป๋านักเรียน",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=(20, 5))

# คำอธิบาย
desc_label = ctk.CTkLabel(
    app, text="เพิ่มของที่อยากใส่กระเป๋าไปโรงเรียน",
    font=("Arial", 14), text_color="gray"
)
desc_label.pack(pady=(0, 15))

# ช่อง input + ปุ่ม
input_frame = ctk.CTkFrame(app, fg_color="transparent")
input_frame.pack(padx=20, fill="x")

entry = ctk.CTkEntry(
    input_frame,
    placeholder_text="พิมพ์ชื่อของ...",
    font=("Arial", 14),
    height=38
)
entry.pack(side="left", expand=True, fill="x", padx=(0, 8))

add_btn = ctk.CTkButton(
    input_frame, text="＋ เพิ่ม", width=90, height=38,
    font=("Arial", 14, "bold"),
    fg_color="#4CAF50", hover_color="#388E3C",
    command=add_item
)
add_btn.pack(side="right")

# รายการของ
list_label = ctk.CTkLabel(
    app, text="📋 ของในกระเป๋า:",
    font=("Arial", 14, "bold"), anchor="w"
)
list_label.pack(padx=25, pady=(15, 5), anchor="w")

listbox = ctk.CTkTextbox(
    app, height=200, font=("Arial", 14),
    state="disabled", fg_color="#F5F5F5"
)
listbox.pack(padx=20, fill="x")

# แถวล่าง: จำนวน + ปุ่มลบ
bottom_frame = ctk.CTkFrame(app, fg_color="transparent")
bottom_frame.pack(padx=20, pady=(10, 20), fill="x")

count_label = ctk.CTkLabel(
    bottom_frame, text="จำนวน: 0 ชิ้น",
    font=("Arial", 14)
)
count_label.pack(side="left")

remove_btn = ctk.CTkButton(
    bottom_frame, text="🗑 ลบชิ้นล่าสุด", width=130, height=36,
    font=("Arial", 13),
    fg_color="#E53935", hover_color="#C62828",
    command=remove_item
)
remove_btn.pack(side="right")

# ============================================================
# เริ่มแอป
# ============================================================
update_display()
app.mainloop()
