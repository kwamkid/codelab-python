# =====================================================
# HW1 — ATM Simulator
# Python Foundation 2 - Session 7 - Loop Control
# =====================================================
# GOAL: Build a simple ATM with 2 break conditions
# TIME: 15-20 minutes
# REQUIRED for everyone
# =====================================================
# SPEC:
#   - Start balance = 1000 baht
#   - Loop:
#       - Ask how much to withdraw
#       - If amount > balance -> "Not enough!" + BREAK
#       - If withdrawal count >= 3 -> "Daily limit reached!" + BREAK
#       - Otherwise: subtract from balance, count++, show new balance
# =====================================================


# ── Initial state ───────────────────────────────────
balance = 1000
count = 0
MAX_WITHDRAWALS = 3


# =====================================================
# TASK: Write the ATM loop
# =====================================================
while True:
    print(f"\nBalance: {balance} baht | Withdrawals used: {count}/{MAX_WITHDRAWALS}")
    amount = int(input("How much to withdraw? "))

    # ── Condition 1: not enough money ───────────────
    if amount ___ balance:                # <-- >
        print("Not enough money in account!")
        ___                               # <-- break

    # ── Subtract + count ────────────────────────────
    balance ___ amount                    # <-- -= amount
    count ___ 1                           # <-- += 1
    print(f"Withdrew {amount}. New balance: {balance}")

    # ── Condition 2: limit reached ──────────────────
    if count ___ MAX_WITHDRAWALS:         # <-- >=
        print("Daily limit reached!")
        ___                               # <-- break


# ── Final summary (after loop ends) ─────────────────
print()
print("===== Session ended =====")
print(f"Final balance: {balance} baht")
print(f"Withdrawals: {count}")


# =====================================================
# EXPECTED OUTPUT (example):
# =====================================================
# Balance: 1000 baht | Withdrawals used: 0/3
# How much to withdraw? 300
# Withdrew 300. New balance: 700
#
# Balance: 700 baht | Withdrawals used: 1/3
# How much to withdraw? 800
# Not enough money in account!
#
# ===== Session ended =====
# Final balance: 700 baht
# Withdrawals: 1
# =====================================================


# =====================================================
# CRITERIA
# =====================================================
# [ ] Runs with no errors
# [ ] BOTH break conditions work (not enough / limit)
# [ ] Counter increases correctly
# [ ] Final summary prints after loop
# =====================================================


# =====================================================
# HINT
# =====================================================
# - while True: + break is a common pattern
# - Order of checks matters — "not enough" should
#   come BEFORE updating balance
# =====================================================
