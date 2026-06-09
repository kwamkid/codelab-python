# 📂 Workshops · F1 Session 3 — Math Operators

**Focus:** 7 math operators (`+ − * / // % **`) + PEMDAS + real-world money math

## 🖥️ Workshop Files

| # | File | Description | Time |
|---|------|-------------|------|
| W1 | [workshop_01_simple_calculator.py](workshop_01_simple_calculator.py) | 🧮 Calculator with + − × ÷ | 10 min |
| W2 | [workshop_02_time_converter.py](workshop_02_time_converter.py) | ⏱ Seconds → min + sec (// %) | 15 min |
| Mini | [mini_even_odd.py](mini_even_odd.py) | 🎲 Check even/odd with % | 10 min |
| 🎯 Project | [project_shopping_cart.py](project_shopping_cart.py) | 🛒 Discount + VAT calculator | 25 min |

## 🏠 Homework (2 levels)

| Level | File | Stars |
|-------|------|-------|
| HW1 Required | [hw1_bmi_calculator.py](hw1_bmi_calculator.py) — BMI Calculator | ⭐⭐ |
| HW2 Advanced | [hw2_shopping_cart_v2.py](hw2_shopping_cart_v2.py) — Buy 3 Get 1 (//) | ⭐⭐⭐ |

## 📦 Requirements

None — pure Python only.

## 🧭 Prerequisites

- F1 S2 — input(), int(), float(), casting

## 🔑 Key Concepts

```python
# 7 math operators
10 + 5    # 15      (add)
10 - 3    # 7       (subtract)
4 * 5     # 20      (multiply)
7 / 2     # 3.5     (divide — always float!)
7 // 2    # 3       (floor — drop decimal)  ⭐ NEW
7 % 2     # 1       (remainder)             ⭐ NEW
2 ** 10   # 1024    (power)                 ⭐ NEW

# PEMDAS — order matters
2 + 3 * 4    # 14   (× before +)
(2 + 3) * 4  # 20   (parens override)

# round() — for clean decimals
round(3.7777, 2)   # 3.78
```

## 🎯 Big Idea

`//` and `%` are the **secret weapons** of programming:
- **Time math:** seconds // 60 + seconds % 60
- **Money split:** total // people = each share
- **Even/odd:** n % 2 == 0 = even
- **Page count:** items // page_size
