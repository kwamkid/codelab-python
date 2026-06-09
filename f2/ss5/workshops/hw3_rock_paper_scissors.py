# =====================================================
# 🪨📄✂️ HW3 — Rock Paper Scissors (⭐⭐⭐⭐⭐ Expert)
# Python Foundation 2 · Session 5 · While Loops + random
# =====================================================
# 🎯 Play 5 rounds vs computer. Track wins/losses/ties.
# ⏱️  TIME: 30 minutes
# 🔑 SKILL: for + random.choice + if-elif + counting
# =====================================================

import random

print("🪨📄✂️  Rock Paper Scissors!")
print("=" * 35)
print("Best of 5 rounds — let's play!")
print()


# 📝 TODO 1: Setup
moves = ["rock", "paper", "scissors"]
my_wins   = 0
cpu_wins  = 0
ties      = 0


# 📝 TODO 2: Loop 5 rounds (for is fine here — known count)
for round_num in range(1, ___):

    print(f"\n--- Round {round_num} ---")

    # Get player's move (lowercase to be safe)
    my_move = input("Your move (rock/paper/scissors)? ").___()

    # Computer picks randomly
    cpu_move = random.___(moves)
    print(f"🤖 chose: {cpu_move}")

    # Decide who wins (if-elif)
    if my_move == cpu_move:
        print("🤝 Tie!")
        ties += 1
    elif (my_move == "rock"     and cpu_move == "scissors") or \
         (my_move == "paper"    and cpu_move == "rock")     or \
         (my_move == "scissors" and cpu_move == "paper"):
        print("✅ You win!")
        my_wins += ___
    else:
        print("❌ Computer wins!")
        cpu_wins += ___


# 📝 TODO 3: Final score
print()
print("=" * 35)
print("📊 FINAL SCORE")
print("=" * 35)
print(f"  You    : {my_wins} 🏆")
print(f"  Ties   : {ties} 🤝")
print(f"  CPU    : {cpu_wins} 🤖")

# 📝 TODO 4: Announce winner
if my_wins > cpu_wins:
    print("\n🎉 You're the champion!")
elif cpu_wins > my_wins:
    print("\n🤖 Computer wins this time!")
else:
    print("\n🤝 It's a draw!")


# =====================================================
# 📋 EXAMPLE INTERACTION:
# =====================================================
# 🪨📄✂️  Rock Paper Scissors!
# ===================================
# Best of 5 rounds — let's play!
#
# --- Round 1 ---
# Your move (rock/paper/scissors)? rock
# 🤖 chose: scissors
# ✅ You win!
#
# --- Round 2 ---
# Your move? paper
# 🤖 chose: paper
# 🤝 Tie!
#
# ... (5 rounds)
#
# ===================================
# 📊 FINAL SCORE
# ===================================
#   You    : 3 🏆
#   Ties   : 1 🤝
#   CPU    : 1 🤖
#
# 🎉 You're the champion!
# =====================================================


# =====================================================
# 🎁 BONUS 1: Use WHILE — play until someone gets 3 wins
# =====================================================
# while my_wins < 3 and cpu_wins < 3:
#     # play one round
#     # update my_wins or cpu_wins
# # First to 3 wins! (best of 5)


# =====================================================
# 🎁 BONUS 2: Validate user input
# =====================================================
# while my_move not in moves:
#     my_move = input("Choose rock/paper/scissors: ").lower()
#     if my_move not in moves:
#         print("⚠️  Invalid choice!")


# =====================================================
# 🎁 BONUS 3: Add lizard + spock (Big Bang Theory style!)
#   moves = ["rock", "paper", "scissors", "lizard", "spock"]
#   ... new rules!
# =====================================================


# =====================================================
# 🔗 SUBMIT:
#   Trinket link OR screenshot → LINE group
#   🏠 Beat your parent in best of 5!
# =====================================================
