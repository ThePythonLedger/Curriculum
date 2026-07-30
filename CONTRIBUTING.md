# CONTRIBUTING.md
First off, thank you for considering a contribution to **The Python Ledger**! High-quality, accessible education is built by the many, not the few.

As a contributor, you are a **"Ledger Keeper"**. Whether you're fixing a typo or designing a new module, your help keeps this roadmap accurate for the next generation of developers.

## 🏗️ Our Architecture
To keep things simple, we use a Two-Repo System:
* The Ledger (This Repo): Contains only Markdown files.
* The Engine: A separate repository that handles the website and the Python interpreter.

You do not need to know `React` or `JavaScript` to contribute here. You only need to know `Markdown` and `Python`. Its also a good idea to visit **Docusaurus** documentation as this is our rendering engine which has some additional markdown elements which you can use.

## 🛠️ How to Contribute
1. Fix a Typo or Bug
If you see a mistake in a lesson:
    1. Click the "Edit this page" button at the bottom of the lesson on the website.
    2. This will take you directly to the file on GitHub.
    3. Make your changes and submit a Pull Request (PR).

2. Propose a New Lesson or Project
If you want to add a new section to the curriculum:
    1. Open an Issue first to discuss the scope.
    2. Fork this repository.
    3. Create a new .md file in the appropriate folder (e.g., 01-foundations/).
    4. Follow the Lesson Structure below.
    5. Submit a PR for review.

## 📝 Lesson Structure
> **Interactive Sandbox:** Use the `interactive` tag > to provide a live editor if you want to do so.
> ```
>     ```python interactive
>     # Provide starter code here
>     print("Try changing this!")
>     ```
> ```
> Our engine will provide the student with code editor and runnable python interpreter right there in the browser.

Every lesson should follow this relativly short format to ensure consistency:

1. **Front Matter:** Every file must start with:
```
    ---
    id: lesson-slug
    title: Human Readable Title
    sidebar_position: X
    sidebar_label: X. Introduction
    ---
```
> If the document you are writing is a **lesson**, be sure to **tag** it as such by adding `lesson: true` to front matter.
> ```
> lesson: true
> ```

2. **Theory:** A concise explanation of the concept (2–3 paragraphs max)

3. **The Challenge:** A small task the student must complete to prove they understood the concept.

## 🐍 Style Guide
* **Tone:** Encouraging, professional, and clear. Avoid overly academic jargon.
* **Python Version:** All code examples must be compatible with Python 3.10+.
* **Code Style:** Follow PEP 8 standards. Use 4 spaces for indentation.
* **Simplicity:** If a concept can be explained with a cat analogy instead of a mathematical proof, choose the cat.

## 🚦 Pull Request Process
* Ensure your Markdown is valid and links are not broken.
* Your PR will be reviewed by a maintainer.
* Once merged, the Engine will automatically detect the changes and rebuild the live site within minutes.

## 📜 Code of Conduct
By contributing, you agree to uphold our Code of Conduct. We are dedicated to providing a harassment-free experience for everyone, regardless of skill level or background.