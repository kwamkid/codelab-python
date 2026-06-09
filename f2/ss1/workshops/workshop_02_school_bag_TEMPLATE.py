# =====================================================
# 🎒 Workshop 2 — School Bag (CTk Template)
# Python Foundation 2 · Session 1 · Lists Intro
# =====================================================
# 🎯 GOAL: GUI to manage items in a bag.
# ⏱️  TIME: 15 minutes
# 📦 INSTALL: pip install customtkinter
# =====================================================

import customtkinter as ctk

# The bag — starts with 3 items
bag = ["📕 Book", "✏️ Pencil", "📐 Ruler"]


# ----- Window setup -----
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("🎒 School Bag")
app.geometry("400x500")
app.configure(fg_color="#1a1a1a")


# ----- UI elements -----
header = ctk.CTkLabel(app, text="🎒 MY SCHOOL BAG",
    font=("Inter", 18, "bold"), text_color="#FFD43B")
header.pack(pady=(20, 10))

# Display area for the bag contents
display = ctk.CTkLabel(app, text="", font=("JetBrains Mono", 14),
    text_color="#fff", justify="left", wraplength=360)
display.pack(pady=(10, 20))

# Input field
entry = ctk.CTkEntry(app, placeholder_text="Item name...",
    width=300, height=40, font=("Inter", 14))
entry.pack(pady=8)


# ----- Helper: refresh the display -----
def refresh():
    if len(bag) == 0:
        display.configure(text="(empty)")
        return
    text = ""
    for i, item in enumerate(bag, start=1):
        text += f"{i}. {item}\n"
    text += f"\nTotal: {len(bag)} items"
    display.configure(text=text)


# 📝 TODO 1: Add item to the bag
def add_item():
    name = entry.get().strip()
    if name == "":
        return
    # Add to bag (use append!)
    bag.___(name)    # ← fill in append
    entry.delete(0, "end")
    refresh()


# 📝 TODO 2: Remove item from the bag
def remove_item():
    name = entry.get().strip()
    if name == "":
        return
    # Try to remove (use remove!)
    if name ___ bag:    # ← fill in: in
        bag.___(name)   # ← fill in remove
    entry.delete(0, "end")
    refresh()


# ----- Buttons -----
btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=14)

ctk.CTkButton(btn_frame, text="➕ Add", command=add_item,
    fg_color="#3776AB", hover_color="#2c5d87",
    font=("Inter", 14, "bold"), width=120).grid(row=0, column=0, padx=8)

ctk.CTkButton(btn_frame, text="➖ Remove", command=remove_item,
    fg_color="#FFD43B", hover_color="#e6b800", text_color="#000",
    font=("Inter", 14, "bold"), width=120).grid(row=0, column=1, padx=8)


# ----- Footer -----
ctk.CTkLabel(app, text="CodeLab · Python F2 · Session 1",
    font=("Inter", 11), text_color="#444").pack(side="bottom", pady=10)


refresh()
app.mainloop()


# =====================================================
# 🎁 BONUS: prevent duplicates
#   Inside add_item, check `if name not in bag:` first
# =====================================================
