---
id: comparisons
title: Comparison Operators
sidebar_label: 6. Comparisons
sidebar_position: 6
---

# Comparisons: Auditing the Ledger

Programming isn't just about math; it's about making decisions. To make a decision, the computer needs to compare two values. The result of any comparison is always a **Boolean** (`True` or `False`).



### The Comparison Operators
In Python, we use these symbols to "audit" our data:

* `==` **Equal to:** Checks if two values are the same. (Note: Double `==` is for comparing; single `=` is for assigning!)
* `!=` **Not equal to:** Checks if two values are different.
* `>` **Greater than** / `<` **Less than**
* `>=` **Greater than or equal to** / `<=` **Less than or equal to**

```python interactive
# Try running these comparisons
print(10 == 10)  # True
print(10 != 5)   # True
print(10 < 5)    # False
print(10 >= 10)  # True
```

---

### Comparing Strings
You can also compare text! Python checks strings character by character. Note that capitalization matters: `"Python"` is **not** the same as `"python"`.

```python interactive
stored_password = "Secret123"
entered_password = "secret123"

print(stored_password == entered_password) # False
```

---

### Logic Gates: `and`, `or`, and `not`
Sometimes a single comparison isn't enough. You might need to check if a user has enough money **AND** if the store is open.

1. **`and`**: Returns `True` only if **both** sides are True.
2. **`or`**: Returns `True` if **at least one** side is True.
3. **`not`**: Flips the result (`True` becomes `False`).



[Image of a logic gate truth table for AND, OR, and NOT operations]


```python interactive
age = 20
has_id = True

# Can they enter?
print(age >= 18 and has_id) # True
```

---

### 🏆 The Ledger Challenge: The Overdraft Check
You are writing a script to see if a transaction should be approved.

**Task:**
1. Create a variable `account_balance` and set it to `500`.
2. Create a variable `withdrawal_amount` and set it to `600`.
3. Create a variable `is_overdraft_protected` and set it to `True`.
4. Create a variable `can_withdraw`. This should be `True` if:
   * The `account_balance` is greater than or equal to the `withdrawal_amount`.
   * **OR** if `is_overdraft_protected` is `True`.
5. Print `can_withdraw`.

**Write your code below:**

```python interactive
# 1. Define your variables


# 2. Check the logic


# 3. Print the result

```

---

<details>
  <summary>📚 Deep Dive</summary>

Other resources:
* [W3Schools: Python Operators](https://www.w3schools.com/python/python_operators.asp)
* [Real Python: Python Booleans: Optimize Your Code With Truth Values](https://realpython.com/python-boolean/)

</details>

## Next Steps
Now that we can compare values, we can finally tell Python to **act** on those results using **If Statements**.