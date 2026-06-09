# ═══════════════════════════════════════════════════════════
# 🎨 Mini · Magic Door — CustomTkinter Template
# F1 Session 04 · If-Else + Logic
# ═══════════════════════════════════════════════════════════
# 🎯 หน้าที่ของเด็ก: เติม function check_door() ตรง # TODO
# ❌ ห้ามแตะส่วน UI ด้านล่าง (ครูเตรียมให้แล้ว)
# ───────────────────────────────────────────────────────────

# ─── ส่วนที่เด็กต้องแก้ ──────────────────────────────────────
def check_door(door):
    if door == 1:
        return "💰 เจอสมบัติ!"
    elif door == 2:
        # TODO: ประตู 2 เจอมังกร
        return ____      # 👈 แก้ตรงนี้: "🐉 เจอมังกร!"
    else:
        return "🚪 ทางออก ปลอดภัย!"
# ───────────────────────────────────────────────────────────


# ❌ ห้ามแตะส่วนล่างนี้ (UI)
import customtkinter as ctk

ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("🚪 Magic Door")
app.geometry("360x260")

result = ctk.CTkLabel(app, text="เลือกประตู!", font=("IBM Plex Sans Thai", 20))
result.pack(pady=24)

def choose(n):
    result.configure(text=check_door(n))

for i in (1, 2, 3):
    ctk.CTkButton(app, text=f"ประตู {i}", command=lambda n=i: choose(n)).pack(pady=6)

app.mainloop()
