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

:::info[Indentation as Code Section]

Unlike other programming languages that use *curly braces* to mark blocks (sections) of code, in Python we use **indentation**.
This is extremely important to learn as Python will raise **IndentationError** if you do it wrong.

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
Now that you know how to get user input and branch your program using conditional logic (`if`, `elif`, `else`) the code can move away from hardcoded values and become interactive. 

**Goal:** use `input()` to collect user choices, cast strings to numbers, and use conditional logic to apply discounts and stock checks.

1. Open `main.py` file in our `simple-python-shop` project directory.
2. Add a new variable `item_stock` and set it to some integer
3. Interactive input: 
    * Ask the user for desired `item_quantity` using `input()`. **Don't forget** to cast the string to integer !
4. Stock & Availability Check
    * If `item_quantity` is less or equal to `0` print an error message: `Invalid quantity ordered`
    * If `item_quantity` is greater then `item_stock` print `Sorry, we do not have enough stock.`
5. Dynamic discount (conditionals)
    * Calculate the total (you should have this from the last lesson)
    * If `total` is over `100` apply a **10%** discount (`total * 0.90`) and print: `Discount applied: 10%`
    * Otherwise print: `No discount applied`
6. Receipt Output
    * Output the final receipt showing item name, quantity, applied discount state, and final amount due.
7. Commit and push your updated code to Github.

## Deepen Your Knowledge
* Learn more about [Indentation in Python](https://realpython.com/ref/glossary/indentation/) from this **Real Python** article
* Learn [The Importance of Indentation](https://medium.com/@duruprincewilluzochukwu/the-importance-of-indentation-in-python-a-beginners-guide-21cec5292519) from this **Medium** article.

## What's Next
Now that our programs can take user input, calculate things and evaluate what to do on those calculations, we can jump into **loops**. These help us to run a peace of code multiple times without us repeating the code.