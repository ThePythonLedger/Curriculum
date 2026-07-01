---
id: programming-languages
title: What is a programming language?
sidebar_label: 3. What is a programming language?
sidebar_position: 3
---

# What is a programming language?

Think of a **programming language** as a bridge between humans and computers. Computers don't understand English or Spanish; they only understand electricity (on or off). A programming language allows us to write instructions in a way that humans can read, which then get translated into something the computer can execute.

At its heart, programming is about two things: **Data** (the information) and **Algorithms** (the instructions).

## Data Structures: Organizing Information
Before a computer can process information, it needs to organize it. This is called a **Data Structure**. 

Imagine you are organizing a kitchen. You put eggs in a carton, flour in a jar, and milk in a jug. Each container is "structured" to hold that specific type of item efficiently.
* **Simple Example:** A "Floating Point" number is just a fancy name for a decimal (like `1.45`). 
* **Built-in Types:** Most languages, including Python, have these "containers" ready for you to use (like integers, text, or lists).
* **Custom Structures:** As you get more advanced, you can build your own "containers" to fit the specific needs of your app.

## Algorithm: The Step-by-Step Recipe
An **algorithm** is simply a list of steps to finish a task. If you have ever followed a recipe to bake a cake, you have executed an algorithm!

In programming, an algorithm must be:
1. **Finite:** It has a clear beginning and end.
2. **Well-defined:** Each step is precise so the computer doesn't get confused.

## Language Elements
Every language has a set of rules that determine if your code will actually run.

### 1. Syntax (The Grammar)
Just like English has rules (sentences start with a capital letter and end with a period), programming has **Syntax**. If you forget a colon or a parenthesis in Python, the computer will give you a "Syntax Error" because it doesn't recognize the "sentence" you wrote.

### 2. Semantics (The Meaning)
Syntax is about the *form*, but Semantics is about the *meaning*. 
* **Static Semantics:** These are rules checked before the program runs (like making sure you aren't trying to "multiply" a word by a color).
* **Dynamic Semantics:** This is what actually happens while the program is running. It’s the "behavior" of your code.

### 3. Type System
The **Type System** categorizes data so the computer knows what it can do with it. For example, you can add two numbers together ($2 + 2 = 4$), but you can't necessarily "add" a number to a list of names.

* **Static vs. Dynamic:** Python uses **Dynamic Typing**. This means you don't have to tell the computer "this is a number" beforehand; it figures it out while the program is running.
* **Strong vs. Weak:** Python is **Strongly Typed**. It won't let you do "weird" things—like adding the number `5` to the word `"Apple"`—without you explicitly converting them first.

---

## Programming Paradigms (Styles of Coding)
A "paradigm" is just a style or approach to writing code. Two of the most common are:

* **Imperative:** You give the computer a list of direct commands. "Go to the fridge, get the milk, pour it in a glass."
    * **Procedural:** Organizing those commands into "blocks" or functions.
    * **Object-Oriented (OOP):** Organizing code by grouping data and actions together (like creating a "Car" object that has data like "Color" and actions like "Drive").
* **Declarative:** You describe *what* you want, but not exactly *how* to do it (like a GPS—you give it the address, and it figures out the turns).

### Which one is Python?
Python is a "Multi-paradigm" language. This is why it is so popular for beginners! You can write simple lists of instructions (Imperative), or you can build complex systems using Objects (OOP).

## Next steps
Now that we are familiar with *programming languages* in general, its time to move on to our target. [The **Python** programming language](/lessons/foundations/why-python).