---
id: set
title: Set
sidebar_label: Set
sidebar_position: 3
lesson: true
isDraft: true
---
# Set
## Introduction {#introduction}
A **set** in Python is unordered collection of unique elements. **Unordered** means it does not keep the order of the elements and **unique** means it does not allow duplicates.

Its mostly used when removing duplicates from list or performing quick membership tests (checking to see if some element belongs to both sets).

## Lesson Overview {#overview}
In this lesson we will cover:
* How to create set
* How to access elements of the set
* Adding or removing elements
* Set operations

## Creating Set
Creating sets in Python is done with curly braces `{}` or its constructor `set()`.
```python interactive
# Using curly braces
myset = {1, 2, 2, 2, 3, 3, 4, 5}
print(f"Type of variable myset is: {type(myset)} and the value is: {myset}")

# Using set() function
other_set = set([1, 1, 2, 2, 3, 4, 5,5])
print(f"Type of variable other_set is: {type(other_set)} and the value is: {other_set}")
```
To create an empty set, we need to use `set()` function as using `{}` will create a new dictionary (which we will cover in the next lesson).

## Accessing Elements
We cannot access elements of the set like we did with other data structures using index, but we can iterate over it with `for` loop or check if the item exists with `in` keyword :
```python interactive
myset = {1, 2, 2, 2, 3, 3, 4, 5}

for item in myset:
    print(item)
    
print(f"Is 3 in set?: {3 in myset}")
```

## Adding and Removing Elements
We can use `.add()` method to add a single element to set or use `.update()` method to add multiple elements.
```python interactive
a = {1, 2, 3}
a.add(4)
print(f"Set after add: {a}")

a.update([5, 6, 7])
print(f"Set after update: {a}")
```

Removing the elements can be done with `.remove()` method which raises `KeyError` if that element does not exist.
```python interactive
a = {1, 2, 3}
a.remove(2)
print(f"Set after remove: {a}")
```

## Set Operations
Sets support mathematical operations like union, intersection, and difference, making them useful for comparing collections.
```python interactive
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
```

:::explore[Learn more about Python Sets]
Learn more about sets in these materials:
* [Python built-in data types from RealPython](https://realpython.com/ref/builtin-types/set/)
* [Python data structures: set from official Python documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)
:::

## Assignment {#assignment}
**Todo**

## What's Next {#next-lesson}
**Todo**