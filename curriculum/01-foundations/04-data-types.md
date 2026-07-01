---
id: data-types
title: Data Types
sidebar_label: 4. Data Types
sidebar_position: 4
---

# Data Types: Sorting the Ledger

Not all data is created equal. You can't multiply a "Name" by a "Phone Number," and you can't capitalize a "Price." To keep your code from crashing, you must understand the four fundamental **Data Types** in Python. These are also called **primitive** data types.


### 1. Strings (`str`)
As we saw in Lesson 2, these are sequences of characters wrapped in quotes.
* **Example:** `"Hello"`, `'12345'`, `"Python_Ledger_v1"`
* **Use for:** Names, addresses, or any text.

### 2. Integers (`int`)
These are whole numbers with no decimal point. 
* **Example:** `10`, `-5`, `1000000`
* **Use for:** Counting items, ages, or quantities.

### 3. Floats (`float`)
Short for "floating-point numbers," these are numbers that contain a decimal point.
* **Example:** `10.5`, `-0.01`, `3.14`
* **Use for:** Prices, percentages, or precise measurements.

### 4. Booleans (`bool`)
These represent logical values: either **True** or **False**. Note the capital letters!
* **Example:** `True`, `False`
* **Use for:** Checking if a user is logged in, if a task is finished, or if a price is too high.

### The `type()` Inspector
If you ever get confused about what is inside a variable, Python provides a built-in magnifying glass: the `type()` function.

```python interactive
# Try running this to see the types!
name = "Alice"
age = 25
price = 19.99
is_coding = True

print(type(name))
print(type(age))
print(type(price))
print(type(is_coding))
```

### Dynamic Typing: The Python Superpower
In some languages, you have to tell the computer exactly what type a variable is. In Python, the computer figures it out automatically based on the value you provide. This is called **Dynamic Typing**.

### 🏆 The Ledger Challenge: Inventory Audit
You are auditing your supply of "Coding Fuel."

**Task:**
1. Create a variable `item_name` and assign it a **String** (e.g., "Coffee").
2. Create a variable `quantity` and assign it an **Integer** (e.g., 5).
3. Create a variable `price_per_unit` and assign it a **Float** (e.g., 3.50).
4. Create a variable `in_stock` and assign it a **Boolean** (`True` or `False`).
5. Print all four variables.

**Write your code below:**

```python interactive
# 1. Define your four data types here


# 2. Print them out to check your work

```

---

<details>
  <summary>📚 Deep Dive</summary>

Primitive data types represent the smallest possible unit of information that can be stored.
In python, these are the ones listed above, as well as `complex` which is used for scientific calculations and wont be part of this course. 

To learn more about primitive data types in python, visit:
* [Official python documentation](https://docs.python.org/3/library/stdtypes.html#built-in-typ)

Other resources:
* [Geomar.de: Primitive Data Types](https://2025-pherwiss-2-945e87.pages.geomar.de/content/02_python_basics/04_primitive_data_types.html)
* [Pieriantraining.com: Python primitive data types - a comprehensive tutorial](https://pieriantraining.com/python-primitive-data-types-a-comprehensive-tutorial/)

</details>

## Next Steps
Now that we know the types, it's time to put them to work. In the next lesson, we’ll learn **Basic Math** - how to add, subtract, and manipulate these numbers in our Ledger.