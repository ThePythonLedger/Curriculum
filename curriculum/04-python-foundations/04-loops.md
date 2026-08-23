---
id: loops
title: Loops
sidebar_label: Loops
sidebar_position: 4
lesson: true
isDraft: true
---

# Loops
## Introduction
More often than not, we will have to execute some peace of code in a loop, repeating the action performed. Python offers us two ways to solve our problems without repeating the same logic. This pattern is something you will see in many programming languages. We developers always try to keep our code **DRY** (Don't Repeat Yourself) as much as possible.

## Lesson Overview
In this lesson you will learn
* What is a loop?
* What types of loops there are in Python and why do we use each one?
* What is **iteration**??

## What Is a Loop?
> a structure, series, or process, the end of which is connected to the beginning.
> - definition of **loop** in english language

In Python, we have two loops that behave sligly diffrently, so lets get to know them.

## While Loop
While loops are used when we need to repeat some code block **while some condition is True**. To create **while** loop, we use keyword `while` followed by `condition` then a colon (`:`). We also have to indent the code block which we wish to execute in the loop
```python
while condition:
```

We can demonstrate this in the following example:
```python interactive
a = 0
while a < 5:
    print(f"a is: {a}")
    a = a + 1 # Increase the variable a by 1

print("Loop has finished")
```

:::tip[Always make sure your loop exits]

While loops can be a bit tricky as we must keep track and update our condition every time the loop starts a new **iteration**. If we fail to update the condition our program will never finish its execution and it must be killed by force.

This is a condition called **infinite loop** and it can be quite useful if controlled, but bad if left with no way to exit.

If you ever do find yourself in an **infinite loop** with no way to exit, do not panic. Use keyboard shorcut <kbd>CTRL</kbd>+<kbd>C</kbd> to kill your program.

:::

## For Loop
For loops are used when you know the number of times the code must loop. They are defined with a keyword: **for** followed by **item** which will be state of the loop, followed by keyword `in`, then followed by **sequence** of some kind. As with while loops, we must indent the code block we wish to run in loop.
```python
for item in sequence:
```

## `range()` Function
Python gives us `range()` function that returns a type of *sequence* called **generator**. We will learn about these at later lesson, for now, just know that we mostly use them in *for* loops to execute a loop specific number of times.

You can pass diffrent arguments to the function to get diffrent behaviur. Function takes in 3 arguments, with the 1 being required.

Signature of the function is as follows:
```python
range(start, stop, step)
```
* **start**: from where it starts counting (inclusive) - default is 0
* **stop**: where it stops counting (exclusive) - required
* **step**: which step to take for each count - default is 1

Let's see a little example of using `for` loop and `range` function.
```python interactive
for item in range(5):
    print(item)
```

As you can see, Python by default always starts counting at index 0. Another thing to note is that we do not have number 5 printed, but we did get 5 iterations of the loop.

```python interactive
for item in range(1, 5):
    print(item)
```
In this example you can see that our loop is now starting to print from 1, but still does not print 5. This is because **start** argument is *inclusive* but the **end** argument is *exclusive*. If we want to have 5 printed, we must set **stop** argument as 6.

```python interactive
for item in range(0, 11, 2):
    print(item)
```
Now we have told the function we want every number from 0 to 11 but in **step**s of 2. We can also count in reverse by setting **step** argument to negative integer.

## `break` And `continue`
### `break`
What if you need to break out of the loop early? You have found something you are looking for and the loop needs to finish? Python has a keyword `brake` which does exactly what it's name suggests. Breaks out of the loop.

Let us demonstrate this:
```python interactive
find = 5
for item in range(10):
    if item == find:
        print("Found what we are looking for..")
        break
print("Exited the loop")
```

### `continue`
In some situations it's useful to continue with iteration but skipping this specific one. This is where `continue` keyword comes in.

Let us demonstrate this:
```python interactive
skip = 5
for item in range(10):
    if item == skip:
        continue
    print(item)
```

:::tip[Both `break` and `continue` work only in loops]

These statements `break` and `continue` work only in loops. If you try to use them outside of the loop you will encounter an error.

:::

## Assigment
1. Open `main.py` in your `simple-python-shop` project.
2. Create a new variable named `item_count` and set it to `0` as its initial value.
3. Use a `while` loop to repeatedly prompt the user for an item price.
    * If the price entered is 0 break out of the loop
    * Otherwise, add the price user entered to `total` and increment `item_count` by 1.
4. When the loop finishes, determine if the `total` can have a discount and print out the final receipt.
5. Make sure your program works, then commit and push your code

## Deepen Your Knowlege

## What's Next