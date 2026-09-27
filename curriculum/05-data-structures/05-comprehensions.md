---
id: comprehensions
title: Comprehensions
sidebar_label: Comprehensions
sidebar_position: 5
lesson: true
isDraft: true
---
# Comprehensions
Comprehensions in Python provide a short and clear way to create new sequences from existing iterable. Basically they are a *fancy* syntax for simple **for-loop** pattern.

## Lesson Overview {#overview}
At the end of the lesson you will know:
* What are comprehensions in Python
* How to write `list`, `dict` or `set` comprehension
* How to use conditions in comprehensions

The key to understanding list comprehensions is that they’re just `for-loops` over a collection expressed in a more terse and compact syntax.

We will start with **list comprehension** as it is most common.

## List Comprehension
Syntax for this looks like:
```python
[item for item in iterable]
```

Let's imagine we have a task of creating a list of **square** numbers from some other list of numbers. For example, let's assume we have a following list of numbers:
```python
nmb_list = [1, 2, 3, 4, 5, 6, 7, 8]
```
To create a new list with **square** of all numbers in a list, we need to first get each element in the list and apply a mathematical operation on it. So it would look something like this:
```python interactive
nmb_list = [1, 2, 3, 4, 5, 6, 7, 8]
squared = []
for nmb in nmb_list:
    squared.append(nmb**2)

print(squared)
```
And the result is correct, but in Python, we can do better. Let's convert our `for-loop` to **list comprehension**.
```python interactive debug
nmb_list = [1, 2, 3, 4, 5, 6, 7, 8]
squared = [nmb**2 for nmb in nmb_list]
print(squared)
```
Result is completely the same, but our code is simpler and more concise. In this simple example we may not see the benefit, but let's add a check there, to only collect **even** numbers.

If we use **for-loop** we may do something like this.
```python interactive
nmb_list = [1, 2, 3, 4, 5, 6, 7, 8]
squared_even = []
for nmb in nmb_list:
    if nmb % 2 == 0:
        squared_even.append(nmb ** 2)

print(squared_even)
```
If we use **list comprehension** it would look like this:
```python interactive debug
nmb_list = [1, 2, 3, 4, 5, 6, 7, 8]
squared_even = [nmb ** 2 for nmb in nmb_list if nmb % 2 == 0]
print(squared_even)
```
The result is again, completely the same, but the syntax is shorter and more concise.

Let's look at the final type of list comprehension, which will produce one value if the condition is `True` or something else if the condition is `False`. For example, let's say we need to produce a list, containing `True` if the number is even or `False` if its odd.

In classic python **for-loop** style, we would do something like this:
```python interactive
nmb_list = [1, 2, 3, 4, 5, 6, 7, 8]
even_mask = []
for nmb in nmb_list:
    if nmb % 2 == 0:
        even_mask.append(True)
    else:
        even_mask.append(False)
print(even_mask)
```

But Python let's us use its super power here also:
```python interactive debug
nmb_list = [1, 2, 3, 4, 5, 6, 7, 8]
even_mask = [True for nmb in nmb_list if nmb % 2 == 0 else False]
print(even_mask)
```

:::tip[Superpowers work with any comprehension]
`if condition` and `if condition else` works will all comprehensions and not just with lists, and they work in the same manner.
:::

You do not need to worry about understanding **comprehensions** right away, but they become extremely useful the more you write your code.

Now that we learned what are list comprehensions, let's look at **dictionary comprehensions** which are very similar in syntax but allows us to create dictionaries similarly.

## Dictionary Comprehension
When creating a new dictionary using dictionary comprehension, you can perform various operations using expressions to determine the data (key and/or value) that will be stored in the new dictionary.

Syntax for this looks like:
```python
{key: value for (key,value) in iterable}
```

To demonstrate this, let's imagine that you are building a currency converter. You would maybe have a dictionary representing prices in USD and need to convert them to EUR. In traditional **for-loop** you would do something like this:
```python interactive
EUR_CONV_RATE = 0.92
prices_in_usd = {'pen': 4, 'book': 15, 'keyboard': 60}
prices_in_eur = {}
for name, price in prices_in_usd.items():
    prices_in_eur[name] = round(price * EUR_CONV_RATE, 2)
print(prices_in_eur)
```
To use **dict comprehension** we would rewrite the above code to:
```python interactive debug
EUR_CONV_RATE = 0.92
prices_in_usd = {'pen': 4, 'book': 15, 'keyboard': 60}

prices_in_eur = {key: round(value * EUR_CONV_RATE, 2) for (key, value) in prices_in_usd.items()}

print(prices_in_eur)
```
:::tip
`round()` function rounds the numbers decimal point to specified number of places. It takes in `float` and a number of decimal places - an `integer`.
```python interactive
a = 43.24214213213
b = round(a, 2)
print(b)
```
:::

:::info
In the above code we use `EUR_CONV_RATE` to declare **constant**. Constants are just variables, but are not supposed to be changed during running of your program. They are useful for declaring things that would not change during runtime of your program, and it's a convention in Python to write them in `ALL_CAPS`. Unlike some other languages, in Python, these are considered just like regular variables and Python will not stop you from changing them during runtime, so you need to consider this when writing your application.

The golden rule is: 
* If the variable will change during your application runtime, its just a variable and should be written as `variable_name`.
* If the variable will **not** change during your application runtime, then you can consider it a **constant** and write them as `VARIABLE_NAME`.

Remember that this is just a convention and it is not a rule you *must* follow.
:::

Now that we covered dictionary comprehensions, we can finally meet **set comprehensions**.

## Set Comprehension
Set comprehension works best when you want a clean transformation, and you also want duplicates to disappear without extra effort. The syntax for **set comprehension** is:
```python
{expression for item in iterable}
```

For example, let's use our *squared* example from before:
```python interactive
nmb_list = [1, 2, 3, 4, 5, 6, 7, 8]
squared = {nmb ** 2 for nmb in nmb_list}
print(squared)
```
We can also use conditionals to get only specific values:
```python interactive debug
nmb_list = [1, 2, 3, 4, 5, 6, 7, 8]
squared_even = {nmb ** 2 for nmb in nmb_list if nmb % 2 == 0}
print(squared_even)
```

:::warning
Comprehensions are very useful and can make your code smaller and easier to understand and reason about. But it also can make your code very difficult to read and understand.

Use them with caution and remember:
* USE comprehensions while the code is readable
* DO NOT use comprehensions when the code starts to become unreadable and go back to **for-loop** for clarity.
:::

## Exercise

## Assignment {#assignment}

## What's Next {#next-lesson}
Comprehensions are very useful in everyday life as a Python programmer, but there is one thing that is universal across all languages, so let's start a new chapter; *code organization*. First thing to learn are **functions** which enable us to write modular code.
