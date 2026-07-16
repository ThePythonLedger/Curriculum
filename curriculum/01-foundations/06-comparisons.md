---
id: comparisons
title: Comparison Operators
sidebar_label: 6. Comparisons
sidebar_position: 6
---

## Introduction: The Cost of a False Ledger

Imagine running a high-frequency financial ledger where every microsecond represents thousands of dollars in transactions. A user requests a withdrawal of $100. Their account balance sits at exactly $100. Do you approve the transaction? 

Now imagine they request $100.01. If your system relies on a sloppy calculation or incorrect evaluation, you risk overdrawing the account and losing capital. 

Computers do not make "judgment calls." At the hardware level, every complex decision-from routing internet traffic to approving a multi-million dollar bank transfer-boils down to binary logic. In this lesson, we will transition from simply storing data to auditing it, evaluating conditions to yield strict, binary truths: `True` or `False`.

---

## Learning Outcomes

By the end of this lesson, you will confidently be able to:
* **Evaluate expressions** using Python's comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`).
* **Explain how Python compares non-numeric data types** (like strings) using Unicode values under the hood.
* **Construct complex logical expressions** by chaining comparisons with boolean operators (`and`, `or`, `not`).
* **Analyze short-circuit evaluation** to predict how Python optimizes logical checks.

---

## Conceptual Overview: The Anatomy of Truth

Every comparison you write in Python is an expression that evaluates to a single primitive value: a **Boolean** (`True` or `False`). 

### How Python Evaluates Value vs. Identity
When we use the equality operator (`==`), we are asking Python to check if two values are equivalent. This is known as **value equality**.

```python
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)  # True (They contain the same values)

```
Behind the scenes, Python evaluates the data stored at the memory addresses of these variables. While they are distinct objects in memory, their contents are identical.


### String Comparisons and Lexicographical Order

When you compare strings using `<` or `>`, Python doesn't look at the length of the string. Instead, it compares them **lexicographically** (character by character) using their **Unicode code points** (integer values assigned to every character).


Because uppercase letters have lower Unicode values than lowercase letters (e.g., "A" is 65, while "a" is 97), Python evaluates `"Python" == "python"` as `False`, and `"Apple" < "banana"` as `True`.


### Boolean Logic and Short-Circuit Evaluation
Python’s logical operators (and, or, not) allow us to chain multiple conditions together. However, Python is lazy in a highly efficient way called **short-circuit evaluation**:
 * **and evaluation**: If the left side of an and expression is False, the entire expression *must* be False. Python won't even look at the right side.
 * **or evaluation**: If the left side of an or expression is True, the entire expression *must* be True. Python stops evaluating immediately.


Understanding this "short-circuiting" behavior is vital for writing clean, error-free code (such as checking if an object is not None *before* checking its properties).


```python interactive
# Try running these basic comparisons in our interactive environment
print("Python" == "python")  # Capitalization matters!
print(10 >= 10.0)            # Floats and integers can be compared directly
print(True or False)         # Short-circuits: stops at True

```

## Assignments

To fully grasp how Python handles these evaluations under the hood, read through these curated resources:
 1. **Python Official Docs: Comparisons**
   * *Focus Guidance:* Read Section 6.10. Focus deeply on how different types are compared and how value comparisons behave across numeric types.
 2. **Real Python: Operators and Expressions in Python**
   * *Focus Guidance:* Read the sections on "Comparison Operators" and "Logical Operators". Pay close attention to how "truthiness" is evaluated in non-boolean objects.
 3. **PEP 285: Adding a True/False Type**
   * *Focus Guidance:* Read the "Motivation" section to understand why Booleans were introduced to Python as a subclass of integers.


## Knowledge Checks
Before writing any code, you must be able to answer these questions. Use the assignment links above to track down the answers—you won't find them explicitly spelled out in the text!
 1. If Booleans in Python are a subclass of integers, what is the exact integer value of True and False when used in arithmetic operations?
 2. What is the behavior of the is operator compared to the == operator? Why is it dangerous to use is for value comparison?
 3. How does Python's short-circuit evaluation prevent a ZeroDivisionError in this specific statement: (x == 0) or (1 / x > 1)?
 4. How does Python evaluate the comparison of two tuples, such as (1, 2, 3) < (1, 2, 4)?


## 🏆 The Ledger Challenge: The Overdraft Check
In a financial system, an overdraft check determines whether a transaction can proceed. You must write the evaluation logic for a basic transaction processor.

### Your Task
Write a script that decides if a transaction is approved (can_withdraw) based on two conditions:
 1. The user must have a sufficient account_balance to cover the withdrawal_amount.
 2. **OR**, the user must have overdraft protection active (is_overdraft_protected is True).


### Documentation Hunting Tip
When chaining complex boolean expressions, operator precedence dictates how Python groups your operations. Look up **"Python Operator Precedence"** in the Python Docs to determine if you need to use parentheses () to force certain comparisons to run before others.


```python interactive
# 1. Define your initial state
account_balance = 500
withdrawal_amount = 600
is_overdraft_protected = True

# 2. Check the logic (Replace 'None' with your boolean expression)
can_withdraw = None

# 3. Print the result (Should output 'True' given the variables above)
print("Transaction approved:", can_withdraw)

```
## Next Steps
Now that we can evaluate conditions and audit our data, we need a way to make our program branch off and execute different blocks of code based on those truths. In the next lesson, we will explore **Conditional Control Flow (if, elif, else)** to give our scripts decision-making power.
```

