---
id: command-line
title: Command Line
sidebar_label: Command Line
sidebar_position: 3
lesson: true
---
# Command Line
## Introduction
Have you ever heard of  **command line** (or **terminal**)? You have certainly seen one, probably in movies depicting hackers. Those black windows with loads of white or green text, hackers hacking into the bank, mainframe or whatever else producers can think of.

That black screen with white or green text is **command line interface** (CLI). We won't be hacking anything today (or any day in this course) but you need to get familiar with basics of *command line* as its **essential** skill for a developer.

This is where you as a developer will spend most of your time (switching between code editor and CLI - in VSCode we have integrated CLI so its all in one window). We can use the command line to execute commands which do basically everything. It can be daunting at first but you will be entering the same commands many times so you will pick up the most used ones quickly. As for the others there is always google, documentation or built in help system (as we will see).

In this lesson we will take a look at same of the basics like manipulating directories (or folders as they are known in Windows world), files, and navigating your computer all from the command line. Commands in this lesson are very easy to use so dont let the "command line" scare you. You can do this !

## Lesson Overview
In this lesson you will learn the following:
* Explain what a command line is
* Open the command line on your computer
* Use the command line to manipulate directories and files
* Use the command line to navigate around your computer
* Use the command line to open some file or directory in another program (like VSCode)

## Let's Open That Scary Command Line Interface
Open a terminal (command line) on your computer.
* **Linux**: Open programs menu and search for `terminal`. You can also try the keyboard shortcut <kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>T</kbd> to open your terminal window.
* **MacOS**: Open Applications > Utilities folder and find `Terminal`. You can also use Spotlight search to open Terminal. Press <kbd>CMD</kbd> + <kbd>Space</kbd> to open Spotlight, and search for `Terminal`. Press <kbd>Enter</kbd> to open the terminal.

The window that opens will probably be mostly blank with the exception of some text and **prompt**. Depending on your operating system, the line will end with `$` (or `%` on newer MacOS) indicating that its ready for command. This is a **prompt**. Let's try our first command. Type `whoami` and press <kbd>Enter</kbd>. This returns your username. See, commands are not scary, it just takes time to practice them.

Often the instructions on various sources will use `$ whoami` examples. Do not copy or write `$` character, only the command in front of it.

## Basic Commands
Lets start by exploring our filesystem. Type in `ls` (which stands for *list*) and press <kbd>Enter</kbd>. This lists out your current directory contents. But where is that directory even located? Let's find out: type `pwd` (which stands for *Print Working Directory*) and press <kbd>Enter</kbd>. This shows your current filepath.

You are probably in your *home* directory indicated by *tilde* (`~`) character. Lets create a new directory. Type `mkdir` (stands for *Make *Directory*) followed by the name of directory. For example `mkdir test`. This will create a new directory called `test`. You can check if thats the case by running `ls` command again. It should now show your newly created `test` directory along the other files and directories from before.

We have successfully created a new directory, but for now its empty. We can check that by typing `ls` command followed by the name of the directory we want to list the contents of. So typing `ls test` will show you empty directory.

So lets go into our `test` directory. Typing `cd` (stands for *Change Directory*) followed by directory name takes us into our newly created directory. Let's try: type `cd test` and press <kbd>Enter</kbd>. Your **prompt** will change, indicating that we are no longer in previous directory but in a new one. Now let's create an empty text file (with the extension `.txt`) by typing `touch` followed by the name of the file we want to create. Let's try that now: type `touch myfile.txt` and press <kbd>Enter</kbd>. You will see no changes in your terminal other then the other **prompt** on a new line, waiting for the next command - this is completely normal. If you now run `ls` command again (remember, we are now inside the `test` directory so only `ls` is needed, no path specified after it) we will see the newly created file `myfile.txt`.

:::info[Do not close terminal window]

In the next step we will open VSCode from our terminal. Leave the terminal open and do not close terminal window as we will need it to continue practicing.

If you do happen to close terminal windows, just open it back up and navigate to our `test` directory.

:::

Now let's try something fun. We will open this file we created, but in VSCode. No, not from our menu, from the terminal. While you are in `test` directory, type `code .` (don't forget the dot (`.`)) and see how VSCode opens directly in our `test` directory. We can also see and edit our `myfile.txt` file.

Once you have played around a bit, write some content in our `myfile.txt` file, save it by pressing <kbd>CTRL</kbd> + <kbd>S</kbd> (Mac: <kbd>CMD</kbd> + <kbd>S</kbd>). Whatever you write in the file is up to you, it can be 2 letters or a whole essay. We will need some content to practice our terminal skills some more but please keep it a few lines so we don't end up with a wall of text.

Once you saved the file, you can close VSCode by pressing on the red <kbd>X</kbd> in the corner, or pressing keyboard shortcut <kbd>ALT</kbd> + <kbd>F4</kbd> (Mac: <kbd>CMD</kbd> + <kbd>Q</kbd>).

In Unix-style operating system, our current and parent directories are represented by `.` and `..`.

