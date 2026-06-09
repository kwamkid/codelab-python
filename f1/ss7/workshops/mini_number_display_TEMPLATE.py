# ═══════════════════════════════════════════════════════════
# 🎨 Mini · Number Display — CustomTkinter Template (slider)
# F1 Session 07 · For Loops (Light)
# ═══════════════════════════════════════════════════════════
# 🎯 เลื่อน slider เลือก N → โปรแกรม print 1 ถึง N ด้วย for loop
# ❌ ห้ามแตะ UI ด้านล่าง — แก้แค่ function make_numbers()
# ───────────────────────────────────────────────────────────

def make_numbers(n):
    result = ""
    # TODO: วน i จาก 1 ถึง n แล้วต่อเข้า result
    for i in range(1, n + 1):
        result = result + str(i) + " "
    return result
# ───────────────────────────────────────────────────────────


# ❌ ห้ามแตะส่วนล่างนี้ (UI)
import customtkinter as ctk

ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("🔢 Number Display")
app.geometry("420x240")

label = ctk.CTkLabel(app, text="เลื่อน slider เลือกจำนวน", font=("IBM Plex Sans Thai", 18), wraplength=380)
label.pack(pady=24)

def on_slide(v):
    n = int(float(v))
    label.configure(text=f"1 ถึง {n}:\n{make_numbers(n)}")

slider = ctk.CTkSlider(app, from_=1, to=20, number_of_steps=19, command=on_slide, width=320)
slider.set(5)
slider.pack(pady=10)
on_slide(5)

app.mainloop()
