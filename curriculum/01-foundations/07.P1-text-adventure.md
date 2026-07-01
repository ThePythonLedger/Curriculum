---
id: project-1-text-adventure
title: "Project 1: The Ledger of Fate"
sidebar_label: "🏆 Project 1: Text Adventure"
sidebar_position: 8
---

# 🏆 Project 1: The Ledger of Fate

Congratulations! You have mastered the foundations of Python. You know how to:
1. **Output data** (`print`)
2. **Store data** (`variables`)
3. **Categorize data** (`int`, `str`, `bool`)
4. **Calculate data** (`math`)
5. **Evaluate data** (`if/elif/else`)

Now, it is time to combine them into a single program: a **Text-Based Adventure Game**.

---

### 📜 The Mission
You are trapped in a digital vault. To escape, you must navigate through three "Nodes" by making choices. Your program must track your **Health**, your **Inventory**, and your **Decisions**.

### 🛠️ Requirements
Your code must include the following:
* **At least 3 Variables:** (e.g., `player_name`, `health`, `has_key`).
* **Input handling:** Use `input()` to get choices from the user. 
  *(Note: `input()` always returns a **String**, so remember to compare it to strings like `"1"` or `"left"`!)*
* **Nested Logic:** An `if` statement inside another `if` statement.
* **A Win/Loss Condition:** The game must end with either an "Escape" or a "Game Over" message.

---

### 🏗️ Starter Template

```python interactive
# --- SETUP ---
player_name = input("Enter your name, Traveler: ")
health = 100
has_token = False

print(f"\nWelcome, {player_name}. You wake up in a stone room.")
print("There is a 'left' door and a 'right' door.")

# --- THE FIRST CHOICE ---
choice1 = input("CHOICE 1: Which door do you choose? (left/right): ")

if choice1 == "left":
    print("You find a hallway that leads to another set of doors!")
    choice2 = input("CHOICE 2: Which door do you choose (left/right)")
    # ADD MORE STORY HERE
elif choice1 == "right":
    print("A trap triggers! You lose 50 health. You stumble out and find another set of doors.")
    health = health - 50
    choice2 = input("CHOICE 2: Which door do you choose (left/right)")
    # ADD MORE STORY HERE
else:
    print("You stumble in the dark and find nothing.")

# --- THE FINAL GATE ---
print(f"\nYour current health is: {health}")
if health > 0 and has_token:
    print("You reached the Exit Gate.")
    # Check if they have the token to win ...
else:
    print("GAME OVER: Your journey ends here.")
```

---

### 💡 Tips for a Great Game
* **The "F-String" Trick:** Use `print(f"Health: {health}")` to easily put variables inside your text.
* **Lower Case:** Use `.lower()` on your inputs so that "Left", "LEFT", and "left" all work: `choice = input().lower()`.
* **The "Secret Path":** Add a hidden choice that only happens if a specific variable is exactly a certain number.

---

### 📤 How to Submit
Once your game is working:
1. Copy your code.
2. Go to the **#🚀-showcase** channel in our Discord.
3. Post a snippet of your code and a screenshot of a "Victory" run!

---

## Next Steps
You've built your first engine! Now, we need to learn how to handle **lots** of data at once without creating 100 different variables.