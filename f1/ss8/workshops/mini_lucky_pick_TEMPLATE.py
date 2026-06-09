# ═══════════════════════════════════════════════════════════
# 🎨 Mini · Lucky Pick — CustomTkinter Template (สุ่มรางวัล)
# F1 Session 08 · Lists (Light)
# ═══════════════════════════════════════════════════════════
# 🎯 กดปุ่ม "สุ่ม!" → โปรแกรมสุ่มรางวัลจาก list มาโชว์
# ❌ ห้ามแตะ UI ด้านล่าง — แก้แค่ function draw_prize()
# ───────────────────────────────────────────────────────────

import random

prizes = ["🎁 ตุ๊กตา", "🍫 ช็อกโกแลต", "✏️ ดินสอ", "📚 หนังสือ", "🎮 เกม"]

def draw_prize():
    # TODO: สุ่มเลือก 1 รางวัลจาก prizes
    return random.choice(____)     # 👈 แก้ตรงนี้: prizes
# ───────────────────────────────────────────────────────────


# ❌ ห้ามแตะส่วนล่างนี้ (UI)
import customtkinter as ctk

ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("🎰 Lucky Pick")
app.geometry("360x240")

result = ctk.CTkLabel(app, text="กดปุ่มเพื่อสุ่ม!", font=("IBM Plex Sans Thai", 26))
result.pack(pady=40)

def on_draw():
    result.configure(text=draw_prize())

ctk.CTkButton(app, text="🎲 สุ่ม!", command=on_draw, width=160, height=44).pack(pady=10)

app.mainloop()
