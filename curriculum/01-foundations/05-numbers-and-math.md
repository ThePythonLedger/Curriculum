---
id: numbers-and-math
title: Numbers and Math
sidebar_label: 5. Numbers and Math
sidebar_position: 5

---

# Numbers and Math: Balancing the Ledger

A ledger is useless if you can't add up the totals. In Python, we use **Arithmetic Operators** to perform calculations. Since you already know about Integers and Floats, let's see how they interact.



### The Basic Operators
Most of these look exactly like the math you learned in school:
* `+` **Addition:** `5 + 2` is `7`
* `-` **Subtraction:** `5 - 2` is `3`
* `*` **Multiplication:** `5 * 2` is `10`
* `/` **Division:** `5 / 2` is `2.5` (Note: Division *always* results in a **Float**)

### The "Special" Operators
Python has a few tools that are specific to programming:

1. **Floor Division (`//`):** Divides and chops off the decimal. `5 // 2` is `2`.
2. **Exponent (`**`):** Raises a number to a power. `5 ** 2` is `25`.
3. **Modulo (`%`):** Returns the **remainder** of a division. `5 % 2` is `1` (because 2 goes into 5 twice, with 1 left over).

```python interactive
# Try these out!
print(10 / 3)   # Normal Division
print(10 // 3)  # Floor Division
print(10 % 3)   # Modulo (The Remainder)
print(2 ** 3)   # 2 to the power of 3
```

---

### Order of Operations
Python follows the standard mathematical order of operations, often remembered by the acronym **PEMDAS** (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction).



When in doubt, use **parentheses** to make your intentions clear to the computer:

```python interactive
result_one = 5 + 2 * 10    # Becomes 25
result_two = (5 + 2) * 10  # Becomes 70

print(result_one)
print(result_two)
```

---

### 🏆 The Ledger Challenge: The Interest Calculator
You are calculating the final balance of a ledger entry after a year of 5% interest.

**Task:**
1. Create a variable `principal` and set it to `1000`.
2. Create a variable `interest_rate` and set it to `0.05`.
3. Create a variable `total` that calculates the final amount using the formula:
   $$Total = principal + (principal \times interest\_rate)$$
4. Print the `total`.

**Bonus:** Use the `int()` function to print only the whole number part of the total!

**Write your code below:**

```python interactive
# 1. Define your variables


# 2. Calculate the total


# 3. Print the result

```

---

<details>
  <summary>📚 Deep Dive</summary>

Other resources:
* [Python Docs: Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
* [Programiz: Python Operators](https://www.programiz.com/python-programming/operators)

</details>

## Next Steps
Calculations are great, but a ledger needs to make decisions. In the next lesson, we’ll learn how to compare values using **Booleans and Comparison Operators**.