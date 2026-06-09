# =====================================================
# 🎵 Workshop 2 — Playlist "เพลงถัดไป" (CTk Template)
# Python Foundation 2 · Session 2 · Access & Slicing
# =====================================================
# 🎯 เป้าหมาย:
#   1) ทำปุ่ม Prev ให้ถอยเพลง
#   2) ป้องกันไม่ให้ index เกินขอบ
#   3) (โบนัส) กด Next ที่เพลงสุดท้าย → กลับไปเพลงแรก
# ⏱️ เวลา: 20 นาที
# =====================================================
# 📦 ต้องติดตั้ง:
#   pip install customtkinter pygame
# =====================================================

import os
import customtkinter as ctk
import pygame

# ----- ข้อมูล Playlist -----
# ชื่อเพลง + ไฟล์จริงในโฟลเดอร์ songs/
playlist = [
    ("🎵 Do-Re-Mi (ไต่บันได)",   "songs/song1_do_re_mi.wav"),
    ("🎵 Twinkle Twinkle",       "songs/song2_twinkle.wav"),
    ("🎵 Happy Bounce",          "songs/song3_happy_bounce.wav"),
    ("🎵 March Time",            "songs/song4_march.wav"),
    ("🎵 Arpeggio",              "songs/song5_arpeggio.wav"),
]

current = 0  # index เพลงที่กำลังเล่น


# ----- เตรียม pygame mixer -----
pygame.mixer.init()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def play_current():
    """เล่นเพลงในตำแหน่ง current"""
    _, path = playlist[current]
    full_path = os.path.join(BASE_DIR, path)
    pygame.mixer.music.load(full_path)
    pygame.mixer.music.play()


# ----- ตั้งค่าหน้าต่าง CTk -----
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("🎧 CodeLab Playlist")
app.geometry("420x400")
app.configure(fg_color="#1a1a1a")


# ----- UI Elements -----
title_label = ctk.CTkLabel(
    app, text="🎧 NOW PLAYING",
    font=("IBM Plex Sans Thai", 13, "bold"),
    text_color="#888"
)
title_label.pack(pady=(24, 4))

song_label = ctk.CTkLabel(
    app, text=playlist[current][0],
    font=("IBM Plex Sans Thai", 20, "bold"),
    text_color="#fff", wraplength=380,
)
song_label.pack(pady=4)

pos_label = ctk.CTkLabel(
    app, text=f"เพลงที่ {current + 1} / {len(playlist)}",
    font=("IBM Plex Sans Thai", 13), text_color="#aaa"
)
pos_label.pack(pady=2)


# ----- Helper: อัปเดตป้ายชื่อเพลง + เล่นเพลง -----
def update_display():
    song_label.configure(text=playlist[current][0])
    pos_label.configure(text=f"เพลงที่ {current + 1} / {len(playlist)}")
    play_current()
    play_btn.configure(text="⏸")
    is_playing[0] = True


# ----- ปุ่ม Next (ตัวอย่าง — ทำไว้ให้แล้ว) -----
def next_song():
    global current
    # TODO ข้อ 2: ป้องกันไม่ให้ index เกิน len(playlist) - 1
    # TODO ข้อ 3 (โบนัส): ถ้าเพลงสุดท้าย → กลับเพลงแรก
    current = current + 1
    update_display()


# ----- ปุ่ม Prev (ให้เด็กเขียน!) -----
def prev_song():
    global current
    # TODO ข้อ 1: ทำให้ถอยกลับเพลงก่อน
    # คำใบ้: ใช้ current = current - 1
    # และอย่าลืม update_display()
    pass


# ----- ปุ่ม Play / Pause -----
is_playing = [False]
def toggle_play():
    if is_playing[0]:
        pygame.mixer.music.pause()
        play_btn.configure(text="▶")
        is_playing[0] = False
    else:
        if pygame.mixer.music.get_pos() > 0:
            pygame.mixer.music.unpause()
        else:
            play_current()
        play_btn.configure(text="⏸")
        is_playing[0] = True


# ----- ปุ่ม Controls -----
btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=30)

prev_btn = ctk.CTkButton(
    btn_frame, text="⏮  Prev", width=110, height=50,
    font=("IBM Plex Sans Thai", 15, "bold"),
    fg_color="#333", hover_color="#555",
    command=prev_song,
)
prev_btn.grid(row=0, column=0, padx=8)

play_btn = ctk.CTkButton(
    btn_frame, text="▶", width=70, height=60,
    font=("Arial", 22, "bold"),
    fg_color="#C8102E", hover_color="#8B0000",
    corner_radius=30,
    command=toggle_play,
)
play_btn.grid(row=0, column=1, padx=8)

next_btn = ctk.CTkButton(
    btn_frame, text="Next  ⏭", width=110, height=50,
    font=("IBM Plex Sans Thai", 15, "bold"),
    fg_color="#333", hover_color="#555",
    command=next_song,
)
next_btn.grid(row=0, column=2, padx=8)


# ----- Tip -----
tip = ctk.CTkLabel(
    app, text="💡 กด ▶ ฟังเพลง แล้วลองกด Next/Prev",
    font=("IBM Plex Sans Thai", 12), text_color="#666"
)
tip.pack(pady=4)


# ----- Footer -----
footer = ctk.CTkLabel(
    app, text="CodeLab · Python F2 · Session 2",
    font=("IBM Plex Sans Thai", 11), text_color="#444"
)
footer.pack(side="bottom", pady=10)


app.mainloop()
