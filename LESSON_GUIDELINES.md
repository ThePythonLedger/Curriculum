### 🏗️ Required Lesson Structure
Every markdown file must contain these exact sections in order:
 1. **Front Matter:** Standard YAML metadata (id, title, sidebar_label, sidebar_position).
 2. **Introduction (The "Why"):** Hook the student with a real-world problem or pain point before providing the code solution.
 3. **Learning Outcomes:** A concrete, bulleted list of what they will confidently understand/do by the end.
 4. **Conceptual Overview:** High-level architectural logic. Explain why do we use the specific concept and explain the basics behind the idea of a concept. Keep it simple and concise.
 5. **Assignments:** 2-3 links to high-quality external resources (Official Docs, Real Python, PEPs). **This is mandatory** - **Make sure the links provided actually resolve to real resources**
 6. **Knowledge Checks:** Deep-dive questions they *must* be able to answer before moving on. Do not answer these in the text; force them to find them in the assignments.
 7. **🏆 The Ledger Challenge:** An interactive practice task using our python interactive code block. Provide a template, minimal starter code, and a "Documentation Hunting Tip" hint.
 8. **Next Steps:** A 1-2 sentence conceptual bridge to the next lesson.


### ⚠️ Guidelines & What to Watch Out For
 * **❌ Don't list every method.** Do not give a table of every string or list method. Give them one example, then send them to the official docs to discover the rest.
 * **✅ Accurate Mental Models.** Avoid overly childish analogies, but also avoid assuming knowledge the student doesn't have yet. Don't reach for systems-level concepts like threads, processes, or execution contexts — a beginner has no scaffolding for these. Instead, build correct foundational models they *can* understand. Accuracy means not teaching things that will need to be "un-taught" later, not front-loading advanced vocabulary. Keep it simple, concise and provide links to external documentation and articles.
 * **❌ No Spoilers.** Do not provide answers to the Knowledge Checks in the lesson body.
 * **✅ Link Guidance.** When adding an assignment link, explicitly state *what* they should focus on (e.g., *"Focus deeply on sections 5.1 through 5.3"*).
 * **✅ Keep it Interactive.** Ensure all challenge blocks use the interactive flag for our Skulpt execution environment. Just add `interactive` to your code block and our engine takes care of the rest.