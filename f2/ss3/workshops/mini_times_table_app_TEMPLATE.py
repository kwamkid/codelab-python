# =====================================================
# 🎨 Mini — Times Table App (CTk Template)
# Python Foundation 2 · Session 3 · For Loops Deep
# =====================================================
# 🎯 GOAL:
#   1) Fix the logic so multiplication works correctly
#   2) (BONUS) Color numbers red if result > 50
#
# ⏱️  TIME: 15 minutes
# 📦 INSTALL: pip install customtkinter
# =====================================================

import customtkinter as ctk


# ----- Window setup -----
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("✖️ Times Table App")
app.geometry("360x520")
app.configure(fg_color="#1a1a1a")


# ----- Header -----
header = ctk.CTkLabel(
    app, text="✖️ TIMES TABLE",
    font=("IBM Plex Sans Thai", 12, "bold"),
    text_color="#888"
)
header.pack(pady=(20, 4))

base_label = ctk.CTkLabel(
    app, text="Table of 2",
    font=("IBM Plex Sans Thai", 24, "bold"),
    text_color="#fff"
)
base_label.pack(pady=4)


# ----- Table display -----
table_label = ctk.CTkLabel(
    app, text="(drag the slider to choose a number)",
    font=("JetBrains Mono", 14),
    text_color="#50FA7B",
    justify="left"
)
table_label.pack(pady=(10, 20))


# ----- The main function (EDIT THIS!) -----
def show_table(value):
    """Called when slider moves — value is the chosen number"""
    base = int(value)
    base_label.configure(text=f"Table of {base}")

    # Build the times table text
    result = ""
    for i in range(1, 13):
        # 📝 TODO: Fix the ___ to calculate base × i
        answer = ___
        result += f"{base} x {i:2d} = {answer}\n"

    table_label.configure(text=result)


# ----- Slider -----
slider_label = ctk.CTkLabel(
    app, text="← drag to change table →",
    font=("IBM Plex Sans Thai", 11),
    text_color="#666"
)
slider_label.pack(pady=(10, 4))

slider = ctk.CTkSlider(
    app, from_=2, to=12,
    number_of_steps=10,
    width=280,
    button_color="#C8102E",
    button_hover_color="#8B0000",
    progress_color="#E53935",
    command=show_table,
)
slider.set(2)
slider.pack(pady=8)


# ----- Footer -----
footer = ctk.CTkLabel(
    app, text="CodeLab · Python F2 · Session 3",
    font=("IBM Plex Sans Thai", 10),
    text_color="#444"
)
footer.pack(side="bottom", pady=12)


# Initial call to show table of 2
show_table(2)


app.mainloop()
