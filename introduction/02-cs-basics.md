---
id: cs-basics
title: What is a computer and how programs are executed?
sidebar_label: 2. What is a computer?
sidebar_position: 2
---

## Introduction: The Digital Workshop

Imagine you are sitting at a physical workbench, ready to build a wooden birdhouse. You have a blueprint telling you what to do, a pile of raw lumber, and a pencil to label your pieces. 

Before you drive your first nail, you instinctively understand how your workshop functions: you know you have to lay your blueprints flat on the table to read them, and you know that if you don't write down your measurements, you will forget them.

Writing code in Python isn't much different. Many beginners treat programming like casting magic spells out of a textbook—typing commands without understanding where that data goes or why it behaves the way it does. This leads to massive frustration the moment a program doesn't run the way they expect.

To write great software, you don't need a degree in computer engineering, but you *do* need a clear mental model of the digital workshop where your Python code will perform. Let's look at how a computer actually manages your instructions.

---

## Learning Outcomes

By the end of this lesson, you will be able to:

* **Identify** the distinct roles of Storage, RAM, and the CPU during code execution.
* **Explain** how Python reads and evaluates a script from top to bottom.
* **Describe** how Python uses variables as labels pointing to data in memory, rather than boxes containing them.

---

## Conceptual Overview: The Hardware Trio

Every computer, whether it's a massive server or the smartphone in your pocket, relies on three core components to run your Python code. 

### Storage vs. RAM vs. CPU

* **Storage (The Storage Closet):** This is your hard drive (SSD/HDD). It holds your files, apps, and Python scripts permanently. It is massive but slow. When your computer is turned off, your code sits safely here. [Deep dive into Computer Storage](https://medium.com/@dilshandareeju/computer-storage-device-c25655abef33)
* **RAM (The Workbench):** This is your computer's temporary, active workspace. It is incredibly fast but has limited space. When you tell your computer to run a Python script, the computer copies the script from your slow storage closet and lays it out on the high-speed RAM workbench. [Deep dive into Computer RAM Memory](https://www.integralmemory.com/articles/understanding-ram-what-you-need-to-know/)
* **The CPU (The Craftsperson):** This is the processor - the actual brain of the computer. The CPU can *only* read instructions and manipulate data that is currently sitting laid out on the RAM workbench. [Deep dive into CPU](https://aws.amazon.com/what-is/cpu/)

### How Python Evaluates Your Code

When the CPU reads your Python script on the workbench, it behaves exactly like a human reading a recipe: it reads **top-to-bottom, line-by-line**. 

If line 2 tells Python to calculate a number, it will complete that calculation before it ever looks at line 3. Python will never skip ahead or predict the future. 

### Under the Hood: Labels, Not Boxes

When you write code, you will want your program to remember data. To do this, we use **variables**. 

Many introductory tutorials will tell you that a variable is a "box" that you stuff data into. **This is an inaccurate mental model that will cause you trouble later.** In Python, a variable is actually a **sticky note label**, and the data is an object sitting on the RAM workbench. 

```
[ Your Code ]        [ RAM Workbench Memory ]
   my_number   --->    ( The integer value 42 )
```

When you create a variable, Python allocates a tiny piece of space on the RAM workbench to hold the value (like the number `42`), and then assigns your variable name as a label pointing directly to that exact spot in memory. If you change what that variable means later, you are simply peeling off the sticky note and slapping it onto a new piece of data. 

When your Python program finishes running, the workbench is completely wiped clean by your computer, and those spaces in memory are freed up for other tasks.

---

## Assignments

To prepare for your first coding session, read through the official Python documentation to see how the language introduces itself. 

* [The Python Tutorial - Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html): Focus deeply on why Python is useful and how it handles scripts.
* [Real Python - Interactivity with Python](https://realpython.com/interacting-with-python/): Focus on the sections explaining how Python code is executed line-by-line.

---

## Knowledge Checks

Before moving on to the practical challenge, ensure you can comfortably research and answer these architectural questions using the assignments above:

1. What does it mean when developers say Python is an "interpreted" language regarding how it executes code top-to-bottom?
2. If your computer suddenly loses power while a Python program is running, what happens to the data that was stored in RAM? Why?
3. If two different variable names are pointed at the exact same value in memory, does Python create two copies of that value on the workbench? 

---

## 🏆 The Ledger Challenge

Let's test your understanding of top-to-bottom execution and how variables point to data. 

Below is a broken Python script. Because Python reads code strictly line-by-line, it will crash if you try to use a variable label before you have actually created it and pointed it to data.

### Your Task
Rearrange and fix the lines of code below so that the script runs from top to bottom without crashing. 

```python interactive

# 1. Try running this code as-is to see the error Python throws!
# 2. Fix the order so the variables are created BEFORE they are printed.

print("The workbench says our total is:")
print(total_tools)

total_tools = 15
```

> 💡 **Documentation Hunting Tip:** Look closely at the error message you get when running the broken code. Search the official Python documentation or your assignment links for the phrase `NameError`. Understanding what a `NameError` means under the hood is a superpower for a beginner.

---

## Next Steps

Now that you have a solid mental model of the workbench and how Python reads your code line-by-line, we are ready to open the toolbox. In the next lesson, we will look at **Built-in Data Types** and learn how to create different kinds of data on our memory workbench.
