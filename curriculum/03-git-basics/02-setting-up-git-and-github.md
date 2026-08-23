---
id: setting-up-git
title: Setting up Git and Github
sidebar_label: Setting up Git & Github
sidebar_position: 2
lesson: true
---
# Setting up Git and Github
## Introduction {#introduction}
Learning `git` is very important as we mentioned before, and you will become very much familiar with it. Don't stress out about the current lesson too much, the goal is to set you up, as we will cover more `git` in feature lessons.

## Lesson Overview {#overview}
In this lesson you will learn:
* What exactly is Git
* What exactly is Github
* Install and configure `git`
* Create Github account
* Connect Git to Github

## Installing Git
Follow guide on installing `git` depending on your own operating system (**Note:** These are external resources until we make our own guides). Only follow installation instructions for now, do not yet configure it.
* [Linux](https://ubuntu.com/developers/docs/explanation/use-vcs/#getting-git)
* [MacOS](https://www.freecodecamp.org/news/setup-git-on-mac/)
* [WSL2](https://www.git-tower.com/blog/git-wsl#configuring-git)

## Make Github Account
Go to [github.com](https://github.com/) and create an account. You will need a valid email where GitHub can contact you in the feature. This will also be default for identifying your contributions. 

:::note[If you are woried about privacy]

If you don't want to have sign-up email listed in your contributions, there is an option to hide it **after** you log in.

In **Email Settings** page, set these two options to **ON**.
* Keep my email address private
* Block command line pushes that expose my email
This will prevent your email from leaking from your contributions. If you wish so, you can use the email generated for you by Github, which is shown in **Keep my email address private** section. Make sure you note it, as you will need it in the next steps.

:::

### Set up 2FA (Optional)
To set up 2-factor auth, follow [Configuring two-factor authentication](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication).

## Connect Git with Github
For `git` to work as intended, you need to provide the credentials it can use to represent your local user (you) to Github.

### Who Are You
First, we need to tell Git what is your username and password. Enter the below commands, one by one, but make sure you provide your own (Github) username and email (be it your personal one you registered for account on Github or Github generated one).
```sh
git config --global user.name "Your Name"
git config --global user.email yourname@example.com
```

### Change Default Branch
Github changed the name of the default branch from `master` to `main` so let's reflect that with this command:
```sh
git config --global init.defaultBranch main
```

## Verify Your Inputs
Before next steps, we should check if we have done everything good. Run these commands one by one and see if they match your information.
```sh
git config --get user.name
git config --get user.email
```

### Create SSH Key
SSH key is cryptographically secure identifier, like a long password used to identify your device. Github uses SSH keys to allow you access to your repositories without asking for a password each time.

First, let's make sure you have *ed25519* algorithm already installed. Run the following command:
```sh
ls ~/.ssh/id_ed25519.pub
```
If an error apears stating **No such fule or directory** then you do not yet have required key and you need to generate one. If no such message appears, you can proceed to the next step.

To create a new SSH key run the following command:
```sh
ssh-keygen -t ed25519
```
When it asks for the location, just press <kbd>Enter</kbd> for the default location. 

Next it will ask for a passphrase; this is like a password for SSH key stored on your machine and you will be asked for it on each use of SSH key. If you do not use passphrase your SSH key will not be encrypted and can be seen or modified with other users of your machine. Enter one if you wish but it is NOT required to do so.

If you choose a passphrase enter it, or if you dont wish to use it, leave it blank and just press <kbd>Enter</kbd>.

### Tell Github Your SSH Key
Now we need go tell Github what is your SSH key. Open Github webpage, then click on your profile picture (top right corner), then `Settings`, then `SSH and GPG keys`. Then click on the green button that says `New SSH Key`.

Give your key some descriptive name, so you will know it belongs to that machine, and leave the window open while you complete the next steps.

Now we need to copy our public half of SSH key. To do this we are going to use that `cat` command we mentioned in the **Command Line** lesson. Open your terminal and run the following command:
```sh
cat ~/.ssh/id_ed25519.pub
```

Select and copy **whole** output of the command, if you followed the instructions above, the output will probably start with `ssh-ed25519` and end with `username@hostname`. 

Now go back to Github window and paste the copied SSK key into the key field. Keep the key type as `Authentication Key` and finally click `Add SSH key`.

You are done, you have successfully connected your local Git with remote Github. All that is left to do is test the connection.

### Test Connection
Test your SSH key by following [GitHub’s directions for testing your SSH connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection?platform=linux). Make sure the fingerprint output in the terminal matches [one of GitHub’s four public fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints).

You should see this response in your terminal: 
```
Hi username! You've successfully authenticated, but GitHub does not provide shell access. 
```
Don’t let GitHub’s lack of providing shell access trouble you.

If you see this message, you’ve successfully added your SSH key and you can move on. If the output doesn’t correctly match up, then try going through these steps again or come to our Discord server to ask for help.

## What's Next {#next-lesson}
In the next lesson we take a look at basic `git` commands, what they do and we create our first repository, both local and remote, so let's jump right in!