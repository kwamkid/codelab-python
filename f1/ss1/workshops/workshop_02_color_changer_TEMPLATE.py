# =====================================================
# 🎨 Workshop 2 — Color Changer (CTk Template)
# Python Foundation 1 · Session 1 · Setup & Variables
# =====================================================
# 🎯 GOAL: Change the window background color!
#    Just change ONE variable and see the magic.
#
# ⏱️  TIME: 15 minutes
# 📦 INSTALL: pip install customtkinter
# =====================================================

import customtkinter as ctk

# 📝 TODO: Change this color to anything you like!
#    Try: "red", "blue", "green", "purple", "pink"
#    Or HEX codes: "#ef443a", "#ffc94a", "#7ed4a5"
my_color = "red"


# ----- Window setup (teacher provides this — don't touch!) -----
app = ctk.CTk()
app.title("🎨 My Color!")
app.geometry("400x400")
app.configure(fg_color=my_color)

# Big label showing the color name
label = ctk.CTkLabel(
    app,
    text=f"I chose:\n{my_color}",
    font=("Space Grotesk", 32, "bold"),
    text_color="white",
)
label.pack(expand=True)

# Run the app
app.mainloop()


# =====================================================
# 🎁 BONUS: Add MORE variables!
#   - Change the title too
#   - Change the window size
#   - Try hex color codes
# =====================================================
#
# my_color = "#ef443a"           # CodeLab red
# my_title = "My Awesome Window"
# my_size = "600x600"
#
# app.title(my_title)
# app.geometry(my_size)
# =====================================================
