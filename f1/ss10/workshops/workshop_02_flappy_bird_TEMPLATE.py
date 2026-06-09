# ═══════════════════════════════════════════════════════════
# 🎮 W2 · Flappy Bird! — PyGame Template
# F1 Session 10 · Workshop Day 2
# ═══════════════════════════════════════════════════════════
# 🎯 หน้าที่ของเด็ก: แก้ตัวเลขในส่วน CONFIG เท่านั้น!
#    แล้ว Upload ขึ้น Replit → Run → Share link พ่อแม่
# 📝 ติดตั้งก่อนรัน:  pip install pygame
# 🕹️  กด SPACE / คลิกเมาส์ = บินขึ้น
# ───────────────────────────────────────────────────────────

import pygame, random

# ─── CONFIG (แก้ตรงนี้ได้เลย!) ──────────────────────────────
GRAVITY     = 0.5                # 👈 แรงโน้มถ่วง (ลอง 0.3 = ตกช้า / 0.8 = ยาก)
FLAP_POWER  = 9                  # 👈 แรงกระพือ (ลอง 12 = พุ่งสูง)
PIPE_GAP    = 170                # 👈 ช่องว่างระหว่างท่อ (ลอง 220 = ง่ายขึ้น)
PIPE_SPEED  = 3                  # 👈 ความเร็วท่อ (ลอง 5 = เร็ว = ยาก)
BG_COLOR    = (113, 197, 207)    # 👈 สีพื้นหลัง (ลอง (255, 214, 165) = ส้มอ่อน)
# ────────────────────────────────────────────────────────────


# ❌ ห้ามแตะส่วนล่างนี้ (engine — ครูจะอธิบายภายหลัง)
pygame.init()
W, H = 400, 560
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 44)

def new_pipe():
    top = random.randint(60, H - PIPE_GAP - 120)
    return {"x": W, "top": top, "scored": False}

def reset():
    return {"y": H // 2, "vy": 0, "pipes": [new_pipe()], "score": 0, "alive": True}

g = reset()
BIRD_X = 90

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
            if g["alive"]:
                g["vy"] = -FLAP_POWER
            else:
                g = reset()

    if g["alive"]:
        g["vy"] += GRAVITY
        g["y"] += g["vy"]
        for p in g["pipes"]:
            p["x"] -= PIPE_SPEED
        if g["pipes"][-1]["x"] < W - 200:
            g["pipes"].append(new_pipe())
        g["pipes"] = [p for p in g["pipes"] if p["x"] > -70]

        for p in g["pipes"]:
            if not p["scored"] and p["x"] + 60 < BIRD_X:
                p["scored"] = True
                g["score"] += 1
            in_x = BIRD_X + 18 > p["x"] and BIRD_X - 18 < p["x"] + 60
            in_gap = g["y"] - 18 > p["top"] and g["y"] + 18 < p["top"] + PIPE_GAP
            if in_x and not in_gap:
                g["alive"] = False
        if g["y"] > H - 18 or g["y"] < 18:
            g["alive"] = False

    screen.fill(BG_COLOR)
    for p in g["pipes"]:
        pygame.draw.rect(screen, (60, 160, 75), (p["x"], 0, 60, p["top"]))
        pygame.draw.rect(screen, (60, 160, 75), (p["x"], p["top"] + PIPE_GAP, 60, H))
    pygame.draw.circle(screen, (255, 209, 67), (BIRD_X, int(g["y"])), 18)
    pygame.draw.circle(screen, (20, 20, 20), (BIRD_X + 6, int(g["y"]) - 5), 3)
    screen.blit(font.render(str(g["score"]), True, (255, 255, 255)), (W // 2 - 8, 30))
    if not g["alive"]:
        msg = font.render("กด SPACE เริ่มใหม่", True, (255, 255, 255))
        screen.blit(msg, (W // 2 - msg.get_width() // 2, H // 2))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
