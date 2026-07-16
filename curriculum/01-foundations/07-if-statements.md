---
id: if-statements
title: If Statements
sidebar_label: 7. If Statements
sidebar_position: 7
---

## Introduction (The "Why")

Imagine building an automated ledger system that processes thousands of transactions a minute. If a transaction amount is standard, it passes right through. But what if a user attempts to withdraw more money than they possess, or tries to execute a multi-million dollar transfer? If your code treats every single line of data exactly the same way, your system will either crash or allow fraudulent activity.

In programming, we cannot rely on linear execution where every line of code runs sequentially from top to bottom. We need our code to make decisions at runtime based on dynamic data. Python solves this using **Conditional Statements** (`if`, `elif`, and `else`), which act as the decision-making forks in your program's execution path.

---

## Learning Outcomes

By the end of this lesson, you will confidently be able to:
* **Explain** how Python evaluates conditions to boolean values (`True` or `False`) to determine execution flow.
* **Master** Python's strict block structuring rules and avoid devastating `IndentationError` bugs.
* **Implement** multi-branched decision pathways using nested and chained `if`, `elif`, and `else` logic.
* **Analyze** the performance implications of conditional ordering (short-circuiting logic).

---

## Conceptual Overview

Under the hood, conditional statements are controlled by **control flow branching**. 


```
[ Evaluate Condition ]
/         
True  /           \  False
v             v
[ Execute Block ]   [ Skip Block / Check Next ]
```

When Python encounters an `if` statement, it evaluates the expression next to it. This expression *must* resolve to a boolean value: either `True` or `False`. 

### Memory and the Execution Context
Unlike some languages that use curly braces `{}` to define scope, Python relies entirely on **indentation** (whitespace) to define execution blocks. When a condition evaluates to `True`, the interpreter steps *into* the indented block of code and creates a localized execution context for those statements. If the condition evaluates to `False`, the interpreter physically skips past that entire indented block in memory, jumping directly to the next unindented line of code.

Because of this, incorrect indentation isn't just a stylistic issue—it changes the actual structural logic of your program, leading to either an immediate `IndentationError` or silent logical bugs where code runs under the wrong conditions.

### The Chained Evaluation Pipeline
When chaining conditions with `if`, `elif`, and `else`, Python evaluates them sequentially from **top to bottom**:
1. **The `if` statement** is always evaluated first.
2. **The `elif` (else-if) statements** are evaluated sequentially *only if* all preceding conditions evaluated to `False`. The moment one `elif` evaluates to `True`, its block runs, and Python skips the rest of the chain entirely.
3. **The `else` statement** acts as a catch-all. It has no condition of its own and executes *only* if every single preceding condition in the chain evaluated to `False`.

---

## Assignments

To understand how Python evaluates conditions under the hood, read the following resources. Focus your energy on the specified sections:

1. **[Python Official Docs: More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)**
   * *Focus Area:* Read Section 4.1 closely. Pay attention to how `if`, `elif`, and `else` chain together.
2. **[Real Python: Conditional Statements in Python](https://realpython.com/python-conditional-statements/)**
   * *Focus Area:* Read the sections on "Grouping Statements: Indentation and Blocks" and "The `elif` Clause". Understand how Python groups statements using indentation levels.
3. **[Python Official Docs: Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)**
   * *Focus Area:* Study the "Truth Value Testing" section. Learn which built-in Python objects naturally evaluate to `False` (implicitly falsy) and which evaluate to `True`.

---

## Knowledge Checks

Before writing any code, you must be able to confidently answer the following questions. Utilize the assigned readings above to discover these answers:

1. What is the difference between an implicit truth value (truthy/falsy) and an explicit boolean value (`True`/`False`) in a Python conditional statement? Which objects in Python naturally evaluate to `False`?
2. If an `if` statement evaluates to `True` and executes its block, will any of the subsequent `elif` blocks in that same chain be evaluated? Why or why not?
3. How does Python's execution environment distinguish between a nested `if` statement (an `if` inside another `if`) and a chained `elif` statement?

---

## 🏆 The Ledger Challenge: The Security Gate

You are writing a secure gateway checkpoint for **The Python Ledger** database.

### Task
Write an authentication check using an `if/elif/else` structure:
1. Create a variable named `username` and set it to a string of your choice.
2. Create a variable named `is_admin` and set it to a Boolean value.
3. Build a conditional structure that evaluates these variables:
   * **IF** the `username` is `"Admin"` **and** `is_admin` is `True`, print: `"Full Access Granted."`
   * **ELIF** the `username` is `"Admin"` but `is_admin` is `False`, print: `"Admin access denied. Check permissions."`
   * **ELSE**, print: `"Standard User Access Granted."`

> 💡 **Documentation Hunting Tip:** Look at the assignment links regarding logical operators. You will need to combine two checks in your first conditional block. Look up how Python uses the `and` operator to combine multiple boolean conditions into a single evaluation.

```python interactive
# 1. Define your variables (Change these to test different pathways)
username = "Admin"
is_admin = False

# 2. Build your security logic below using if, elif, and else


## Next Steps
Now that you've mastered how to branch your execution path using single-variable logic, we are going to supercharge our decisions. In the next lesson, we'll explore **Logical Operators** (and, or, not) to construct sophisticated, multi-layered logical expressions.