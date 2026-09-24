# 🛠️ How to Contribute

Thanks for helping improve this project! Every contribution counts, from fixing a single typo to writing a whole new lesson.

## Which path is mine?

| I want to... | What to do | Issue needed? |
|---|---|---|
| Fix a typo, broken link, or small mistake in an existing lesson | [Quick fix](#-quick-fix-typos-and-small-bugs) | ❌ No |
| Add a new lesson or project | [New lesson or project](#-new-lesson-or-project) | ✅ Yes, assigned to you |
| Make a bigger change to existing lessons (rewrites, many files) | [Bigger change](#-bigger-changes) | ✅ Yes, assigned to you |
| Suggest an idea or report something I can't fix myself | [Open an issue](https://github.com/OWNER/REPO/issues/new) | n/a |

> Not sure which one fits? Open an issue and ask. We're happy to help.

---

## ⚡ Quick fix (typos and small bugs)

No issue and no permission needed. Just send the PR.

**A change counts as a quick fix when all of these are true:**

- It only **edits existing** Markdown files (`.md` or `.mdx`). No new files, renames, or deletions.
- It touches **3 files or fewer**.
- It changes **20 lines or fewer** in total. Fixing a single word counts as 2 changed lines (one removed, one added), so you have room for roughly 10 edited lines.

**Steps:**

1. Click the **"Edit this page"** button at the bottom of the lesson on the website.
2. This takes you directly to the file on GitHub.
3. Make your change and submit a Pull Request (PR).

That's it! A maintainer will review it.

---

## 📚 New lesson or project

New content needs to be coordinated first, so we don't end up with two people writing the same lesson.

1. **Check the [Curriculum Roadmap](/curriculum-roadmap.md)** to see which lessons still need to be written.
2. **Open an issue** describing the lesson you'd like to write and its scope.
3. **Wait to be assigned.** A maintainer will assign the issue to you. (If nobody replies after a few days, leave a comment on the issue.)
4. **Fork** this repository.
5. **Create a new `.md` file** in the appropriate folder (e.g. `01-foundations/`).
6. **Follow the [Lesson Guidelines](/lesson-guidelines.md)** so your lesson fits in with the existing lessons.
7. **Open a draft PR** as soon as you have some content. We'll label the lesson as *Being Worked On*, so others know it's taken. Our pipeline checks your document for inconsistencies automatically, even on draft PRs, so you get early feedback.
8. **Link your issue** in the PR description (see [below](#-linking-your-issue)).
9. When you're happy with it, mark the PR as **Ready for review**.

---

## 🔧 Bigger changes

If your change to existing lessons is larger than a quick fix (more than 3 files, more than 20 changed lines, or it adds/removes/renames files), follow the same steps as for a [new lesson](#-new-lesson-or-project): open an issue, get it assigned, then send a PR that links it.

---

## 🔗 Linking your issue

Add a closing keyword and the issue number to the **PR description**:

```
Closes #12
```

`Fixes #12` and `Resolves #12` work too. The issue must be **assigned to you**.

---

## 🤖 What the automatic check does

When you open a PR, a bot checks whether it's a quick fix. If it isn't, it checks that you linked an issue assigned to you.

If something is missing, the bot will:

1. Add the **`needs-issue`** label and leave a comment explaining what to do.
2. Give you time to fix it. Your PR is **not** closed right away.
3. Post a reminder after about 5 days and close the PR after about 7 days if nothing has changed. You can always reopen it once the issue is sorted out.

**To fix it**, link an assigned issue in the PR description. Editing the description re-runs the check automatically, and the label and comment disappear once everything is fine.

---

## ❓ FAQ

**My PR got the `needs-issue` label. Did I do something wrong?**
No! It just means your PR is bigger than a quick fix or has no assigned issue linked. Follow the steps in [Linking your issue](#-linking-your-issue).

**The bot says my issue isn't assigned to me.**
Comment on the issue to claim it and wait for a maintainer to assign it. Then edit your PR description (or push a new commit) to re-run the check.

**My PR was closed automatically.**
It stayed without an assigned issue for about a week. Claim an issue, then reopen the PR.

**I only fixed a typo but the bot still complains.**
Check that you only edited existing `.md`/`.mdx` files, stayed within 3 files and 20 changed lines, and didn't add or rename any file. If it still looks wrong, leave a comment and a maintainer will take a look.

**Can I work on a lesson without opening a draft PR?**
Yes, but a draft PR helps us mark the lesson as *Being Worked On* and lets the pipeline give you feedback early.

---

Thank you for contributing! 💙
