# ═══════════════════════════════════════════════════════════
# 🎮 Mini · Dino Run! — PyGame Template
# F1 Session 05 · Workshop Day + PyGame
# ═══════════════════════════════════════════════════════════
# 🎯 หน้าที่ของเด็ก: แก้ตัวเลขในส่วน CONFIG เท่านั้น!
#    แล้ว Upload ขึ้น Replit → Run → Share link พ่อแม่
# 📝 ติดตั้งก่อนรัน:  pip install pygame
# ───────────────────────────────────────────────────────────

import pygame, random

# ─── CONFIG (แก้ตรงนี้ได้เลย!) ──────────────────────────────
DINO_SPEED   = 5                 # 👈 ความเร็วเกม (ลองเปลี่ยนเป็น 8)
JUMP_POWER   = 16                # 👈 แรงกระโดด (ลอง 22 = กระโดดสูง)
DINO_SIZE    = 50                # 👈 ขนาดไดโน (ลอง 70)
BG_COLOR     = (135, 206, 235)   # 👈 สีพื้นหลัง (ลอง (255, 182, 193) = ชมพู)
OBSTACLE_GAP = 320               # 👈 ระยะห่างกระบองเพชร (ลอง 500 = ง่ายขึ้น)
# ────────────────────────────────────────────────────────────


# ❌ ห้ามแตะส่วนล่างนี้ (engine — ครูจะอธิบายภายหลัง)
pygame.init()
W, H = 800, 300
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Dino Run")
clock = pygame.time.Clock()
GROUND = H - 40

dino = pygame.Rect(60, GROUND - DINO_SIZE, DINO_SIZE, DINO_SIZE)
vel_y = 0
on_ground = True
obstacles = [pygame.Rect(W + i * OBSTACLE_GAP, GROUND - 40, 24, 40) for i in range(3)]
score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and on_ground:
            vel_y = -JUMP_POWER
            on_ground = False

    vel_y += 1
    dino.y += vel_y
    if dino.y >= GROUND - DINO_SIZE:
        dino.y = GROUND - DINO_SIZE
        vel_y = 0
        on_ground = True

    for ob in obstacles:
        ob.x -= DINO_SPEED
        if ob.right < 0:
            ob.x = W + OBSTACLE_GAP
            score += 1
        if dino.colliderect(ob):
            running = False

    screen.fill(BG_COLOR)
    pygame.draw.line(screen, (80, 80, 80), (0, GROUND), (W, GROUND), 3)
    pygame.draw.rect(screen, (60, 60, 60), dino)
    for ob in obstacles:
        pygame.draw.rect(screen, (34, 139, 34), ob)
    screen.blit(font.render(f"Score {score}", True, (0, 0, 0)), (W - 170, 20))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
