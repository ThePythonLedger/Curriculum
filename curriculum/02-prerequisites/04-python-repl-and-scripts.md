---
id: python-repl-and-scripts
title: Python, REPL, and Script Files
sidebar_label: Python, REPL, and Script Files
sidebar_position: 4
lesson: true
IsDraft: true
---
# Python, REPL, and Script Files
## Introduction
As we mentioned in the previus lesson, Python is a command (a program) that you run by typing `python` (or `python3` depending on your operating system). For this to work, Python must be installed and in your `PATH`. If you have been following along with our course, Python should be preinstalled on your system, which you can verify by running `python --version` command. This will output your currently installed Python version or produce an error if there is no system-wide Python installed.

## Python has Two Operating Modes
### REPL Mode
Python REPL (stands for **R**ead, **E**valuate, **P**rint, **L**oop) is pretty powerful and very easy to use Python as an evaluation engine or some quick and dirty automation. It allows you to execute Python code evaluating it (and running) in line-by-line mode which means you get a direct feedback, rather then writing code to the file and then executing it by reading that file.

We can start Python REPL from the command line by typing `python` (or `python3` depending on your operating system). To let us know we are in Python REPL our prompt will change to `>>>`. Everything you type here should be valid Python code. Add the following line `5+2` and press <kbd>Enter</kbd>, it should output `7` - congratulations, you have just added two numbers together.

As much as this REPL is powerful and useful, we are mostly be writing our own files ending with `.py` extension, and passing those to our Python program to run. To exit our of the Python REPL you can write `exit()`.

### Script Mode
Script mode is more useful to us programmers to use as it allows us to write permanent files and have more complex file structures.

In script mode, Python reads the file you provide and executes it line-by-line. In the rest of this course, we will use script mode unless otherwise specified.

To run Python in script mode, we will need a file with an extension `.py` and we will pass that to our Python program. So let's open our `test` directory in VSCode, add a new file called `main.py` and insert a line inside:
```python
print(5+2)
```
Do not yet worry about what the code does (but you can conclude that from the code - we will learn all this in the upcoming lessons), just save the file and exit VSCode. To make sure we did everything correctly, check the contents of the file with `cat main.py` command. If the file contents matches what you written in it, you are good to go, and if not, repeat the above steps.

Now that we have a file with `py` extension, we need to pass it to our Python program by running `python main.py` (or `python3 main.py`). This will read the code inside the file, run it, and produce a result (in this case number `7` just like in REPL mode example)

## What's next?
Now that we have the basics covered, we are going for just a little trip down to `git` and **Github** land, as those are essential tools to learn as a programmer. We will just be scratching the surface of them for now, but it will be required for feature lessons and excercises as all of the content of this curriculum is saved on Github and version controlled by Git. So let's dive in.