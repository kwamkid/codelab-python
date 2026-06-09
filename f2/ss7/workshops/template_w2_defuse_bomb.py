# =====================================================
# W2 — Defuse the Bomb (PyGame Template)
# Python Foundation 2 - Session 7 - Loop Control
# =====================================================
# GOAL: Use break inside a game loop with countdown + input
# TIME: 15 minutes
# SKILL: while loop, break, attempts counter
# REQUIREMENT: pip install pygame
# =====================================================
# RULES OF THE GAME:
#   - 10-second countdown
#   - Player must type the CODE before time runs out
#   - 3 wrong attempts -> BOOM (game over)
#   - Correct guess -> break (defused!)
# =====================================================

import pygame
import sys
import time

pygame.init()

# ── Game window setup ───────────────────────────────
WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Defuse the Bomb")
font_big = pygame.font.SysFont("Arial", 60, bold=True)
font_mid = pygame.font.SysFont("Arial", 32)
font_small = pygame.font.SysFont("Arial", 22)
clock = pygame.time.Clock()

# ── Bomb settings ───────────────────────────────────
CODE = "1234"           # the secret code (change if you want)
TIME_LIMIT = 10         # seconds
MAX_ATTEMPTS = 3

attempts = 0
input_text = ""
start_time = time.time()
status = "TICKING"      # TICKING / DEFUSED / EXPLODED


# =====================================================
# GAME LOOP
# =====================================================
while True:
    # Calculate remaining time
    elapsed = time.time() - start_time
    remaining = TIME_LIMIT - elapsed

    # ── TODO 1: time runs out -> EXPLODED ───────────
    if remaining ___ 0:        # <-- <=
        status = "EXPLODED"
        ___                    # <-- break

    # ── Event handling ──────────────────────────────
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and status == "TICKING":
            if event.key == pygame.K_RETURN:
                # ── TODO 2: check input ─────────────
                if input_text == ___:    # <-- CODE
                    status = "DEFUSED"
                    ___                  # <-- break  (out of FOR loop, then check while)
                else:
                    # ── TODO 3: wrong attempt ───────
                    attempts ___ 1       # <-- += 1
                    input_text = ""
                    if attempts >= ___:  # <-- MAX_ATTEMPTS
                        status = "EXPLODED"
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.unicode.isdigit():
                input_text += event.unicode

    # ── If defused/exploded, exit while loop ────────
    if status != "TICKING":
        ___                    # <-- break

    # ── DRAWING ─────────────────────────────────────
    screen.fill((20, 20, 30))

    timer_text = font_big.render(f"{remaining:.1f}s", True, (255, 80, 80))
    screen.blit(timer_text, (WIDTH//2 - 80, 40))

    label = font_mid.render("Enter code:", True, (255, 255, 255))
    screen.blit(label, (50, 160))

    input_box = font_big.render(input_text + "_", True, (255, 200, 50))
    screen.blit(input_box, (50, 200))

    attempts_text = font_small.render(f"Attempts: {attempts} / {MAX_ATTEMPTS}", True, (200, 200, 200))
    screen.blit(attempts_text, (50, 320))

    pygame.display.flip()
    clock.tick(30)


# =====================================================
# END SCREEN
# =====================================================
end_running = True
while end_running:
    screen.fill((20, 20, 30))

    if status == "DEFUSED":
        msg = font_big.render("DEFUSED!", True, (80, 220, 100))
        sub = font_mid.render(f"Code cracked in {attempts + 1} tries", True, (255, 255, 255))
    else:
        msg = font_big.render("BOOM!", True, (255, 80, 80))
        sub = font_mid.render("Better luck next time", True, (255, 255, 255))

    screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 60))
    screen.blit(sub, (WIDTH//2 - sub.get_width()//2, HEIGHT//2 + 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            end_running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()


# =====================================================
# KEY IDEAS
# =====================================================
# - while True + break = controlled game loop
# - attempts counter + max = "3 strikes" pattern
# - break exits the LOOP, not the program
# =====================================================
