---
id: numbers-and-math
title: Numbers and Math
sidebar_label: 5. Numbers and Math
sidebar_position: 5

---

## Introduction: The Cost of a Fraction
In financial auditing, tiny calculation errors don't just disappear—they compound. Imagine calculating daily interest accrued across 10,000 corporate investment accounts. 

If your code rounds a fraction of a cent incorrectly, a multi-million dollar ledger will suddenly show a massive, unaccounted deficit by the end of the fiscal year.


Computers do not think like humans, and they do not store numbers the way we write them on paper. To build a reliable financial ledger, you must understand how Python represents numbers under the hood and how to control its arithmetic engine with absolute precision.


## Learning Outcomes
By the end of this lesson, you will confidently be able to:
 * **Differentiate** between how Python represents integers and floating-point numbers in memory.
 * **Apply** specialized operators (modulo, floor division, and exponents) to solve practical business logic problems.
 * **Predict** the execution order of complex mathematical expressions using Python's operator precedence rules.
 * **Cast** numeric types to enforce specific formatting and data integrity.
## Conceptual Overview: Under the Hood
To the untrained eye, 5 and 5.0 represent the same value. To Python's memory manager, they are entirely different beasts.
### Integers vs. Floats in Memory
 * **Integers (int):** Python handles integers with **arbitrary precision**. This means Python dynamically allocates memory to store integers of virtually any size. Your only limit is your physical computer memory.
 * **Floating-Point Numbers (float):** Floats are stored using the **IEEE 754 double-precision binary standard**. Because computers operate in binary (base-2) and we write decimals in base-10, certain fractions cannot be represented exactly in memory. This leads to subtle rounding anomalies that every developer must expect and plan for.


### Division & The Operators
Python provides two distinct forms of division to handle different structural needs:
 * **True Division (/):** Always returns a floating-point number, even if the numbers divide perfectly (e.g., 4 / 2 evaluates to 2.0).
 * **Floor Division (//):** Divides the numbers and rounds *down* to the nearest whole integer, discarding the remainder.
 * **Modulo (%):** Calculates the remainder of a division. In a ledger system, this is incredibly useful for batch processing (e.g., triggered events every N entries) or determining if a value is perfectly divisible.

```python interactive
# Observe the structural difference in output types:
print("True Division:", 10 / 2)
print("Floor Division:", 10 // 3)
print("Modulo Remainder:", 10 % 3)

```

### Execution Context (Operator Precedence)

Python evaluates mathematical expressions using a strict hierarchy, closely mimicking the mathematical rules of **PEMDAS** (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction). If you write ambiguous math, Python will resolve it based on its internal precedence table.
> **Rule of Thumb:** Never force a colleague to guess your operator precedence. Use parentheses () to explicitly define your execution contexts.
> 


## Assignments

Expand your understanding by exploring these curated external resources.
 * **Python Standard Library:** Built-in Numeric Types
   *Focus closely on Section 4.4.1 to understand how integers and floats behave, and pay special attention to the footnotes regarding float limitations.*
 * **Real Python:** Numbers in Python
   *Focus deeply on the section titled "Floating-Point Representation Problems" to see why fractional binary representations can drift.*
 * **Python PEPs:** PEP 238 – Changing the Division Operator
   *Read the "Rationale" section to understand why Python developers intentionally split the division operator into / and // in Python 3.*


## Knowledge Checks
Before writing code for the challenge, ensure you can thoroughly explain the following:
 1. Why does evaluating 0.1 + 0.2 in standard Python floating-point math not equal exactly 0.3?
 2. In corporate finance software, why is standard float representation avoided, and what built-in Python module is used to solve this? (Hint: You'll need to dig into the assignments to find this!).
 3. How does Python's modulo operator (%) behave differently from other languages (like C or Java) when handling negative numbers?


## 🏆 The Ledger Challenge: The Interest Calculator
Let's put your math skills to work on a ledger balance. You need to calculate the final balance of a ledger entry after a year of earning interest, and then truncate the decimal to prepare the data for an integer-only legacy database.
### Task:
 1. Create a variable principal and set it to 1000.
 2. Create a variable interest_rate and set it to 0.05 (representing 5%).
 3. Calculate the total accrued amount using the standard compound interest formula:
 4. Cast the final result to an integer (discarding the decimal) and print it.
> **Documentation Hunting Tip:** > When converting types, Python's built-in conversion functions share their names with the data types themselves. If you need to convert a float to an integer, search for the built-in function that shares its name with the int data type.
> 

```python interactive
# 1. Define your variables (principal and interest_rate)


# 2. Calculate the total accrued balance


# 3. Cast the total to an integer and print the result


```

## Next Steps

Performing basic calculations is a crucial step, but a ledger is useless if it cannot make decisions based on those calculations. In the next lesson, we will explore how to evaluate balances and compare values using **Booleans and Comparison Operators**.
