---
id: core-datatypes
title: Outputting, Storing and Representing Data
sidebar_label: Outputting, Storing and Representing Data
sidebar_position: 1
lesson: true
---
# Outputting, Storing and Representing Data
Welcome to the first real python lesson. Our programs need a way to output information back to users and they also need to store varius data to perform operations on them. We will learn how to do these things in the following lesson.

## Lesson Overview
At the end of the lesson you will:
* Know how to output information to users screen
* Know what is a **variable** and how to store values to them
* Know core python data types:
    * Integer
    * Float
    * String
    * Boolean
* Know how to represent missing values


## Outputting Data Back to User
In Python, we use `print` function to output some data back to user.
```python interactive
print(5)
```
Whatever you pass into the function will be outputted to the screen.

We can also *print* multiple things at once, with python inserting space between each **argument**.
```python interactive
print(2, 5)
```

## Declaring Variables
You can think of **variables** as boxes where your program stores various data. Python does not require any special syntax for declaring variables.

**Variables** are defined by *assignment*.
```python
my_variable = 5
```

Declaring variables has some rules:
* It must start with a letter or underscore
* It can contain lowercase and uppercase letters, underscores, and numbers

Styling guide **PEP8** suggests the use of `snake_case` for variable naming in python.

:::tip

See [PEP8 - Style Guide for Python Code](https://peps.python.org/pep-0008/) to learn more about style of writing python code.

:::

## Python Core Data Types
Python has 4 core data types with addition of `None` which is a special value representing **no value**.

:::note

Python has a special `type()` function which returns what type some data is. We will use this to inspect the following data types.

:::

### Integer
Integers represent **whole numbers**. We use them to represent age of user, score of the game and similar things.

In Python, they are represented as `int`.
```python interactive
my_int = 5

print(type(my_int))
print(my_int)
```

### Float
Floats represent **real numbers**. We use them to represent prices in shop and various other purposes.

In Python, they are represented as `float`
```python interactive
my_float = 1.25

print(type(my_float))
print(my_float)
```

### String
Strings represents **text** data. We use them to represent names, titles, descriptions and various other purposes.

In Python, they are represented as `str` and must be wrapped with single (`'`) or double (`"`) quotes.
```python interactive
string1 = "Double quoted string"
string2 = "Single quoted string"

print(type(string1), type(string2))
print(string1, string2)
```

**Strings** can have special characters called **escape character**. That character is a single **backslash** (`\`). Most common usecase is `\n` which tells Python that the rest of the string goes on the new line.
```python interactive
a = "Hello \n World"

print(a)
```

### Boolean
Boolean values represent **yes** or **no** state. We use them to represent if something is *true* or *false*.

In Python, they are represented as `bool` and only two valid values are `True` or `False`.
```python interactive
bool1 = True
bool2 = False

print(type(bool1), type(bool2))
print(bool1, bool2)
```

### None
This special value `None` represents when there is no value. Its *type* is a special **NoneType**. Its useful when some of the data is missing or arriving at a later time.

```python interactive
none_value = None

print(type(none_value))
print(none_value)
```

### Complex, Bytes, Bytearray
Python has a built-in support for **complex** numbers, as well as for **bytes** representations, but we will deal with those later.

## Type Casting {#type-casting}
Type casting refers to transforming one datatype to another. For example, to transform string `"32"` to integer `32`.
```python interactive
a = "32"
print("Type:", type(a), "Value:", a)
b = int(a)
print("Type:", type(b), "Value:", b)
```

We can also convert to and from other types.
```python interactive
a = 5
b = str(a)
c = float(a)

print("a=", a, "type=", type(a))
print("b=", b, "type=", type(b))
print("c=", c, "type=", type(c))
```

:::note

If Python cannot convert one type to another, it will raise **ValueError**. This usually happens when you try to convert some *text* into *number* or *float*.

Error are very helpful as they tell us exactly **what** is the issue and **where** they happend. If the errors did not exists, your programs would just silently die, and you would have to randomly guess where the issue is.

We will learn how to read and deal with errors in later lessons.

:::

## Assignment {#assignment}
Try the following excercise to establish your knowlege. We will build a shop, starting with defining (declaring) diffrent variables in this lesson and progress with our little shop as we go further along.

You will need to do this assignment on your own machine.

1. Create a new directory with the name `simple-python-shop`
2. Navigate inside the newly created directory
3. Instantiate `git` repository
4. Create a new file with the name `main.py`
5. Inside the file define the the following variables:
    * `shop_name` - set its value to some **string**
    * `item_name` - set its value to some **string**
    * `item_quantity` - set its value to some **integer**
    * `item_price` - set its value to some **float**
    * `item_available` - set its value to some **boolean**
6. Output the variables you defined (using `print()` function) like the following example:
    ```
    Shop name: Merlin Shop
    Item name: Excalibur
    Item quantity: 3
    Item price: $67.2
    Item available: True
    ```
7. Make sure your program works as expected then create a repository and push your code to github

## Deepen Your Knowlege
Go through these articles to deepen your knowlege about the topics covered in this lesson.
1. Read more about `print()` function from [Your Guide to Python print Function](https://realpython.com/python-print/) from this **RealPython** article.
2. Learn more about [Basic Datatypes in Python](https://realpython.com/python-data-types/) from this **RealPython** article.

## What's Next
Now that you have basic knowlege of Python's core data types, we will see how we can use them to make useful output. In the next lesson, we learn about basic **math** and **comparisons**.