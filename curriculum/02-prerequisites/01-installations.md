---
id: installations
title: Installations
sidebar_label: Installations
sidebar_position: 1
---
# Installations
## Introduction
First step to building any software is to have the right tools. For us developers, this means having to set up our **local development enviroment**.

Many online courses (as well as ours) use in-browser code editors or *sandboxes* which provide some level of control for the given task but not much more. We will use these *sandboxes* throughout the course to demonstrate how code works. Projects on the other hand expect of you to use your own **local development enviroment** and will not provide code editor on the webpage itself.

We won't lie to you. Installing packages, editors or even whole operating systems can be a daunting task but essential in your skill set.

## Lesson Overview
In the following lesson your will learn to:
* Set up a proper environment to follow The Python Ledger curriculum

## Supported Operating Systems
The Python Ledger supports *unix-based* operating systems:
* MacOS
* Linux (Ubuntu and official flavours)

### MacOS
MacOS is an operating system that ships with Apple laptops. It is an *unix-based* operating system and by installing just a few things, you are ready to go.

### Linux (Ubuntu and official flavours)
[Linux](https://en.wikipedia.org/wiki/Linux) is an free, open-source operating system that is extremly well with almost all programming languages. Most development tools are written for *Linux* first. Your tools will be most up to date, have the best documentation and generally running better on a *Linux* operating system.

## Why Limited Support (no Windows)
Because most of the development tools are written for Linux operating system, you need to have a dedicated environment even if you plan on using *Windows* as your development OS in the feature. This also helps us all to get on the same page when requesting help in our community or in general public. Windows has its special quirks and writing instructions specific to *Windows* would be tedius and time-consuming.

Does this means you need to get rid of *Windows*? No. There are varius options for you to use both *Windows* and *Linux*.
* A `VirtualBox` virtual machine (VM)
* Dual-booting
* Windows Subsystem for Linux version 2 (WSL2)

### `VirtualBox` Virtual Machine
A [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) (VM) is a simulated computer inside another computer. This simulated computer is called **guest** and the computer running it is called **host**.

This is very common way for you to experiment with diffrent operating systems, tools or anything else, because its separated from you **host machine** and cannot modify it.

:::info[Virtual Machines consume resources]

Your **host** operating system now has to share resources with other **guest** machines running.

If you own a system with low performances, this may be the wrong option. See **dual-booting** below.

:::

### Dual-booting
Dual-booting means installing two operating systems on your machine (for example: Windows and Linux). Then you will have an option to select which one you want when you computer starts up. Advantages over VM is that your computer can give full resources to that specific operating system usually resulting in a much quicker operations.

There is some risk due to changing your storage, but you should be fine as long as you take your time and follow instructions carefully. ** Don't mix and match varius sources.**

### WSL 2 
WSL2 is a special VM allowing you to simulate Linux directly in Windows. While powerful, it does not offer clear separation on which operating system you are working on, making it easyer for beginners to make mistakes.

## Assigment
1. If you do use Windows as your operating system, choose one of the options below to install a dedicated environment.
    * Virtual Machine (recommended) - Most easy and realiable way to get started. VM runs inside your current OS (like Windows). **Tutorial coming soon**
    * Ubuntu/Windows dual-boot - Install Ubuntu as a separate operating system alongside Windows and choose which one to start. Great for lower end systems as there is no *virtualization* step. [Step by step tutorial on dual booting](https://medium.com/linuxforeveryone/how-to-install-ubuntu-20-04-and-dual-boot-alongside-windows-10-323a85271a73)
    * WSL2 (advanced) - Run Linux from Windows. Can couse confusion with new learners.

## What's Next
Now that you have a dedicated environment, we will continue with installation of **text editor**.