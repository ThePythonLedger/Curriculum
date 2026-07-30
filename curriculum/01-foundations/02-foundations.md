---
id: foundations
title: Foundations
sidebar_label: 2. Foundations
sidebar_position: 2
lesson: true
---
# Introduction
In this introductory lesson we will start with writing some Python code. 

# Lesson Overview
What you will learn in the following lesson:
* Outputting data back to user
* Declaring variables
* Python core data types (*integer*, *float*, *string*, *boolean*, *None*)
* Performing operation on numbers
* Performing operations on strings
* Using logical and mathematical operators

# How to Run Python Code?
In this beginner course we will use our python interpreter right here on the website.

> There is no need for any installation step at this stage. Later we will use *local development environment* and learn how to download and use python on your own machine.

# Outputting Data Back to User
In Python, we use `print` function to output some text back to user.
```python interactive
print("Welcome to The Python Ledger")
```
Whatever you pass into the function will be outputted to the screen.

Additional resources:
* [Your Guide to Python print Function - Real Python](https://realpython.com/python-print/)
* [Print and Standard Out - Stanford CS](https://cs.stanford.edu/people/nick/py/python-print.html)
* [Python print() function - Mimo](https://mimo.org/glossary/python/print-function)

# Code Comments
Code comments are ignored by programming language and are useful to us, programmers. We use them to explain the logic in the code.

In Python, code comments start with `#` sign. Everything after that sign is considered a comment and python will not execute it.
```python
# This is a comment
```

# Declaring Variables
You can think of **variables** as boxes where your program stores various data. Python does not require any special syntax for declaring variables.

**Variables** are defined by *assignment*.
```python
my_variable = 5
```

Declaring variables has some rules:
* It must start with a letter or underscore
* It can contain lowercase and uppercase letters, underscores, and numbers

Styling guide **PEP8** suggests the use of `snake_case` for variable naming in python.
[Style Guide for Python Code](https://peps.python.org/pep-0008/)

# Python Core Data Types
Python has 4 core data types with addition of `None` which is a special value representing **no value**.

> Python has a special `type()` function which returns what type some data is. We will use this to inspect the following data types.

## Integer
Integers represent **whole numbers**. We use them to represent age of user, score of the game and similar things.

In Python, they are represented as `int`.
```python interactive
my_integer = 5

print(type(my_integer))
print(my_integer)
```

## Float
Floats represent **real numbers**. We use them to represent prices in shop and various other purposes.

In Python, they are represented as `float`
```python interactive
my_float = 1.25

print(type(my_float))
print(my_float)
```

## String
Strings represents **text** data. We use them to represent names, titles, descriptions and various other purposes.

In Python, they are represented as `str` and must be wrapped with single (`'`) or double (`"`) quotes.
```python interactive
string1 = "Double quoted string"
string2 = "Single quoted string"

print(type(string1), type(string2))
print(string1, string2)
```

## Boolean
Boolean values represent **yes** or **no** state. We use them to represent if something is *true* or *false*.

In Python, they are represented as `bool` and only two valid values are `True` or `False`.
```python interactive
bool1 = True
bool2 = False

print(type(bool1), type(bool2))
print(bool1, bool2)
```

## None
This special value `None` represents when there is no value. Its useful when some of the data is missing or arriving at a later time.

```python interactive
none_value = None

print(type(none_value))
print(none_value)
```

## Complex, Bytes, Bytearray
Python has a built-in support for **complex** numbers, as well as for **bytes** representations, but we will deal with those later.

## Learn More About Datatypes
* [Basic Datatypes in Python - Real Python](https://realpython.com/python-data-types/)
* [Built-In Types - Python official documentation](https://docs.python.org/3/library/stdtypes.html)
# Type Casting
Type casting refers to transforming one datatype to another. For example, to transform string `"32"` to integer `32`.
```python interactive
a = "32"
print("Type:", type(a), "Value:", a)
b = int(a)
print("Type:", type(b), "Value:", b)
```
> If you try to convert letters to **int** or **float** Python will raise a **ValueError**. We will learn how to deal with errors in later lessons.

We can also convert to and from other types.
```python interactive
a = 5
print(a)
print(str(a))
print(float(a))
```

# Performing Operations on Numbers
Number data types, `int` and `float` are very useful when we must do some math.
## Addition
Adding two numbers together can be done with `+` operator.
```python interactive
a = 5
b = 2

print(a + b)
```

## Subtraction
Subtraction of two numbers is done with `-` operator.
```python interactive
a = 5
b = 2

print(a - b)
```

## Multiplication
Multiplication of two numbers is done with `*` operator.
```python interactive
a = 5
b = 2

print(a * b)
```

## Division
Division of two numbers is done with `/` operator.
```python interactive
a = 5
b = 2

print(a / b)
```
> Division **always** returns `float`

> You must be careful when dividing two numbers as the second number must not be equal to 0. If the *divisor* (second number) is 0, Python will raise **ZeroDivisionError**.

## Floor Division
Sometimes we may need to only get *whole number* from division and we dont care about the remainder. In that case we can use something called **floor (integer) division**. 

**Floor division** is done with `//` operator.
```python interactive
a = 5
b = 2

print(a // b)
```

## Modulo Operator
Sometimes we may need to know remainder of *division* but we do not care about the whole number, only the remainder. In that case we use **modulo** operator.

**Modulo** in done with `%` operator.
```python interactive
a = 10
b = 3

print(a % b)
```
> Result of this operation is 1 because 3 goes into 10 three times and whats left is 1.

## Exponentiation
Raises the left value to the power of the right value.

**Exponentiation** is done with `**` operator.
```python interactive
a = 10
b = 2

print(a ** b)
``` 

# Performing Operations on Strings
We can perform various operations on strings in Python. For example, we can:

## Add Strings Together
```python interactive
a = "Hello"
b = " World"

print(a + b)
```

## Multiply Strings
```python interactive
print("-" * 20)
```
## Get a Single Letter
```python interactive
a = "The Python Ledger"

print(a[0]) # First letter at index 0
print(a[1]) # Second letter at index 1
print(a[-1]) # Last letter at index -1
```
> Python always starts counting at 0. This is called an **index**.

## Convert Case
```python interactive
a = "MixEd CasiNG"

print(a.upper()) # Uppercase
print(a.lower()) # Lowercase
print(a.title()) # Titlecase
```

## Strings Cannot Be Modified in Place
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

## String Formatting
Modern Python recommends usage of `f-string` for string formatting. Only difference is that we use letter `f` in front of the string to mark it as `f-string`. 
Then we can use `{ }` syntax to inject variables directly into strings.

```python interactive
course_name = "Python Course"
formatted_string = f"I am starting {course_name}"

print(formatted_string)
```


# Comparisons
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
# Logical Operators
In Python we have 3 logical operators. These are:
* `and`
* `or`
* `not`

## `and` Logical Operator
`and` operator is used to check if both conditions (on left and right side) are `True`. If so the whole expression is evaluated to `True`.

## `or` Logical Operator
`or` operator is used when we need to check if **any** of the conditions are `True`. If so, whole expression is evaluated to `True`

## `not` Logical Operator
`not` operator is used for inverting logic. If something is `True` it will invert it to `False`

```python interactive
print((5 > 3) and (8 > 4)) # True
print((6 > 7) and (8 > 4)) # False

print((5 > 3) or (8 > 4)) # True
print((6 < 7) or (8 > 4)) # True

print(not True) # False
```

# Quiz Time
> Some of the questions will require you to read from external resource linked in this lesson and you are higly encouraged to do so.

Before attempting to solve the challenge below, try to answer these questions:
* What are **core** datatypes in Python?
* How do we represent **real numbers**?
* How do you split the string into multiple lines (using **string delimiters**)
* `print()` function always prints a newline character at the end of its output. How do we tell it not to do that?
* From what index Python starts counting?

# Mini-Project: The Café Receipt & Loyalty Calculator

## Project Goal
Write a Python script that calculates the total cost of a customer's order at a coffee shop, applies formatting, and checks if they qualify for a VIP loyalty reward using logical operators.

## Instructions
1. Use proper `snake_case` variable names.  
2. Track item details using **strings**, **integers**, and **floats**.
3. Perform calculations using *arithmetic operators*.  
4. Format the final output using **f-strings** and **string repetition**.  
5. Evaluate customer discount eligibility using **logical operators**.

## Task
### Define the Following Variables
* Name of the store selling the item - *string*
* Name of the item - *string*
* Price of the item - *float*
* Quantity of item - *float*

### Calculate Subtotal, Tax Amount and Total Price
* Calculate **subtotal** by multiplying item **price** with item **quantity**
* Calculate **tax amount** by multiplying **subtotal** with **tax rate** (0.08)
* Calculate **total price** by adding **subtotal** to **tax amount**

### Set Customer Status and Happy Hour Check
* Customer **is** a *VIP member* (create a variable that represents this and set it to `True`)
* Currently it's not happy hour (create a variable that represents this and set it to `False`)

### Check for and Apply Discount
* If the customer is VIP **and** quantity is 3 or more items **or** is *happy hour*, give 10% discount 
* There should be only one check that utilizes `or` and `and` logical operators

Define a variable containing a separator line using **string multiplication**

Finally print out the receipt on the screen showing:
```
Separator line
Store name
Separator line
Item: quantity x item name
Subtotal
Tax amount
Total price
Separator line
Has discount been included?
Separator line
```
## Your Solution

```python interactive
# Use this to solve your first mini project


```
