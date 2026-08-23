---
id: git-basics
title: Git Basics
sidebar_label: Git Basics
sidebar_position: 3
lesson: true
isDraft: true
---
# Git Basics
## Introduction {#introduction}
Now that we have connected `git` with `github` we can learn some `git` basics.

Git comes with a lot of commands, and is extremly powerful software. For now, we will focus on a few basic commands that you will use daily.

We belive in learning by doing, so let's go in this direction and prepare yourself for the assignments when we start working with python code.

## Lesson Overview {#overview}
In this lesson you will learn:
* What are `git` specific terms
* How to create a local repository
* How to add files to be tracked by `git` and **commit** changes to those files 
* How to create and connect remote repository (from *Github*) to your local repository, then pushing changes to remote repository.

## Learn How Git Speaks
Before starting with commands, it's useful to get to know ourself with some wording `git` uses:
* **Repository**: A folder for your project. Each `git` project is a **repository** (or **repo** for short).
* **Commit**: A snapshot of your code at the time of creating **commit**. Commits are what allow you to undo your changes to any older commit at any time.
* **Branch**: A parallel codebase for you to experiment with and build new features without affecting the **main** branch
* **Pull Request (PR)**: When work on the branch is finished, you issue a pull request to your *main* branch so changes can be *merged*.
* **Remote**: A copy of your repository NOT on your local machine (etc.: *Github*)

## Assignment {#assignment}
1. Choose a directory on your local computer where you will store all of your projects and `cd` into it. For example create a directory called `Projects` in your `Documents` directory. For the rest of the course, we will assume your `Projects` directory has the following path: `~/Documents/Projects`.
2. Create a new directory by executing `mkdir simple-python-shop`, then `cd` into it by executing `cd simple-python-shop`.
3. Initialize `git` repository by executing `git init` command. This tells `git` to start tracking for changes in our directory. 
4. Let's create a `README.md` file as every good repository should have one. Open your code editor in that directory by executing `code .` command (**NOTE:** don't forget the `.` at the end of the command). Create a new file with the name `README.md` and write some content in it, like:
    ```
    This is the start of my python journey!
    ```
    Or whatever contents you want.
5. Let's check the status of our repository by executing `git status` command. You will see your `README.md` in the section **untracked files**. This means `git` knows about your file, but it's not part of the snapshot it will create, so let's fix that in the next step.
6. By executing `git add README.md` we say to `git` that we want to add that file to **staging area** which is like a space where git is aware of your files and which will be included in the snapshot (commit). Like saying a photographer to line up and frame the shot. Now we take the actuall snapshot (commit) in the next step.
7. Execute `git commit -m "Add README file with initial content"` command which tells `git` to make the actuall snapshot (or **commit**). `-m` stands for **message** and its **required** in *commit* command, and not supplying it will open your default terminal text editor to enter the message. Message should be short but descriptive note explaining what you changed and why.
8. Now let's upload our files to *Github* (or **push** the changes we made). First we need to create a repository in our *Github*. Go to [github.com/new](https://github.com/new) and enter the name for your new remote repository. You can use the same name as your local directory: `simple-python-shop`.  Then choose visibility setting (public or private). **DO NOT** create files *Github* offers: *README*, *.gitignore*, *license*; we will do these manually. Click on the green *Create repository* button.
9. Github will offer varius ways of getting things done, but the main thing you should be looking for is the command starting with `git remote add origin`. Copy that whole line and paste it in your terminal (be sure you are in our current directory (`simple-python-shop`)). The line should look something like `git remote add origin https://github.com/your-username/simple-python-shop.git`. Execute the command to add our remote repository as **remote** to our current git repository, so we can **push** the changes we made to online repository. 
10. Now run `git push -u origin main` to send files to your *remote* we just added in the previus step. The `-u` flag is used only **first time** you push to set up *tracking connections* so in later pushes, we can just do `git push`.
11. Check your *Github* for pushed code. You should see your `README.md` sitting there on your repository view. Congratulations! You’ve just mastered the fundamental workflow of Git and GitHub.

## What's Next {#next-lesson}
We are finally done with introductions and essential setup so we can start with python lessons. Let's learn.