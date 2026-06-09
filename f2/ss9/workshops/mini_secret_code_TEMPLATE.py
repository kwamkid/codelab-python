# ═══════════════════════════════════════════════════════════
# 🔐 Mini · เข้ารหัสลับ (Encode/Decode) — CustomTkinter Template
# F2 Session 09 · String Methods
# ═══════════════════════════════════════════════════════════
#
# 🎯 หน้าที่ของเด็ก: เติมแค่ 2 function ตรง # TODO
# ❌ ห้ามแตะส่วน UI ด้านล่าง (ครูเตรียมไว้ให้แล้ว)
# 💡 หลักการ: เลื่อนตัวอักษรไป 3 ตำแหน่ง (a->d, b->e ...)
# ───────────────────────────────────────────────────────────

# ─── ส่วนที่เด็กต้องแก้ (FUNCTIONS) ─────────────────────────
def encode(text):
    result = ""
    for char in text:
        # TODO 1: เลื่อนตัวอักษรไป +3 ด้วย chr(ord(char) + 3)
        result = result + ____   # 👈 แก้ตรงนี้
    return result

def decode(text):
    result = ""
    for char in text:
        # TODO 2: เลื่อนกลับ -3 ด้วย chr(ord(char) - 3)
        result = result + ____   # 👈 แก้ตรงนี้
    return result
# ───────────────────────────────────────────────────────────


# ❌ ห้ามแตะส่วนล่างนี้ (UI — ครูจะอธิบายภายหลัง)
import customtkinter as ctk

ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("เครื่องเข้ารหัสลับ 🔐")
app.geometry("400x280")

entry = ctk.CTkEntry(app, placeholder_text="พิมพ์ข้อความ", width=260)
entry.pack(pady=20)
result = ctk.CTkLabel(app, text="ผลลัพธ์จะขึ้นตรงนี้", font=("IBM Plex Sans Thai", 18), wraplength=340)
result.pack(pady=10)

def do_encode():
    result.configure(text="🔐 " + encode(entry.get()))

def do_decode():
    result.configure(text="🔓 " + decode(entry.get()))

ctk.CTkButton(app, text="Encode (เข้ารหัส)", command=do_encode).pack(pady=6)
ctk.CTkButton(app, text="Decode (ถอดรหัส)", command=do_decode).pack(pady=6)

app.mainloop()
