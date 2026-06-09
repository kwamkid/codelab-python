# ═══════════════════════════════════════════════════════════
# 🎨 Mini · Unit Converter (°C ↔ °F) — CustomTkinter Template
# F2 Session 08 · Functions
# ═══════════════════════════════════════════════════════════
#
# 🎯 หน้าที่ของเด็ก: เติมแค่ 2 function ตรง # TODO
# ❌ ห้ามแตะส่วน UI ด้านล่าง (ครูเตรียมไว้ให้แล้ว)
# ───────────────────────────────────────────────────────────

# ─── ส่วนที่เด็กต้องแก้ (FUNCTIONS) ─────────────────────────
def c_to_f(c):
    # TODO 1: แปลง Celsius เป็น Fahrenheit
    # สูตร: c * 9/5 + 32
    return ____   # 👈 แก้ตรงนี้

def f_to_c(f):
    # TODO 2: แปลง Fahrenheit เป็น Celsius
    # สูตร: (f - 32) * 5/9
    return ____   # 👈 แก้ตรงนี้
# ───────────────────────────────────────────────────────────


# ❌ ห้ามแตะส่วนล่างนี้ (UI — ครูจะอธิบายภายหลัง)
import customtkinter as ctk

ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("เครื่องแปลงอุณหภูมิ")
app.geometry("360x260")

entry = ctk.CTkEntry(app, placeholder_text="ใส่ตัวเลข", width=200)
entry.pack(pady=20)
result = ctk.CTkLabel(app, text="ผลลัพธ์จะขึ้นตรงนี้", font=("IBM Plex Sans Thai", 18))
result.pack(pady=10)

def do_c_to_f():
    val = float(entry.get())
    result.configure(text=str(val) + "°C = " + str(c_to_f(val)) + "°F")

def do_f_to_c():
    val = float(entry.get())
    result.configure(text=str(val) + "°F = " + str(round(f_to_c(val), 1)) + "°C")

ctk.CTkButton(app, text="°C → °F", command=do_c_to_f).pack(pady=6)
ctk.CTkButton(app, text="°F → °C", command=do_f_to_c).pack(pady=6)

app.mainloop()
