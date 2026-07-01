---
id: loops
title: Loops
sidebar_label: 9. Loops
sidebar_position: 10
---
# Python Iteration: Mastering the Loop

Data is only useful if you can do something with it. In this lesson, we cover **iteration**—the process of "looping" through a collection of data to perform an action on every item.

---

## 1. The `for` Loop (Definite Iteration)
In Python, the `for` loop is primarily used to iterate over a sequence (like a list, tuple, dictionary, set, or string). It’s called "definite" because we usually know how many times it will run based on the size of the collection.

**Basic Syntax:**
```python interactive
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I am eating a {fruit}")
```

### Iterating with `range()`
If you need to loop a specific number of times (rather than over a collection), use the `range()` function.
```python interactive
# range(start, stop) - stop is exclusive
for i in range(1, 4):
    print(f"Attempt number {i}")
# Output: Attempt 1, Attempt 2, Attempt 3
```

### Iterating over Dictionaries
Dictionaries require a bit more specific handling since they have keys and values.
```python interactive
user = {"username": "coder99", "status": "active", "level": 5}

# 1. Iterating over keys (default)
for key in user:
    print(key)

# 2. Iterating over values
for value in user.values():
    print(value)

# 3. Iterating over both (The Pythonic Way)
for key, value in user.items():
    print(f"{key}: {value}")
```

---

## 2. The `while` Loop (Indefinite Iteration)
A `while` loop repeats as long as a certain condition is **True**. It is used when you don't know exactly how many times you need to repeat the code beforehand.

**Example:**
```python interactive
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1  # Important: Change the condition or you'll get an infinite loop!

print("Blast off!")
```

---

## 3. Loop Control: `break` and `continue`
Sometimes you need to change the behavior of a loop while it’s running.

* **`break`**: Exits the loop entirely immediately.
* **`continue`**: Skips the rest of the current block and jumps to the next iteration.

**Example:**
```python interactive
numbers = [1, 2, 3, 4, 5, 6]

for n in numbers:
    if n == 3:
        continue  # Skip 3
    if n == 5:
        break     # Stop entirely at 5
    print(n)

# Output: 1, 2, 4
```

---

## Lesson Review Test

1. Which loop is best used when you know the exact collection of items you want to process?
   * A) `while` loop
   * B) `for` loop
2. What happens if the condition in a `while` loop never becomes `False`?
   * A) The program crashes immediately.
   * B) It creates an "infinite loop" that runs until the process is killed.
   * C) Python automatically stops it after 100 rounds.
3. Which method do you use to get both keys and values simultaneously in a dictionary loop?
   * A) `.keys()`
   * B) `.values()`
   * C) `.items()`
4. **True or False:** The `break` statement skips the current item and moves to the next one in the loop.

*(Answers: 1. B, 2. B, 3. C, 4. False (That is what `continue` does; `break` exits the loop entirely))*

---

## Deep Dive: External Resources

<details>
  <summary>📚 Deep Dive</summary>

Ready to learn more? Check out these excellent resources:

* **Python Docs:** [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
* **Real Python:** [Python "while" Loops (Indefinite Iteration)](https://realpython.com/python-while-loop/)
* **W3Schools:** [Python For Loops Reference](https://www.w3schools.com/python/python_for_loops.asp)
* **Programiz:** [Python break and continue](https://www.programiz.com/python-programming/break-continue)

</details>

