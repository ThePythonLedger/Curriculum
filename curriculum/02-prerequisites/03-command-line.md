---
id: command-line
title: Command Line
sidebar_label: Command Line
sidebar_position: 3
lesson: true
isDraft: true
---
# Command Line
## Introduction
Have you ever heard of  **command line** (or **terminal**)? You have certanly seen one, probably in movies depicting hackers. Those black windows with loads of white or green text, hackers hacking into the bank, mainframe or whatever else producers can think of.

That black screen with white or green text is **command line interface** (CLI). We won't be hacking anything today (or any day in this course) but you need to get familiar with basics of *command line* as its **essential** skill for a developer.

This is where you as a developer will spend most of your time (switching between code editor and CLI - in VSCode se have integrated CLI so its all in one window). We can use the command line to execute commands which do basicly everything. It can be daunting at first but you will be entering the same commands many times so you will pick up the most used ones quickly. As for the others there is always google, documentation or built in help system (as we will see).

In this lesson we will take a look at same of the basics like manipulating directories (or folders as they are known in Windows world), files, and navigating your computer all from the command line. Commands in this lesson are very easy to use so dont let the "command line" scare you. You can do this !

## Lesson Overview
In this lesson you will learn the following:
* Explain what a command line is
* Open the command line on your computer
* Use the command line to manipulate directories and files
* Use the command line to navigate around your computer
* Use the command line to opet some file or directory in another program (like VSCode)

## Let's Open That Scary Command Line Interface
Open a terminal (command line) on your computer.
* **Linux**: Open programs menu an search for `terminal`. You can also try the keyboard shortcut <kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>T</kbd> to open your terminal window.
* **MacOS**: Open Applications > Utilities folder and find `Terminal`. You can also use Spotlight search to open Terminal. Press <kbd>CMD</kbd> + <kbd>Space</kbd> to open Spotlight, and search for `Terminal`. Press <kbd>Enter</kbd> to open the terminal.

The window that opens will probably be mostly blank with the exception of some text and **prompt**. Depending on your operating system, the line will end with `$` (or `%` on newer MacOS) indicating that its ready for command. Let's try our first command. Type `whoami` and press <kbd>Enter</kbd>. This returns your username. See, commands are not scary, it just takes time to practice them.

Often the instructions on varius sources will use `$ whoami` examples. Do not copy or write `$` character, only the command in front of it.

## Basic Commands
Lets start by exploring our filesystem. Type in `ls` and press <kbd>Enter</kbd>