### Current Directory
One dot (`.`) is our **current directory**. In the command `ls` if you do not supply a path, it assumes the path is `.` (current directory). We could also write `ls .` and it would print out the same thing, but we programmers are lazy, so we made it the default option to save a few keystrokes.

### Parent Directory
Two dots (`..`) represent **parent directory**. To move back from your `test` directory to your parent directory, you would do `cd ..` and it would "go one directory up" the chain. We will try this out in a moment.

Right now you should be in your `test` directory with a file inside named `myfile.txt` that has some content in it. If you are not, please open your terminal and navigate to `test` directory. To view the content of a file, you can use `cat` command which will dump everything that the file contains into your terminal.

:::tip[Clear screen]

If you have added too much content to our `myfile.txt` file, you may end up with a wall of text when running `cat` command. To clear your screen, you can use `clear` command, or use a keyboard shorcut <kbd>CTRL</kbd> + <kbd>L</kbd> (Mac: <kbd>CMD</kbd> + <kbd>L</kbd>).

:::

Lets see `cat` command in action. Type `cat myfile.txt` and press <kbd>Enter</kbd>. You should see content of your file right there in the terminal.

Now, let's rename our file to `mytestfile.txt`. To do this we are going to use `mv` command (which stands for *move* - may seem weird but in Linux, renaming is considered moving from old filename to new one). Move command looks like:
```
mv <old_filename> <new_filename>
```
If we type `mv myfile.txt mytestfile.txt` we will essentually be renaming our file. Feel free to do so.

:::danger

If the new name already exists, `mv` will overwrite it without warning. To prevent this, use `mv -i` (interactive mode) to prompt you before overwriting.

:::

Now that we renamed (moved) file, we can also learn how to delete it. If you type `rm` (stands for *remove*) you can delete the files. **Be aware** there is no *Recyle Bin* when working in terminal. If you remove a file, its gone, so be **extremely careful** with this command. Let's type `rm mytestfile.txt` and press <kbd>Enter</kbd>. This command does not return any output, so we can use `ls` command to check if it has worked or not. If the file is gone, you can use `cd ..` to go back to parent directory.

### Tab Completion
We programmers are lazy, like really lazy (`mv` instead of `move`, `rm` instead of `remove`, etc...). Long before all this AI hype, Linux had its AI-like superpower: **tab completion**. This is an essential for your programming journey as it will shorten time it takes to write commands and make it free of errors.

Right now you should be in your terminal, in the parent directory looking at the `test` directory after `ls` command. Let's go back to `test` directory but using this superpower.

Type `cd te` and then press <kbd>TAB</kbd>. This will autocomplete the path to `cd test/` and all you have to do is press <kbd>Enter</kbd> (if you do not have any other files or directories starting with a letter `t` in your current directory, you can write just `cd t` and press <kbd>TAB</kbd>). 

In this example, maybe it seems redundant, but imagine the following command:
```
cd Documents/Coding/Projects/Excalibur
```
It takes time to write all that up, making sure that we dont misspell something or write lowercase instead of uppercase letter. Now imagine this flow:

`cd Do` > <kbd>TAB</kbd> > `Co` > <kbd>TAB</kbd> > `Pr` > <kbd>TAB</kbd> > `Ex` > <kbd>TAB</kbd> <kbd>Enter</kbd>

Practice tab completion as its very useful skill and will save you from all the typing.

### Command History
Have you ever typed a long command, made a tiny typo at the end, and dreaded retyping the whole thing? The terminal remembers everything you type during a session.

Press the <kbd>Up Arrow</kbd> key on your keyboard. Your terminal will cycle backward through your previously executed commands. Pressing the <kbd>Down Arrow</kbd> cycles back forward.

Next time you need to re-run `cat mytestfile.txt` or execute a command again, don't retype it—just press <kbd>Up Arrow</kbd> until you see it, and hit <kbd>Enter</kbd>.

### Command Flags
Commands aren't limited to a single word. You can pass **flags** (also called *options* or *switches*) to modify how a command behaves. Flags usually start with a dash (`-`).

Earlier, we used `ls` to list files. By default, `ls` hides "hidden" configuration files (files starting with a dot `.`). Let's pass the `-a` flag (which stands for *all*):

```bash
ls -a
```
Now you'll see every file, including hidden ones and those special `.` (current directory) and `..` (parent directory) markers!
You can also combine flags. For example, `-l` gives a detailed "long list" (showing file sizes and creation dates). Running `ls -la` combines both: it lists *all files* in *long format*.

General pattern to remember:
```sh
command -flag target
```

### Built-in Help System
Commands in linux usually have built in help system. If you use `-h` or `--help` with a command, it will show you its options and description on what each one does. You can also read full documentation by accessing command *manual* by typing `man <command>` (for example: `man ls`). This usually produces a large document to be viewed in your terminal. If you can't seem to exit the document viewer, press <kbd>Q</kbd>.

## What's Next?
Python is no diffrent, its basicly a command that runs your `.py` files (yes, Python file extension is `.py`).  In the next leason we will learn two Python operating modes and how to run your first python program.