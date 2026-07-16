---
id: data-types
title: Data Types
sidebar_label: 4. Data Types
sidebar_position: 4
---

## Introduction: The Ledger Breakdown
Imagine you are running a high-frequency trading platform or auditing a company ledger. You have a customer’s name, "Alice", the quantity of shares they purchased, "100", and the price per share, "150.50".
You attempt to calculate the total transaction value like this:
```python interactive
total = "100" * "150.50"

```
Instead of a calculated financial balance, your system crashes with a fatal TypeError.
To a computer, raw text and numerical values exist in entirely different universes. If you cannot explicitly control and understand the format of your data, your applications will experience silent failures or outright crashes. In this lesson, we will look under the hood of Python’s memory manager to understand how primitive data types are stored and kept secure.
## Learning Outcomes
By the end of this lesson, you will confidently be able to:
 * Identify and define Python’s four primary primitive types: str, int, float, and bool.
 * Explain the mental model of **dynamic typing** and **object references** in memory.
 * Utilize Python's type() and id() functions to inspect and trace variables at runtime.
## Conceptual Overview: Under the Hood of Python’s Memory
In many programming languages (like C++ or Java), a variable is a named "box" that holds a specific type of value. Once you declare a box is for integers, it can *only* hold integers.
Python operates differently. In Python, **variables are pointers (or references) to objects in memory.**
When you write x = 42, Python:
 1. Allocates space in memory for an **integer object** and stores the value 42 inside it.
 2. Creates a reference named x that points directly to that memory location.
Every single thing in Python is an object, managed by a underlying structure (in the standard CPython implementation, this is a C struct called PyObject). This struct contains two vital pieces of metadata:
 * **A Reference Count:** How many variables are currently pointing to this object.
 * **A Type Pointer:** An internal marker telling Python what kind of data this object contains (e.g., a string, an integer).
Because of this type pointer, Python knows exactly what data type it is dealing with at runtime. This is called **Dynamic Typing**. You don't have to tell Python that x is an integer; Python figures it out by inspecting the object that x is pointing to.
### The Four Core Primitives
To write robust code, you must master the four fundamental types of objects Python manages:
| Type | Name | Purpose | Example |
|---|---|---|---|
| **String** (str) | Text sequence | Storing alphanumeric characters (immutable) | name = "Alice" |
| **Integer** (int) | Whole numbers | Countable values with arbitrary precision | shares = 100 |
| **Float** (float) | Floating-point | Decimal values (IEEE 754 standard) | price = 150.50 |
| **Boolean** (bool) | Logical states | Truth evaluations (True or False) | is_active = True |
### Inspecting Your Objects: type() and id()
Because variables are just references pointing to memory, Python provides built-in tools to inspect them:
 * Use **type(variable)** to find out what class of object the variable is pointing to.
 * Use **id(variable)** to retrieve the unique integer address of the object in memory.
```python interactive
# Inspecting variables and their identities
client = "Alice"
print(type(client))
print(id(client))

```
## Assignments
Read and analyze the following resources to prepare for the knowledge checks:
 1. **Python Official Docs: Built-in Types**
   * Python Standard Library: Built-in Types
   * *Focus Guidance:* Concentrate deeply on **Section 4.1 (Numeric Types)** and **Section 4.8 (Sequence Types)**. Pay close attention to how floats and integers behave.
 2. **Real Python: Variables in Python**
   * Real Python: Variables in Python (Object References)
   * *Focus Guidance:* Carefully read the section titled **"Object References"** and **"Object Identity"** to cement your understanding of how variables act as pointers in memory.
## Knowledge Checks
> ⚠️ **Prerequisite Check:** You must find the answers to these questions in the assignment links above before proceeding to the ledger challenge. Do not look for them in the lesson text!
> 
 1. If you declare x = 5 and then reassign x = 6, does Python modify the original integer object in place, or does it point x to a brand-new object in memory? Explain how this relates to "immutability."
 2. Booleans in Python are actually a subclass of another primitive type. What is this underlying type, and how does Python represent True and False numerically?
 3. Why is it highly discouraged to use standard float data types to store exact monetary balances in financial software? What specific standard or problem causes floats to be imprecise?
## 🏆 The Ledger Challenge: Asset Initialization
For your third audit task, you must initialize the state of a financial asset in our ledger.
### Instructions
 1. Create four variables exactly as specified in the template code:
   * asset_name assigned to a string.
   * units assigned to an integer.
   * market_price assigned to a float.
   * is_tradable assigned to a boolean.
 2. Print out the data type of market_price using Python's built-in inspection tool.
 3. Print out the unique memory identity of asset_name.
> 💡 **Documentation Hunting Tip:** If you can't remember the name of the function that returns the unique memory location of an object, review the **"Object Identity"** section of the Real Python assignment linked above.
> 
```python interactive
# 1. Initialize your variables here with appropriate values
asset_name = None
units = None
market_price = None
is_tradable = None

# 2. Print the type of market_price


# 3. Print the memory identity (ID) of asset_name


```
## Next Steps
Now that we have mapped out how data is represented and referenced in memory, we can begin manipulating it. In the next lesson, we will explore **Basic Operators** to see how Python performs calculations on these types—and how to avoid type errors along the way.
