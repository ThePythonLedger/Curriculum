---
id: dictionary
title: Dictionary
sidebar_label: Dictionary
sidebar_position: 4
lesson: true
isDraft: true
---
# Dictionary
## Introduction {#introduction}
Dictionaries in Python are mutable and unordered collection data structure. **Mutable** meaning it can be modified after creating and **unordered** meaning it does not keep track of it's elements.

Dictionaries are something special, usually called **key-value** data structure because of the way you store data inside them. You will certanly do a lot of work involving dictionaries in your python applications and its a very powerful concept, so let's get started.

## Lesson Overview {#overview}
In this lesson you will learn:
* How to create a dictionary
* How to manipulate elements
* How to iterate over dict

## Dictionary
### Creating Dictionary 
We create a **dictionary** in Python using curly braces `{}`. It consists of two values; **key** and **value**. **Key** is what you use to access the element and **value** is what that element holds.
Let's see an example:
```python interactive
mydict = {"key": "value"}
print(f"Type of variable mydict is: {type(mydict)} and value is: {mydict}")
```
Keys can be any **imutable** type like strings, integers, floats, tuples, etc...
Values can be practicly anything, from simple strings and numbers to complex lists, other dictionaries or any combinations which you want and need.
To separate elements (key-value pairs), use comma `,`.

### Accessing Elements
Accessing an element in a dictionary is done with `[]` syntax but unlike *indexes* we used before, now we use **key** of the element to retrive it.

If the key does not exists, Python will raise **KeyError**. We can get around that by using `.get()` method which is safer to use as it does not raise an error, but returns `None` (by default) if the key does not exists.
```python interactive
mydict = {"key1": "value1", "key2":"value2"}
value1 = mydict["key1"]
print(value1)

# Safer and recommended approach
value2 = mydict.get("key2")
print(value2)
```

### Updating Elements
Updating elements is as simple as assigment of a new value to existing key.
```python interactive
mydict = {"key1": "value1", "key2":"value2"}
print(f"Before: {mydict}")
mydict["key1"] = "other value"
print(f"After: {mydict}")
```

### Adding Elements
Adding new elements to dictionary is done just like *updating* but we use *key* that is **not** already in the dictionary.
```python interactive
mydict = {"key1": "value1"}
print(f"Before: {mydict}")
mydict["key2"] = "other value"
print(f"After: {mydict}")
```

### Removing Elements
To remove and return the value of the element from dictionary you can use `.pop()` method which takes in a single argument; **key**.
```python interactive
mydict = {"key1": "value1", "key2":"value2"}
print(f"Before: {mydict}")
poped_value = mydict.pop("key1")
print(poped_value)
print(f"After: {mydict}")
```

You can also use `del`keyword to remove a key-value pair from the dictionary.
```python interactive
mydict = {"key1": "value1", "key2":"value2"}
print(f"Before: {mydict}")
del mydict["key1"]
print(f"After: {mydict}")
```

For clearing the whole dictionary content you can use `.clear()` method.
```python interactive
mydict = {"key1": "value1", "key2":"value2"}
print(f"Before: {mydict}")
mydict.clear()
print(f"After: {mydict}")
```

### Iterating Over Elements
Its common to iterate over dictionaries to check if it contains some specific values or simply using elements one by one. Dictionaries have two methods that help with this.

Let's go over what happens when you iterate over a dictionary by itself.
```python interactive
mydict = {"key1": "value1", "key2":"value2"}

for elem in mydict:
    print(elem)
```
We would expect to get both keys and values, but you can see, that is not the case. This only returnes keys present in the dictionary. 

You can also use `.keys()` method to get the same result.
```python interactive
mydict = {"key1": "value1", "key2":"value2"}

for elem in mydict.keys():
    print(elem)
```

While it can be useful, we usually want to grab values, or both keys and values. To grab just values contained we can use `.values()` method which does exactly that.
```python interactive
mydict = {"key1": "value1", "key2":"value2"}

for value in mydict.values():
    print(value)
```

To grab both keys and values, we can use `.items()` method. This method returnes 2 values which we can unpack directly to `key` and `value` pairs (these are just variables, so you can name them whatever you want).
```python interactive
mydict = {"key1": "value1", "key2":"value2"}

for key, value in mydict.items():
    print(key, value)
```



## Assignment {#assignment}


## Deepen Your Knowlege {#learn-more}


## What's Next {#next-lesson}