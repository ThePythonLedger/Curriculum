---
id: math-strops-and-comparisons
title: Math, String Operations and Comparisons
sidebar_label: Math, String Operations and Comparisons
sidebar_position: 2
lesson: true
---

# Math, String Operations and Comparisons
In the last lesson we have learned how to output data to our screen, how to declare a variable and what different core data types exists in Python. In this lesson we will learn how math works in Python.

## Lesson Overview
At the end of the following lesson you will be confident at:
* Doing math with numbers in Python
* Doing math with strings in Python
* Comparing results to see if they are the same or one is bigger than the other

## Performing Operations on Numbers
Number data types, `int` and `float` are very useful when we must do some math.

### Addition
Adding two numbers together can be done with `+` operator.
```python interactive
a = 5
b = 2

print(a + b)
```

### Subtraction
Subtraction of two numbers is done with `-` operator.
```python interactive
a = 5
b = 2

print(a - b)
```

### Multiplication
Multiplication of two numbers is done with `*` operator.
```python interactive
a = 5
b = 2

print(a * b)
```

### Division
Division of two numbers is done with `/` operator.
```python interactive
a = 5
b = 2

print(a / b)
```

:::info

Division **always** returns `float`

You must be careful when dividing two numbers as the second number must not be equal to 0. If the *divisor* (second number) is 0, Python will raise **ZeroDivisionError**.

:::

### Floor Division
Sometimes we may need to only get *whole number* from division and we dont care about the remainder. In that case we can use something called **floor (integer) division**. 

**Floor division** is done with `//` operator.
```python interactive
a = 5
b = 2

print(a // b)
```

### Modulo Operator
Sometimes we may need to know remainder of *division* but we do not care about the whole number, only the remainder. In that case we use **modulo** operator.

**Modulo** in done with `%` operator.
```python interactive
a = 10
b = 3

print(a % b)
```
> Result of this operation is 1 because 3 goes into 10 three times and whats left is 1.

### Exponentiation
Raises the left value to the power of the right value.

**Exponentiation** is done with `**` operator.
```python interactive
a = 10
b = 2

print(a ** b)
``` 

## Performing Operations on Strings
We can perform various operations on strings in Python. For example, we can:

### Add Strings Together
```python interactive
a = "Hello"
b = " World"

print(a + b)
```

### Multiply Strings
```python interactive
print("-" * 20)
```

### Get a Single Letter
```python interactive
a = "The Python Ledger"

print(a[0]) # First letter at index 0
print(a[1]) # Second letter at index 1
print(a[-1]) # Last letter at index -1
```

:::info[In programming we count from 0]

Python always starts counting at 0. This is called an **index**.

:::

### Convert Case
```python interactive
a = "MixEd CasiNG"

print(a.upper()) # Uppercase
print(a.lower()) # Lowercase
print(a.title()) # Titlecase
```

### Strings Cannot Be Modified in Place
Strings in Python are **immutable**.
This means that they cannot be modified in place and every operation on strings results in a new string.

We demonstrate this in the following example
```python interactive
a = "hello"
a.upper()
print(a) # Expecting "HELLO", but gets "hello"

b = a.upper()
print(b)
```

### String Formatting
Modern Python recommends usage of `f-string` for string formatting. Only difference is that we use letter `f` in front of the string to mark it as `f-string`. 
Then we can use `{ }` syntax to inject variables directly into strings.

```python interactive
course_name = "Python Course"
formatted_string = f"I am starting {course_name}"

print(formatted_string)
```


## Comparisons
We can compare values

In Python we use these comparison operators:
* **Equal to** (`==`)
* **Not equal to** (`!=`)
* **Greater than** (`>`)
* **Less than** (`<`)
* **Greater than or equal to** (`>=`)
* **Less than or equal to** (`<=`)

All of these return a `boolean` value. `True` or `False`
```python interactive
a = 5
b = 3

print(a == b) # False
print(a != b) # True
print(a > b) # True
print(a < b) # False
print(a >= b) # True
print(a <= b) # False
```

## Logical Operators
In Python we have 3 logical operators. These are:
* `and`
* `or`
* `not`

### `and` Logical Operator
`and` operator is used to check if both conditions (on left and right side) are `True`. If so the whole expression is evaluated to `True`.

### `or` Logical Operator
`or` operator is used when we need to check if **any** of the conditions are `True`. If so, whole expression is evaluated to `True`

### `not` Logical Operator
`not` operator is used for inverting logic. If something is `True` it will invert it to `False`

```python interactive
print((5 > 3) and (8 > 4)) # True
print((6 > 7) and (8 > 4)) # False

print((5 > 3) or (8 > 4)) # True
print((6 < 7) or (8 > 4)) # True

print(not True) # False
```

## Assignment
In the last assignment we have declared our shop variables and printed the inventory. In this one you are tasked with:
1. Open your code editor in your last project directory `simple-python-shop`
2. Open `main.py` file we have been working on
3. Standardize your strings:
    * Convert `shop_name` to **uppercase** (e.g., `MERLIN SHOP`)
    * Convert item name to **titlecase** (e.g., `Excalibur`)
4. Calculate the checkout price:
    * Create variable `total` by multiplying `item_price` and `item_quantity`
5. Comparison checks:
    * Create a boolean `is_large_order` that evaluates whether `item_quantity` is greater then or equal to `3`.
6. Update your output to use **f-string** :
    ```
    Welcome to MERLIN SHOP
    --------------------------------
    Item: Excalibur
    Purchased: 3 x 67.20
    Total: $201.60
    Large Order: True
    --------------------------------
    Thank you for your purchase !
    ```
7. Commit your changes with `git` and push to Github

## Deepen Your Knowledge
1. Learn more about [Basic math in Python](https://cs.stanford.edu/people/nick/py/python-math.html#math) from article in **Stanford University**, covering all the topics in this lesson but in a different style and a bit more.
2. Broaden your knowledge about [Strings](https://developers.google.com/edu/python/strings) from this Google article and read [Common String Operations](https://docs.python.org/3/library/string.html) from official Python documentation.
3. Read about [Comparisons](https://docs.python.org/3/library/stdtypes.html#comparisons) and [Boolean Operators - and, or and not](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) in official Python documentation.

## What's Next
Now that we have learned how to do calculations and comparisons, its time for our program to change behavior based on those calculations or comparisons. Lets dive in **conditionals**.