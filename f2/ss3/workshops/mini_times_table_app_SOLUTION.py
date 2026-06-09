# =====================================================
# ✅ Mini Times Table App — SOLUTION
# =====================================================

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("✖️ Times Table App")
app.geometry("360x520")
app.configure(fg_color="#1a1a1a")

header = ctk.CTkLabel(app, text="✖️ TIMES TABLE",
    font=("IBM Plex Sans Thai", 12, "bold"), text_color="#888")
header.pack(pady=(20, 4))

base_label = ctk.CTkLabel(app, text="แม่ 2",
    font=("IBM Plex Sans Thai", 24, "bold"), text_color="#fff")
base_label.pack(pady=4)

table_label = ctk.CTkLabel(app, text="",
    font=("JetBrains Mono", 14), text_color="#50FA7B", justify="left")
table_label.pack(pady=(10, 20))


def show_table(value):
    base = int(value)
    base_label.configure(text=f"แม่ {base}")

    result = ""
    for i in range(1, 13):
        answer = base * i           # ← ข้อ 1: คำนวณผลคูณ
        star = " ⭐" if answer > 50 else ""   # ← ข้อ 2: โบนัส
        result += f"{base} x {i:2d} = {answer}{star}\n"

    table_label.configure(text=result)


slider_label = ctk.CTkLabel(app, text="← เลื่อนเพื่อเปลี่ยนแม่ →",
    font=("IBM Plex Sans Thai", 11), text_color="#666")
slider_label.pack(pady=(10, 4))

slider = ctk.CTkSlider(app, from_=2, to=12, number_of_steps=10, width=280,
    button_color="#C8102E", button_hover_color="#8B0000",
    progress_color="#E53935", command=show_table)
slider.set(2)
slider.pack(pady=8)

footer = ctk.CTkLabel(app, text="CodeLab · Python F2 · Session 3",
    font=("IBM Plex Sans Thai", 10), text_color="#444")
footer.pack(side="bottom", pady=12)

show_table(2)
app.mainloop()
