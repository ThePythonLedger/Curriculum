---
id: complex-data-types
title: Complex data types
sidebar_label: 8. Complex data types
sidebar_position: 9
---
# Python Data Structures: Beyond the Basics

Welcome to your next step in Python! While primitive data types (like integers, floats, and strings) hold a single value, Python has built-in complex data types that allow you to store, organize, and manipulate collections of data efficiently. 

Let's explore the four main complex data types: Lists, Tuples, Dictionaries, and Sets.

---

## 1. Lists
A list is an ordered, mutable (changeable) collection of items. Lists can contain items of different data types and allow duplicate values. They are the most common and versatile data structure in Python.

**Key Characteristics:**
* **Ordered:** Maintains the exact order in which you add items.
* **Mutable:** You can add, remove, or change items after creation.
* **Syntax:** Created using square brackets `[]`.

**Example:**
```python interactive
# Creating a list of fruits
fruits = ["apple", "banana", "cherry"]

# Modifying an element (lists are 0-indexed)
fruits[0] = "blueberry"

# Adding a new element to the end
fruits.append("orange")

print(fruits) 
# Output: ['blueberry', 'banana', 'cherry', 'orange']
```

---

## 2. Tuples
A tuple is very similar to a list, but it is **immutable**. Once a tuple is created, you cannot change, add, or remove items. They are perfect for data that should never change (like fixed coordinates or configurations).

**Key Characteristics:**
* **Ordered:** Maintains insertion order.
* **Immutable:** Unchangeable after creation.
* **Syntax:** Created using parentheses `()`.

**Example:**
```python interactive
# Creating a tuple of coordinates
coordinates = (10.5, 20.0, 5.5)

# Accessing an element
print(coordinates[0])  # Output: 10.5

# coordinates[0] = 15.0  <-- This would cause an error!
```

---

## 3. Dictionaries (Dicts)
A dictionary is a collection of key-value pairs. Instead of using numbers to access elements (like finding the 1st item in a list), you use unique keys (like looking up a word in a real dictionary to find its definition).

**Key Characteristics:**
* **Key-Value Pairs:** Stores data as `key: value`.
* **Mutable:** You can add, remove, or change pairs.
* **Syntax:** Created using curly braces `{}` with colons separating keys and values.

**Example:**
```python interactive
# Creating a dictionary for a student
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}

# Accessing a value using its key
print(student["name"])  # Output: Alice

# Adding a new key-value pair
student["graduation_year"] = 2026
```

---

## 4. Sets
A set is an unordered collection of unique items. Sets are highly efficient for checking if an item exists and for ensuring there are absolutely no duplicate values in your data.

**Key Characteristics:**
* **Unordered:** No guaranteed order and no indexing (you can't ask for the "first" item).
* **Unique:** No duplicate values allowed.
* **Syntax:** Created using curly braces `{}` or the `set()` function.

**Example:**
```python interactive
# Creating a set of numbers with duplicates
unique_numbers = {1, 2, 2, 3, 4, 4, 5}

# Duplicates are automatically removed
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Checking if a value exists in the set (very fast)
print(3 in unique_numbers)  # Output: True
```

---

## Lesson Review Test

Test your understanding of the concepts covered above!

1. Which data type is **immutable** (cannot be changed after creation)?
   * A) List
   * B) Tuple
   * C) Dictionary
   * D) Set
2. Which data type uses `key: value` pairs?
   * A) List
   * B) Tuple
   * C) Dictionary
   * D) Set
3. What will be the output of the following code?
   ```python
   my_set = {10, 10, 20, 30}
   print(len(my_set))
   ```
   * A) 2
   * B) 3
   * C) 4
   * D) Error
4. **True or False:** A list is created using square brackets `[]`.

*(Answers: 1. B, 2. C, 3. B (duplicates are removed, so the set is {10, 20, 30} which has 3 items), 4. True)*

---

<details>
  <summary>📚 Deep Dive</summary>

Ready to learn more? Check out these excellent resources:

* **Python Official Documentation:** [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
* **Real Python:** [Lists and Tuples](https://realpython.com/python-lists-tuples/)
* **Real Python:** [Dictionaries](https://realpython.com/python-dicts/)
* **W3Schools:** [Python Sets](https://www.w3schools.com/python/python_sets.asp)

</details>


