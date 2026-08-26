---
id: lists
title: Lists
sidebar_label: Lists
sidebar_position: 1
lesson: true
isDraft: true
---
# Lists
## Introduction {#introduction}
Up until now we have stored a single value in a variable, but what if we need to hold multiple values in some variable? Do we create multiple variables? Of course not, Python has a *built-in* mechanisms for dealing with collections of data which we call **data structures**. In this lesson we first take a look at **list**.

Lists in Python are *built-in* data structure for storing ordered collections of items. They are **ordered** meaning they keep the order in which data came in. They are also **mutable** which means we can change them in place without creating a new copy. They can hold any other type of data including other lists or other data structures. Lists are probably the most used data structure in Python.

## Lesson Overview {#overview}
In this lesson we will cover:
* What lists are?
* How to create a list?
* How to insert, modify or delete elements
* How to access elements
* Iterating over the lists using `for` loops

## Creating lists
Lists in Python are created using **square brackets** (`[]`). They can be creates empty or already with some items provided (elements are separated by **comma** (`,`))

### Empty List
```python interactive
mylist = []
print(f"Type of 'mylist' variable is: {type(mylist)}")
print(f"Value of 'mylist' is: {mylist}")
```
### Pre-populated List
```python interactive
mylist = [1, 2, 3, 4]
print(f"Type of 'mylist' variable is: {type(mylist)}")
print(f"Value of 'mylist' is: {mylist}")
```

:::tip[Check the number of items (elements) in the list]

You can use `len()` function to check the length of the list (and other types that support iteration).

```python interactive
mylist = [1, 2, 3, 4]
list_length = len(mylist)
print(f"List has {list_length} elements")
```
This function always returns **integer**.

:::

## Manipulating Elements in List
### Accessing Elements
To access the element withing a list we must use use its **index**. In Python we start counting from zero (0) so first element in the list is at index 0. Let's see this is example:
```python interactive
mylist = [1, 2, 3]
first_elem = mylist[0]
last_elem = mylist[-1]

print(f"First element of the list is {first_elem} and last is {last_elem}")
```

### Adding Elements
There are multiple ways to insert elements to the list, depending on where you want to place it. 

#### Method: `.append`
First example uses `.append()` method which takes a **single** argument and it is the recommended way of inserting elements. It adds them at the **last position**, expanding the list by one element, and does not need to recompute positiona of other elements, making it fast and reliable. Let's see an example:
```python interactive
a = [] # Empty list
print(f"List before appending: {a}")
a.append(2)
print(f"List after appending: {a}")
a.append(5)
print(f"List after another append: {a}")
```

#### Method: `.insert`
If you need to add elements at specific index, for that we use `.insert()` method which takes **two** arguments; *index* and *value*. This will insert *value* to supplied *index* shifting other elements to the right. Let's see this in the following example:
```python interactive
a = [1, 2, 3, 4]
print(f"List before insert: {a}")
a.insert(2, 5) # Insert value 5 to index 2
print(f"List after insert: {a}")
```

### Removing Elements
Removing of elements can also be done in a couple of ways.

In the first example we will use `.pop()` method that takes **one optional** argument; *index*. This method removes **and** returnes the element from the list. By default, it *pops* the last element but can be set with optional argument.
```python interactive
a = [1, 2, 3, 4]
print(f"List before pop: {a}")
b = a.pop()
print(f"List after pop: {a}, {b=}")

# Pop some other element
c = a.pop(0) # Pop first element
print(f"List after another pop: {a}, {c=}")
```

Another way to remove an element is to use `.remove()` method, but unlike `.pop()` it requires **one** argument; *element*. This method is useful when you want to remove the specific element but do not know its index position and you dont care about the element afterwards.
```python interactive
a = [1, 2, 3, 4]
print(f"List before remove: {a}")
a.remove(3)
print(f"List after remove: {a}")
```
### Iterating With Lists
Lists can be used with `for` loops to iterate on each element of the list, so you can proccess one at a time. Let's see how this works in the following example:
```python interactive
a = [1, 2, 3, 4]

for item in a:
    print(item)
```
This is very useful as we often need to work with specific elements from the list.

:::explore[Learn more about Python lists]

Learn more about Python lists from these resources:
* [Google for Education - Python Lists](https://developers.google.com/edu/python/lists)
* [Official Python Documentation on Lists](https://docs.python.org/3/library/stdtypes.html#typesseq-list)
* [Official Python Documentation on Data Structures - more on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

:::

## Exercise
**Todo**

## Assignment {#assignment}
**Todo**

## What's Next {#next-lesson}
**Todo**