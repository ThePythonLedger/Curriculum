---
id: input-and-conditionals
title: User Input and Conditionals
sidebar_label: User Input and Conditionals
sidebar_position: 3
lesson: true
---

# User Input and Conditionals
In the last lesson we learned how to compare values. In this lesson we will expand that knowledge and learn how to influence programs decision to do something depending on conditions. We will also cover how to get input from the user.

## Lesson Overview
In this lesson you will learn:
* How to receive an input from user
* How to make program respond to conditions
* How to use `if-elif-else` to branch your program

## User Input
Our program would not be very useful if it cannot take data from the user. In Python we do this using `input()` function.  `input()` takes any string as a **user prompt** (what will be displayed to the user while waiting for input)

```python interactive
name = input("What is your name?" )

```

:::info[`input()` always returns a string]

`input()` function **always** returnes a *string*. This is something you need to watch for when you ask the user to enter some data. If you need numbers (integer or float) you will need to **type cast** it to some other type.

If you cannot remember how to do this, check out previus [Core Datatypes - Type Casting](./01-output-variable-datatypes.md#type-casting) lesson.

:::

## Conditionals - What Are They?
**Conditionals** is a name for a group of keywords that branch the program logic depending on **condition**.
In Python we have:
* `if`
* `elif`
* `else`

We use these keywords to make our program do something **if** one condition is **True** and something else if its **False**.

We start by using `if` keyword, followed by a **condition** and end it with **colon** (`:`).
Then we **must** indent (4 spaces or 1 tab) the next line.

Let's see a simple example by running the code below. Feel free to change variable `a` to see how the program reacts.
```python interactive
a = 5

if a == 5:
    print("a is 5")
else:
    print("a is not 5")
```
In this basic example, our program will execute its task depending on **conditions**. In the current example, we ask Python to compare value in variable `a` to **int** 5. If they are equal, program executes one branch and if its not, program executes another branch.

:::info

Unlike other programming languages that use *curly braces* to mark blocks of code, in Python we use **indentation**.
This is extremely important to learn as Python will raise **IndentationError** if you do it wrong.

Learn more about [Indentation in Python](https://realpython.com/ref/glossary/indentation/) from this **Real Python** article and [The Importance of Indentation](https://medium.com/@duruprincewilluzochukwu/the-importance-of-indentation-in-python-a-beginners-guide-21cec5292519) from this **Medium** article.

:::

In Python, we also have `elif` keyword which means *else-if*. Its used to check more than one condition. Let's see an example:
```python interactive
a = 5

if a == 5:
    print("a is 5")
elif a < 5:
    print("a is lower then 5")
else:
    print("a is bigger then 5")

```
In this example, we check the value of variable `a`. Then based on conditions set, our program will execute specific branch.

We use this branching logic to make our program do varius things based on these conditions. Each condition we have **always** evaluates to **boolean** - being **True** or **False**. We can also use logical operators (`and`, `or`, `not`) to chain multiple conditions for Python to check.
```python interactive
age = 15
name = "Bob"
is_verified = True

if age > 15 and is_verified:
    print(f"{name} is allowed to enter.)
elif age > 15 and not is_verified:
    print(f"{name} has correct age but not verified)
elif age <= 15:
    print(f"{name} is not 15 years old")
```

## Assigment
We now know enough to build a basic calculator.
1. Ask the user to supply following
2. Based on user *operand* calculate the result and assign it to variable with a name `result`.

### Assignment Area
Use our built in Python interpreter to solve your assignment.
```python interactive
# Write your assignment below

```

:::tip

Use **modulo** operator to determine the remainder of division with 2. If remainder is 0, then the number is **even** otherwise its **odd**

:::

## Deepen Your Knowledge

## What's Next