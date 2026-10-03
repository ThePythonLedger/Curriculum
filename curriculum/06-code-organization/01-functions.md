---
id: functions
title: Reusable Code with Functions
sidebar_label: Functions
sidebar_position: 1
lesson: true
isDraft: false
---
# Reusable Code with Functions

Throughout this course, you have already been using functions without necessarily realizing it, like **print()** and **len()**. 

Up to this point all of our python scripts have executed straight from top to bottom. If you needed to perform the same calculation three times you had to copy and paste the exact same block three times.

In this lesson, we will learn how to bundle operations into reusable, named blocks of code called **functions**

## Lesson OverView {#overview}

At the end of this lesson you will”

- Define your own custom function using **def** keyword
- Call functions  and pass data into them using parameters and arguments
- Provide fallback options using default parameter values
- Send computed data back to your program using **return**
- Understand the critical distinction between **return** and **print()**
- Understand between built-in and user-defined functions.

## Conceptual Overview

**Functions**: is reusable block of code that perform a specific task which can be called multiple times with different inputs and returns the value

When talking about function think like self-contained machine:

1. **Input**: you feed data into it (arguments)
2. **Process**: it carries out a sequence of instructions.
3. **Output**: it produce a result and hands it back to you (return)

:::tip The DRY Principle
 One thing to know by organizing code into function, your programs follow the DRY principle : Don’t Repeat Yourself
::: 

## Defining and Calling Functions

A function is defined using the **def** keyword followed by descriptive name in **snake_case** , parentheses () and colon : .Everything inside function must be indented

Example:

```python interactive debug

def display_welcome():

 print('welcome to our python function')

```

Above is the  function which when we run should show you  the message **welcome to our python function** but when your run it now nothing will display in terminal this because we have not call it

In order to see the function output we will have to call it here is now full code

```python interactive

def display_welcome():

 print('welcome to our python function')

#Calling the function

display_welcome()

```

At the bottom of our function we have written the function name with parenthesis **display_welcome()** this is how to call the function

:::info
Always use descriptive action verbs for function names such as calculate_total, display_welcome
:::


## Parameters and Arguments

Function become more powerful and useful when they can operate on varying inputs

**Parameter**: the variable listed inside the parentheses in the function definition(act as place holder)

**Argument**: the actual concrete value sent to the function when it called

```python interactive

def greet_customer(name):# name is parameter

 print("hello", name)

greet_customer("Alfred")#Alfred is argument
```

you can pass multiple parameters by separating them by comma

```python interactive

def greet_customer(name,address):
 print ("hello", name,"from", address)

#And calling will be

greet_customer("Bob","dubai")

```

## Default parameter

You can provide fallback value for parameter using the assignment operator (=) in the function definition. This help if caller does not provide argument Python uses the default value

```python interactive

def add_numbers(a,b=2):

 return a + b

print(add_numbers(2,3)) #result 5

print(add_numbers(10)) #result 12

```

:::info

 Parameters with default values must always be placed **after** parameters without default values in your function definition. 
:::


## Returning Values vs Printing

The different between **print()** and **return** is one ot the most critical concepts for beginners to master:

- **print()** simply displays text on your screen for human to read.The rest of your program cannot capture or do any further work with that displayed text
- **return** hands a computed value back to the caller. This allows your program to capture the result in a variable and pass it to other calculations

```python interactive debug

def calculate_subtotal(quantity, unit_price):

  total = quantity * unit_price

  return total

# We capture the returned value in a variable

order_total = calculate_subtotal(3, 15.0)

# Now we can perform further math on it

final_total = order_total + 5.0 # Adding a $5 shipping fee

print("Final amount due:", final_total)

```

:::tip 
If a function finishes without an explicit return statement, Python automatically returns None. 
:::


## Function Types
Broadly speaking, function in Python fall into two categories:
- **Built-in function**: Tools that pre-packaged with python, ready to use anywhere without any extra setup(such as print(), len(), type() and range())
- **User-defined function**: Customer function you write yourself using **def** keyword to solve the specific needs of your program


:::tip 
Apart from these function there other types of function you can study more from here [**types of functions**](https://www.geeksforgeeks.org/python/python-functions) 
:::





## Deepen your Knowledge

:::explore
**Learn More: Official Documentation & Best Practices** Read the following resources to build a deeper mental model of how arguments and documentation work in Python:

1. Read [**Python Tutorial: Defining Functions**](https://docs.python.org/3/tutorial/controlflow.html#23defining-functions) (Sections 4.7, 4.7.1, and 4.7.2). Pay close attention to how Python handles positional arguments versus keyword arguments.
2. Read **Section 4.7.7 (Documentation Strings)** in the official documentation to see how professionals document what a function does. 
:::

## Check Knowledge

Test your understanding with the following questions. Some questions require research using the links above:

1. What happens if you define a parameter without a default value *after* a parameter that has a default value (e.g., def func(a=1, b):)?
2. What value does a function return if it contains no return statement?
3. What is a **Docstring**, where is it placed inside a function, and what syntax is used to define it?
4. What is the difference between passing an argument by position versus passing it by keyword?

## Exercise

Visit our [python-exercises repository](https://github.com/ThePythonLedger/python-exercises) to update your local copy:

1. Fetch and pull the latest changes from upstream/main.
2. Locate the exercise directory exercises/foundations/05_functions.
3. Run pytest to see the test suite.
4. Implement the required functions one by one, removing the @pytest.mark.skip decorator as you pass each level.

## Assignment {#assignment}

Return to your simple-python-shop project from previous lessons. We will refactor our script to use modular functions rather than top-level code.

You will do this assignment on your local machine:

1. Open your simple-python-shop directory in your code editor.
2. Open main.py and refactor your logic into the following dedicated functions:
  - calculate_subtotal(price, quantity): Multiplies the unit price by quantity and **returns** the subtotal as a float.
  - calculate_tax(subtotal, tax_rate=0.07): Calculates the tax amount with a default rate of 7% (0.07) and **returns** the tax amount.
  - format_receipt(shop_name, item_name, quantity, total): Takes shop details and **prints** a multi-line formatted receipt to the console.
3. Call your functions using your shop's item data and print the resulting receipt.
4. Verify your program runs cleanly with python main.py.
5. Stage, commit, and push your changes to your remote GitHub repository.

## What's Next {#next-lesson} 

Now that we can package code into reusable functions, an important question arises: where do the variable defined inside a function live and who can access them?
In the next lesson we will explore **Scope and Namespace(the LEGB rule) to understand how Python looks up variable names and how to prevent unintended side effects in your code  