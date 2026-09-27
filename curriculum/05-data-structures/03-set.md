---
id: set
title: Set
sidebar_label: Set
sidebar_position: 3
lesson: true
isDraft: true
---
# Set
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
```python interactive debug
myset = {1, 2, 2, 2, 3, 3, 4, 5}

for item in myset:
    print(item)
    
print(f"Is 3 in set?: {3 in myset}")
```

## Adding and Removing Elements
We can use `.add()` method to add a single element to set or use `.update()` method to add multiple elements.
```python interactive debug
a = {1, 2, 3}
a.add(4)
print(f"Set after add: {a}")

a.update([5, 6, 7])
print(f"Set after update: {a}")
```

Removing the elements can be done with `.remove()` method which raises `KeyError` if that element does not exist.
```python interactive debug
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
Explore Python sets deeper by visiting this [built-in: set] article from **Real Python** (especially the part about additional methods which come in handy when working with sets).

Remember you do not need to remember all the methods there are. Just read through them, to know they exist.
:::

## Exercise
Complete [[TODO] Exercise 07 — WorkingTitle](#) to practice sets.

## Assignment {#assignment}
In this assigment our task is simple one. We need to track distinct *unsold* items so we can better prepare for the next day in our little shop.

1. Open `main.py` file we have been working on.
2. Define a set for all **sold items** (`item[0]` of element in `order` list) and define a set of **all inventory items** (`item[0]` of element in `inventory` list) - you can use set coprehension to do this in one line or use a for loop to iterate over each item in the lists.
3. Create a variable `unsold_items` and set its value to be `sold_items` substracted from `all_inventory_items`
4. Print out items that did not have a sale today.
5. Confirm the program works, commit and push to Github

## What's Next {#next-lesson}
Now that we covered index based data structures, it's time to meet **dictionary** which is unique in its *key-value* approach and is probably most used data structure (besides *lists*).