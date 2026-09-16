---
id: tuples
title: Tuple
sidebar_label: Tuple
sidebar_position: 2
lesson: true
isDraft: true
---
# Tuple
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
Unlike lists, as we cannot modify tuples, we don't have a lot of methods available to us, but we will list a few.
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
Deep dive into Python tuples in this [Deep Dive: tuples](https://realpython.com/python-tuple/) article by **Real Python** which takes you deep in topic of tuples and their usecases.
:::

## Exercise
Complete [[TODO] Exercise 06 — WorkingTitle](#) to practice tuples.

## Assignment {#assignment}
Using lists to separatly hold multiple related values is brittle and will break if you do not pay attention to all lists containing data. In this assigment we will deal with those issues by using tuples.

1. Open our `main.py` file we have been working on
2. Create a new empty list called `inventory`. This will hold tuples of related data `(product_name, product_price, product_stock)`.
3. Delete previusly defined `item_name`, `item_price` and `item_stock` variables, we wont need them anymore.
4. Just like before, in **infinite loop**, first check if the input is an *empty string* and if it is, break out of the loop, otherwise get the users input containing *name*, *price* and *stock* in a single line, then split the line using `split()` method to get a list of inputed data.
5. Instead of appending each data to their own list, create a tuple called `item` containing `name`, `price` and `stock` in that particular order and append that to our `inventory` list we declared earlier. Print out each `inventory` element using `for` loop.
6. On to customer ordering items now. Keep `order` list and instead of storing only totals for each item, we will now store `item_name`, `item_quantity` and `line_total` in **tuple** called `line_item` and append that to our `order` list so our shop can better keep track of the orders. **Keep in mind** - tuples are *immutable* which means that you will have to reduce `stock` of the item by replacing entire tuple with new `stock` value.
7. Same as before, calculate the `total` for all the items bought, apply a 10% discount if the `total` is over 100.
8. In the end, print out the inventory, to make sure that the items are actually removed once bought.
9. Make sure your program runs, then commit the changes and push to Github

## What's Next {#next-lesson}
Now that you have seen data structures that can contain duplicates, it's time to meet **set** - a unique data structure that does not allows for duplicates.