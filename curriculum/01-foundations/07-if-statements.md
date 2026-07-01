---
id: if-statements
title: If Statements
sidebar_label: 7. If Statements
sidebar_position: 7
---

# If Statements: The Fork in the Road

In a real-world ledger, you don't treat every entry the same way. If an account is overdrawn, you flag it. If a payment is massive, you verify it. In Python, we use **Conditional Statements** (`if`, `elif`, and `else`) to control the flow of our program.



### The Basic `if` Statement
The structure of an `if` statement is simple but strict. You provide a condition, followed by a **colon** (`:`). The code that follows must be **indented** (usually 4 spaces).

```python interactive
balance = 100

if balance > 0:
    print("Account is in good standing.")
```

### Adding an `else`
What happens if the condition is `False`? We use the `else` block to provide a backup plan.

```python interactive
balance = -50

if balance > 0:
    print("Account is in good standing.")
else:
    print("WARNING: Negative balance detected!")
```

---

### The `elif` (Else If)
Sometimes you have more than two options. For example, a ledger might have "Positive," "Zero," and "Negative" states. We use `elif` to check multiple specific conditions in order.

```python interactive
balance = 0

if balance > 0:
    print("Profit detected.")
elif balance == 0:
    print("Break even.")
else:
    print("Loss detected.")
```

### ⚠️ The Golden Rule: Indentation
In Python, indentation isn't just for looks—it's part of the grammar. Everything indented under the `if` statement "belongs" to that decision. If you forget to indent, Python will throw an `IndentationError`.



---

### 🏆 The Ledger Challenge: The Security Gate
You are writing a login check for **The Python Ledger** database.

**Task:**
1. Create a variable `username` and set it to a string.
2. Create a variable `is_admin` and set it to a Boolean.
3. Write an `if/elif/else` structure:
   * **IF** the `username` is "Admin" **AND** `is_admin` is `True`, print: "Full Access Granted."
   * **ELIF** the `username` is "Admin" but `is_admin` is `False`, print: "Admin access denied. Check permissions."
   * **ELSE**, print: "Standard User Access Granted."

**Write your code below:**

```python interactive
# 1. Define your variables


# 2. Build your security logic

```

---

<details>
  <summary>📚 Deep Dive</summary>

Official python documentation:
* [Python Docs: More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)

Other resources:
* [Real Python: Conditional Statements in Python](https://realpython.com/python-conditional-statements/)

</details>

## Next Steps
Congratulations! You've mastered the basics of logic. You are now ready for your first **Project**. We will be building a text-based adventure right inside our browser terminal.