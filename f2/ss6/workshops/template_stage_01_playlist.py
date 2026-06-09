# =====================================================
# Stage 1 — Playlist Mayhem
# Python Foundation 2 - Session 6 - Survival Challenge
# =====================================================
# GOAL: Review list operations from S1-S2
#       (append, remove, slicing, in)
# TIME: 15 minutes
# SKILL: list methods, slicing, for loop
# =====================================================

# SETUP: starting playlist (8 mixed songs)
playlist = [
    "rainy heart [sad]",
    "rock anthem",
    "lonely night [sad]",
    "pump it up",
    "tears in rain [sad]",
    "feeling alive",
    "energy boost",
    "broken dreams [sad]",
]

print("--- Starting Playlist ---")
for song in playlist:
    print(f"  - {song}")
print(f"Total: {len(playlist)} songs\n")


# =====================================================
# TASK 1: Add 3 upbeat songs (append)
# Hint: use .append() 3 times — any song you like!
# =====================================================
playlist.append(___)   # <-- upbeat song #1
playlist.append(___)   # <-- upbeat song #2
playlist.append(___)   # <-- upbeat song #3


# =====================================================
# TASK 2: Remove all songs that contain "[sad]"
# Hint: loop through the list, build a new one without "[sad]"
#       (do not use .remove() directly — list will shift)
# =====================================================
playlist_happy = []
for song in playlist:
    if "[sad]" ___ song:    # <-- not in (keep songs WITHOUT "[sad]")
        playlist_happy.___(song)   # <-- append to playlist_happy

playlist = playlist_happy   # update main playlist


# =====================================================
# TASK 3: print Top 5 (slicing)
# Hint: use [:5]
# =====================================================
print("--- Top 5 After Cleanup ---")
top_5 = playlist[___]   # <-- slice first 5
for i, song in enumerate(top_5, start=1):
    print(f"  {i}. {song}")


# =====================================================
# TASK 4 (BONUS): check if your favorite song is in playlist
# =====================================================
my_favorite = ___   # <-- one of the songs you added in TASK 1
if my_favorite in playlist:
    print(f"\nFound favorite '{my_favorite}' in playlist!")
else:
    print(f"\nNot found: '{my_favorite}' (check spelling)")


# =====================================================
# EXPECTED OUTPUT (example):
# =====================================================
# --- Starting Playlist ---
#   - rainy heart [sad]
#   - rock anthem
#   ... (8 songs)
# Total: 8 songs
#
# --- Top 5 After Cleanup ---
#   1. rock anthem
#   2. pump it up
#   3. feeling alive
#   4. energy boost
#   5. [upbeat song #1]
#
# Found favorite 'xxx' in playlist!
# =====================================================


# =====================================================
# KEY IDEAS reviewed
# =====================================================
# - .append(x)         add x to end of list
# - .remove(x)         remove first occurrence of x
# - list[a:b]          slicing — from index a to b-1
# - list[:5]           first 5 items
# - for x in list      loop over every item
# - x in list          check membership (True/False)
# - not in             opposite of in
# =====================================================
