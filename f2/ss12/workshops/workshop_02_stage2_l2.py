# ═══════════════════════════════════════════════════════════
# 🎤 ด่าน 2 · Functions + String — Showcase L2 (โจทย์สด 15 นาที)
# F2 Session 12 · Grand Showcase Level 2
# ═══════════════════════════════════════════════════════════

# โจทย์ 1: function นับสระในคำ (function + string + loop)
def count_vowels(word):
    count = 0
    for ch in word.lower():
        if ch in "aeiou":
            count += 1
    return count

print(count_vowels("CodeLab"))   # 3

# โจทย์ 2: function กลับคำ (string)
def reverse(word):
    result = ""
    for ch in word:
        # TODO: ต่อ ch ไว้ข้างหน้า
        result = ____            # 👈 แก้: ch + result
    return result

print(reverse("hello"))          # olleh
