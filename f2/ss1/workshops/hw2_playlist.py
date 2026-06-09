# =====================================================
# 🎵 HW2 — My Playlist (⭐⭐⭐ Advanced)
# Python Foundation 2 · Session 1 · Lists Intro
# =====================================================
# 🎯 Build playlist of YOUR favorite songs.
#    Add 5+, remove 1, check if a song is in the list.
# ⏱️  TIME: 20-25 minutes
# =====================================================

playlist = []


# 📝 TODO 1: Add YOUR 5 favorite songs
playlist.append("🎵 ___")     # song 1
playlist.append("🎵 ___")     # song 2
playlist.append("🎵 ___")
playlist.append("🎵 ___")
playlist.append("🎵 ___")

print("🎧 My Playlist:")
for i, song in enumerate(playlist, start=1):
    print(f"  {i}. {song}")


# 📝 TODO 2: Remove 1 song
print()
playlist.remove("___")    # name a song to remove


# 📝 TODO 3: Check if a song is in playlist
print(f"\nHas 'Pink Venom'? {'Pink Venom' in playlist}")
print(f"Has 'Old MacDonald'? {'Old MacDonald' in playlist}")


# 📝 TODO 4: Print final stats
print(f"\nTotal songs: {len(playlist)}")


# =====================================================
# 📋 EXAMPLE OUTPUT:
# =====================================================
# 🎧 My Playlist:
#   1. 🎵 Pink Venom
#   2. 🎵 Dynamite
#   3. 🎵 Shake It Off
#   4. 🎵 Perfect
#   5. 🎵 24K Magic
#
# Has 'Pink Venom'? True
# Has 'Old MacDonald'? False
#
# Total songs: 4
# =====================================================


# =====================================================
# 🎁 BONUS 1: Don't allow duplicates
# =====================================================
# new_song = input("Add a song: ")
# if new_song in playlist:
#     print("Already in playlist!")
# else:
#     playlist.append(new_song)


# =====================================================
# 🎁 BONUS 2: Print only songs starting with a letter
# =====================================================
# letter = input("Letter? ").upper()
# for song in playlist:
#     if song.upper().startswith(letter):
#         print(f"  ⭐ {song}")


# =====================================================
# 🔗 SUBMIT:
#   Trinket link → LINE group
#   🏠 Share with parents — show your music taste!
# =====================================================
