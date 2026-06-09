# =====================================================
# HW2 — Password Lock (Advanced)
# Python Foundation 2 - Session 7 - Loop Control
# =====================================================
# GOAL: Build a 3-try password lock + log attempts
# TIME: 30 minutes
# LEVEL: Advanced (optional)
# =====================================================
# SPEC:
#   - Correct password: "codelab"
#   - User has 3 attempts
#   - Right -> "Welcome!" + break
#   - Wrong 3 times -> "Account locked!" + show all wrong attempts
#   - Track every wrong attempt in a list (Bonus)
# =====================================================


# ── Setup ───────────────────────────────────────────
PASSWORD = "codelab"
MAX_ATTEMPTS = 3
wrong_attempts = []                       # Bonus: log wrong tries


# =====================================================
# TASK 1: 3-attempt loop with break
# =====================================================
print("=== Welcome to the Vault ===")

for attempt in range(MAX_ATTEMPTS):
    print(f"\nAttempt {attempt + 1} of {MAX_ATTEMPTS}")
    guess = input("Enter password: ")

    if guess == PASSWORD:
        print("\nWelcome! Access granted.")
        ___                               # <-- break
    else:
        print("Wrong password!")
        # ── Bonus: log this wrong attempt ───────────
        wrong_attempts.___(guess)         # <-- append(guess)


# =====================================================
# TASK 2: for-else — runs if loop completed without break
# =====================================================
# (Place this DIRECTLY after the for loop above,
#  with the same indentation as 'for')
___:                                       # <-- else
    print("\n*** Account LOCKED after 3 wrong attempts ***")

    # ── Bonus: show all wrong attempts ──────────────
    print("Wrong attempts log:")
    for i, wrong in enumerate(wrong_attempts, start=1):
        print(f"  {i}. '{wrong}'")


# =====================================================
# EXPECTED OUTPUT — Scenario A (correct on 2nd try):
# =====================================================
# === Welcome to the Vault ===
#
# Attempt 1 of 3
# Enter password: hello
# Wrong password!
#
# Attempt 2 of 3
# Enter password: codelab
#
# Welcome! Access granted.
# =====================================================
# EXPECTED OUTPUT — Scenario B (3 wrongs):
# =====================================================
# === Welcome to the Vault ===
#
# Attempt 1 of 3
# Enter password: 1234
# Wrong password!
# ... (3 tries)
#
# *** Account LOCKED after 3 wrong attempts ***
# Wrong attempts log:
#   1. '1234'
#   2. 'qwerty'
#   3. 'password'
# =====================================================


# =====================================================
# CRITERIA
# =====================================================
# [ ] Correct password breaks out -> "Welcome!"
# [ ] 3 wrong attempts -> locked message
# [ ] Bonus: wrong_attempts list is built correctly
# [ ] Bonus: log printed only on lockout
# =====================================================


# =====================================================
# HINT
# =====================================================
# - for-else: the 'else' clause of a for loop runs only
#   when the loop completes WITHOUT hitting a break.
# - Indentation: 'else' must align with 'for', NOT with
#   the 'if' inside.
# =====================================================


# =====================================================
# EXTRA CHALLENGE (if you have time)
# =====================================================
# - Hide the password input using getpass.getpass()
# - Lock for 30 seconds after 3 wrong tries (use time.sleep)
# - Save lockout state to a .txt file (so it persists)
# =====================================================
