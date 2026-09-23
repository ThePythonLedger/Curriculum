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
name = input("What is your name? ")
print("Your name is:", name)
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
    print(f"{name} is allowed to enter.")
elif age > 15 and not is_verified:
    print(f"{name} has correct age but not verified")
elif age <= 15:
    print(f"{name} is not 15 years old")
```

:::tip
In below assigment you are tasked with checking some rules and exiting application if any are broken.

You can use built-in module called `sys` which has some handy functionality to work with our operating system. For now, we are only interested in using its `exit()` functions. It takes in **int** value to provide as **exit code** which other applications can use to interpret whether your program run successfully or failed and in what way.

It is common to use `0` as **success** and any other positive integer to signify a failure.

You can use it like this:
```python
import sys
sys.exit(0) # success
sys.exit(1) # failed / error
```

We will learn more about built-in, custom and third-party **modules** (called libraries) later in the course.
:::

## Assigment
Now that you know how to get user input and branch your program using conditional logic the code can move away from hardcoded values and become interactive. 

1. Open `main.py` file in our `simple-bookstore` project directory.
2. Instead of hardcoding values (`booktore_name`, `book_title`, `book_quantity`, `book_price`) we will ask the user to enter these values using `input()` function. **Remember** that `input()` always returns **str** so we must *cast* the string to desired type (`book_quantity` to **int** and `book_price` to **float**). Replace all of these variables hardcoded values to `input()` function, asking the user to enter the data.
3. Now the system must add some contraints, printing the error message and exiting if any of the rules are broken. Add these below each of the inputs, so that check runs as soon as user enters something. Rules are as follows:
    * `bookstore_name` must be between 3 and 20 characters long
    * `book_name` must be between 3 and 15 characters long
    * `book_quantity` must be positive **integer** (above `0`)
    * `book_price` must be positive **float** (above `0.00`)
4. System must now also calculate taxes that depend on the `book_price`, so make another variable `book_tax` and set it to `0`. Then calculate the tax using below rules, assign it to `book_tax` and print out the tax applied.
    * If `book_price` is above `5` tax is `3%` (`0.03`)
    * If `book_price` is above `10` tax is `5%` (`0.05`)
    * If `book_price` is above `18` tax is `10%` (`0.1`)
5. Display inventory listing like this:
    ```
    Welcome to WILLOW CREEK BOOKS inventory system
    - - - - - - - - - - - - - - - - - - - -
    CURRENT INVENTORY
    - - - - - - - - - - - - - - - - - - - -
    - Book: The Last Cartographer -> [price:$18.5, tax: 10%, copies: 3, available: True]
    - - - - - - - - - - - - - - - - - - - -
    Inventory total: $55.5 [VAT: $60.05]
    - - - - - - - - - - - - - - - - - - - -
    Thank you for using our inventory system.
    ```
6. Commit and push your changes.

## Deepen Your Knowledge
* Learn more about [Indentation in Python](https://realpython.com/ref/glossary/indentation/) from this **Real Python** article
* Learn [The Importance of Indentation](https://medium.com/@duruprincewilluzochukwu/the-importance-of-indentation-in-python-a-beginners-guide-21cec5292519) from this **Medium** article.

## What's Next
Now that our programs can take user input, calculate things and evaluate what to do on those calculations, we can jump into **loops**. These help us to run a peace of code multiple times without us repeating the code.