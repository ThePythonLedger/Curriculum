# 📝 Lesson Structure
Lessons should always follow the same structure. You can use [Lesson Template](/templates/lesson-template.md) to quickly scaffold skeleton of your lesson.

1. **Front Matter** - we use front matter to organize our lessons. Some of the tags are required and some of them are optional.
    * `id`(**required**) - identifier for the lesson. Keep it short and with no spaces (use `-` for replacing space)
    * `title` (**required**) - human readable title to be shown at the top of the lesson
    * `sidebar_label` (**required**) - human readable label on the sidebar
    * `sidebar_position` (**required**) - position of the lesson in the respective directory
    * `lesson` (**optional**) - marks the document as a lesson, enabling tracking of progress, and providing *Mark as Complete* button at the end of the lesson.
    * `isDraft` (**optional**) - marks the lesson as *Work in Progress / Draft* and displays the warning on the lesson (but still visible on the live page)
2. **Introduction (The "Why"):** Hook the student with a real-world problem or pain point before providing the code solution.
3. **Learning Outcomes:** A concrete, bulleted list of what they will confidently understand/do by the end.
4. **Conceptual Overview:** High-level architectural logic. Explain why do we use the specific concept and explain the basics behind the idea of a concept. Keep it simple and concise.
5. **Lesson Content:** Provide the basic examples and mention basics of using the related subject. Do not list every possible function / method as the point is to focus students on learning to search for solutions and reading documentation rather then spoon feeding them.
6. **Learn More section:** Use our *custom admonition* to point students to documentation or well written articles. Learn how to use it below. Make sure you give them exact directions on what to focus on, rather then letting them get lost in rabbit hole. For example provide a link to external resource and say: `Read thrue sections 1.3 to 1.6` to learn about list comprehension. 
7. **Check Knowlege section:** A set of questions student should be able to answer after finishing with the lesson (and documentation hunting). Be sure to include questions that are not mentioned in the lesson body so students must search documentation to find the answer.
8. **Exercise Section:** Content of the lesson (including documentation hunting) should be distilled into a meaningful exercise, that students will solve on their own machines. **Do not provide interactive editor for this section.** Exercises are test based (`pytest`) and are done with "levels" (by using `@pytest.mark.skip` decorater on all tests execpt the first one). See the [repository](https://github.com/ThePythonLedger/python-exercises) to learn more about writing exercises. When submitting a lesson, you must also submit an exercise that follows it.
9. **Assigment Section:** Assigment is also a required section, but unlike exercises, assigments follow a storyline from the start of the lessons - `simple-python-shop`. Students are encouraged to build and modify their existing project, following the lessons. **Do not provide interactive editor for this section.** Students complete this step on their own machines.
10. **What's Next section:** A 1-2 sentence conceptual bridge to the next lesson.

### Useful Features to Use
In addition to [standard markdown](https://www.markdownguide.org/) and [Docusaurus markdown](https://docusaurus.io/docs/markdown-features) we have a few custom built components.
* **Interactive python interpreter** - an interactive browser-based python interpreter (built with **Skulpt**) provides instant running of python code right there in the browser, reducing context switching and providing instant feedback on the code. This is intended for bringing code examples to life but should not be used for exercises or assigments which are to be done on local machine. All you need to do is to add `interactive` to your code blocks ans it takes care of the rest.
    ```
        ```python interactive
        print("Hello World!")
        ```
    ```

* **Custom *Learn More* admonition** - in addition to Docusaurus provided admonitions, we have implemented a custom one for *Learn More* section. To create such admonition, use standard Docusaurus syntax with `explore` keyword.

## ⚠️ No AI in lesson content
We strongly belive that human written content has way more value and can teach a lot more then AI generated content can, so please do not use AI to write the content. If you do not have the time or knowlege, do not use AI as it will be rejected.

## ⚠️ Guidelines & What to Watch Out For
 * **❌ Don't list every method.** Do not give a table of every string or list method. Give them one example, then send them to the official docs to discover the rest.
 * **✅ Accurate Mental Models.** Avoid overly childish analogies, but also avoid assuming knowledge the student doesn't have yet. Don't reach for systems-level concepts like threads, processes, or execution contexts — a beginner has no scaffolding for these. Instead, build correct foundational models they *can* understand. Accuracy means not teaching things that will need to be "un-taught" later, not front-loading advanced vocabulary. Keep it simple, concise and provide links to external documentation and articles.
 * **❌ No Spoilers.** Do not provide answers to the Knowledge Checks in the lesson body.
 * **✅ Link Guidance.** When adding an assignment link, explicitly state *what* they should focus on (e.g., *"Focus deeply on sections 5.1 through 5.3"*).
 * **✅ Keep it Interactive.** Ensure all challenge blocks use the interactive flag for our Skulpt execution environment. Just add `interactive` to your code block and our engine takes care of the rest.