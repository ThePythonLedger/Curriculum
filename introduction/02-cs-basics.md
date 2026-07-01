---
id: cs-basics
title: What is a computer and how programs are executed?
sidebar_label: 2. What is a computer?
sidebar_position: 2
---

## Introduction: The Digital Workshop

Before you write your very first line of Python, you need to understand the stage where your code will perform.

You don't need a degree in electrical engineering to write great software, but you *do* need to know how a computer juggles tasks. If you don't, programming can feel like casting magic spells out of a textbook without understanding why they work—or why they suddenly blow up.

Think of your computer as a highly organized workshop. Let's look at the three main characters running this shop, how they interact, and how your future Python programs will live inside them.

---

## Learning Outcomes

By the end of this introductory lesson, you will be able to:

* **Identify** the distinct roles of the CPU, RAM, and Storage.
* **Contrast** a Process and a Thread using a real-world analogy.
* **Explain** exactly what happens to a computer's memory when a program is launched.

---

## The Hardware Trio: Brains, Desks, and Closets

Every computer, whether it's a massive server or the smartphone in your pocket, relies on three core pieces of hardware to run code:

| Component | Analogy | What it Does | Volatile? (Does it lose data when turned off?) |
| --- | --- | --- | --- |
| **Storage (SSD/HDD)** | The Storage Closet | Holds your files, apps, and games permanently. Very large, but slow. | **No** (Data stays saved) |
| **RAM (Memory)** | The Workbench | The temporary workspace where active programs sit. Super fast, but limited space. | **Yes** (Wiped clean on reboot) |
| **CPU (Processor)** | The Craftsperson | The actual brain that reads instructions and executes calculations. | **N/A** (Just processes data) |

### How They Work Together

When your computer is turned off, your Python scripts and applications sit silently in **Storage** (the closet).

When you double-click an app or run a script, the computer copies that file from Storage and places it onto the **RAM** workbench. The **CPU** can only read instructions that are sitting on the RAM workbench. If your computer runs out of RAM, your workbench is full, and everything grinds to a painful halt.

---

## What is an Operating System (OS)?

Your computer hardware is just a collection of metal and silicon. It doesn't inherently know how to draw a window on a screen, connect to Wi-Fi, or run a Python script. That is the job of the **Operating System (OS)**—like Windows, macOS, or Linux.

The OS is the workshop's manager. It decides which programs get to use the workbench (RAM) and ensures that one greedy program doesn't steal all the CPU's attention or accidentally overwrite another program's data.

---

## Programs in Action: Processes and Threads

When the OS brings a program to life in RAM, it organizes it using two concepts: **Processes** and **Threads**.

To make sense of this, imagine your computer is running a busy restaurant kitchen.

### 1. The Process (The Kitchen Station)

A **Process** is a fully isolated, independent running program. Think of it like a self-contained kitchen station (like the bakery station or the grill station).

* Each process gets its own dedicated slice of RAM that no other process is allowed to touch.
* If you open Google Chrome and Microsoft Word at the same time, they run as completely separate processes.
* If Chrome crashes, it won't take Microsoft Word down with it because their workspaces are totally separated by the OS.

### 2. The Thread (The Cooks)

A **Thread** is a single worker *inside* that process. If a process is the kitchen station, threads are the individual cooks working at that station.

* A single process can have multiple threads (cooks) working at the same time.
* Because they are all standing at the same station, they all **share the same workspace (RAM)**. They can easily hand tools and ingredients to one another.
* **The Catch:** If one cook accidentally burns down the station, the *whole* station goes down. If a single thread crashes catastrophically, the entire process crashes.

---

## How Code Occupies RAM

When you start writing Python, you will create **variables** to hold data—like names, numbers, or lists.

Every single variable you create is a physical piece of data that must sit on the RAM workbench. The moment your Python program finishes running (or you close it), the OS steps in, clears that workbench space, and makes it available for the next program.

Let's look at how this works in practice.

---

## Knowledge Checks

Before writing your first script, make sure you can answer these simple questions based on our workshop analogy:

1. Why can't the CPU just run a program directly from your hard drive (Storage) without loading it into RAM first?
2. If your computer suddenly loses power, why do you lose the progress on a document you haven't saved yet?
3. If a web browser tab freezes but you can still type perfectly fine in your code editor, are those two apps running in the same *Process* or separate *Processes*?