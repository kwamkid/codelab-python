# =====================================================
# HW2 — Boss Battle V2: Score System
# Python Foundation 2 - Session 6 - Survival Challenge
# =====================================================
# GOAL: Extend Boss Battle with a scoring system + multi-round
# TIME: 30 minutes
# LEVEL: Advanced (optional)
# =====================================================
# SPEC:
#
# 1. SCORING:
#    - 1 try  -> 100 points
#    - 2 tries -> 90 points
#    - 3 tries -> 80 points
#    - ... drops by 10 each try
#    - 10+ tries -> 10 points (does not go negative)
#
# 2. PLAY 3 ROUNDS:
#    - Round 1, 2, 3
#    - Track high_score throughout (max)
#
# 3. AT THE END:
#    - print results of all 3 rounds
#    - print "HIGH SCORE: ___"
# =====================================================


import random


# =====================================================
# PART 1: function to calculate score
# =====================================================
# Hint: use if-elif chain, or formula: max(110 - count*10, 10)

def calc_score(count):
    """Take number of tries, return score."""
    # write here
    pass


# =====================================================
# PART 2: function to play one round
# =====================================================
# Returns the number of tries

def play_one_round(round_number):
    """Play one game, return count."""
    print(f"\n---- ROUND {round_number} ----")
    secret = random.randint(1, 100)
    count = 0
    # write the game loop here
    pass


# =====================================================
# PART 3: main — play 3 rounds + track high score
# =====================================================
# Hint:
#   high_score = 0
#   for round in range(1, 4):
#       count = play_one_round(round)
#       score = calc_score(count)
#       if score > high_score:
#           high_score = score

# write main here


# =====================================================
# EXPECTED OUTPUT (example):
# =====================================================
# ---- ROUND 1 ----
# Guess 1-100: 50
# Too high!
# Guess 1-100: 25
# Too low!
# Guess 1-100: 37
# You got it in 3 tries! -> 80 points
#
# ---- ROUND 2 ----
# ... (new game)
#
# ---- ROUND 3 ----
# ... (new game)
#
# =======================
# HIGH SCORE: 90
# =======================
# =====================================================


# =====================================================
# HINTS
# =====================================================
# - Functions start with: def name(params):
# - Return a value with: return x
# - High Score = max of all 3 rounds
# - Use if-elif for calc_score, or formula with max()
# =====================================================


# =====================================================
# EXTRA CHALLENGE (if you have time left)
# =====================================================
# - Ask difficulty (easy: 1-50, hard: 1-1000)
# - Adjust scoring formula by difficulty
# - Save high score to a .txt file (no file I/O lesson
#   yet — figure it out from docs.python.org)
# =====================================================
