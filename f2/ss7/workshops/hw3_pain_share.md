# 🔥 HW3 — Feel the Pain, Then Share It

> Required for everyone · ~20 minutes total · Combines pedagogy + share

---

## Two Parts

### Part A — Feel the Pain (15 minutes)
Calculate the price of 5 menu items by **copy-pasting** the same logic 5 times.
You MUST write all 5 blocks by hand. **NO function. NO AI. NO shortcut.**

### Part B — Share the Pain (5 minutes)
Screenshot your repetitive code and share it with someone special.
Tell them: "Next week we'll learn how to fix this!"

---

## Part A — The 5-Dish Menu Calculator

### Setup

Open a new file: `hw3_pain.py`

Use this menu:
| # | Dish | Price | Quantity |
|---|---|---|---|
| 1 | Khao Mun Gai | 60 | 2 |
| 2 | Pad Thai | 80 | 1 |
| 3 | Som Tam | 50 | 3 |
| 4 | Tom Yum | 120 | 1 |
| 5 | Iced Tea | 35 | 4 |

### Formula (same for every dish)

```
subtotal = price * quantity
vat      = subtotal * 0.07
discount = subtotal * 0.10
total    = subtotal + vat - discount
```

### Output for each dish

```
Khao Mun Gai: subtotal=120.00, vat=8.40, discount=12.00, total=116.40
```

### And at the end

```
========================================
GRAND TOTAL: ___.__
========================================
```

### Rules

- Write 5 SEPARATE blocks (one per dish)
- No `def`, no `for` loop over items, no list comprehension, no AI
- Use clear variable names: `total_1`, `total_2`, etc.

---

## Part B — Share Time

### Step 1 — Take a screenshot

Take a clear screenshot of your code that shows:
- All 5 repeated blocks visible (or at least 3)
- The "GRAND TOTAL" line

### Step 2 — Open LINE chat with someone special

(parent / best friend / sibling / cousin / grandparent — pick one)

### Step 3 — Send the screenshot + this message

```
Today in coding class, the teacher made me write the same
thing 5 times! I'm so tired of copy-paste.
Next session we'll learn "Functions" to make this short.
Bet you a snack I can make it 5x shorter next week!
```

### Step 4 — Save proof

- Wait for their reply
- Screenshot the conversation (your message + their reply)
- Show this to the teacher next class

---

## Criteria

- [ ] Part A: 5 repeated blocks written by hand
- [ ] Part A: GRAND TOTAL is correct
- [ ] Part A: No `def`, no AI used
- [ ] Part B: Screenshot sent to someone special
- [ ] Part B: They replied (any reply counts)
- [ ] Conversation screenshot saved to show teacher

---

## Why This HW Exists

This is not a normal homework. The **pain** of copy-pasting is the **whole point**.

When we learn Functions next session, you'll feel:
> "Wait — the same problem fits in 8 lines instead of 40?? Why didn't we just do this from the start?!"

That feeling = the moment Functions become **meaningful**, not just a syntax rule.

Most people learn `def` and forget. You'll never forget — because you'll remember the 5-Dish Pain.

---

## Bonus Stars

- They reply within 1 hour -> ⭐
- They ask "what's a function?" -> ⭐⭐
- They share it back to their friend -> ⭐⭐⭐
