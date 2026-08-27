---
id: tuples
title: Tuple
sidebar_label: Tuple
sidebar_position: 2
lesson: true
isDraft: true
---
# Tuple
## Introduction {#introduction}
Tuple is an ordered and immutable collection data structure. **Ordered** meaning it keeps the order of elements in which they are inserted, and **immutable** means that once the tuple is created it cannot change, and you cannot add or remove elements from it.

## Lesson Overview {#overview}
In this lesson we will cover:
* How to create tuple
* Accessing the elements in tuple
* Useful methods on tuples

## Creating Tuple
A tuple is created by enclosing items in parentheses `()`  separated by comma.
```python interactive
a = (1, 2, 3)
print(f"Variable a contains type: {type(a)} and the value of variable is: {a}")
```
Tuples containing a single element still must contain a comma, otherwise python will read the wrong data type:
```python interactive
a = (1)
b = (1,)

print(f"Type of variable a is: {type(a)}")
print(f"Type of variable b is: {type(b)}")
```

## Accessing Elements
Accessing elements of the tuple is done with index, just like lists.
```python interactive
a = (1, 2, 3)
print(f"First element: {a[0]} - Last element: {a[-1]}")
```

## Useful methods
Unlike functions, as we cannot modify tuples, we don't have a lot of methods available to us, but we will list a few.
* `count()` - returns the number of times a specified value appears in tuple.
    ```python interactive
    numbers = (1, 2, 3, 3, 3, 4, 5)
    print(numbers.count(3))
    ```
* `index()` - returns index of the **first occurrence** of the element.
    ```python interactive
    fruits = ("apple", "banana", "cherry")
    print(fruits.index("banana"))
    ```

:::explore[Learn more about Python Tuples]
* [Python built-in types: tuples from RealPython](https://realpython.com/ref/builtin-types/tuple/)
* [Tuples and Sequences from official Python documentation](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
:::

## Assignment {#assignment}
**Todo**

## What's Next {#next-lesson}
**Todo**