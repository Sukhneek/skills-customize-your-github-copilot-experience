# GitHub Copilot Instructions for the Educational Assignment Portal

This repository is an educational website for sharing homework assignments and coding exercises with students.
The site is a static portal that uses `config.json` to dynamically generate assignment listings and assignment detail pages.

## Project Purpose
- Provide a fun, student-friendly portal for browsing and downloading assignments.
- Keep content consistent, accessible, and learning-focused.
- Use clear, encouraging language that helps students stay motivated.

## Key Files and Structure
- `index.html` — Main landing page for the course and assignment list.
- `config.json` — Course metadata and assignment definitions.
- `assets/js/script.js` — Loads the configuration and renders the assignment list.
- `assets/pages/assignment.html` — Assignment details page.
- `templates/assignment-template.md` — Reusable template for creating new assignment content.
- `assignments/` — One folder per assignment with exercise content, starter files, and data.

## How to Help
When generating content or changes, follow these principles:
- Keep the learning objective clear and easy to understand.
- Use student-friendly wording: positive, encouraging, and supportive.
- Keep file names and folder names descriptive, consistent, and organized.
- Preserve the existing design style and simple navigation.
- Avoid overcomplicated language or overly advanced examples.

## Content Guidelines
- For assignment descriptions and tasks, include:
  - A short title
  - A concise objective
  - A clear “what students will learn” outcome
- Keep descriptions actionable and grade-appropriate for introductory programming.
- Use examples and instructions that align with Python basics, games, classes, or data analysis.
- When adding new assignments, update `config.json` and include a matching folder under `assignments/`.

## Code Guidelines
- Use semantic HTML and maintain the existing page structure.
- Keep CSS consistent with the current styles in `assets/css/styles.css`.
- Use plain JavaScript for dynamic page rendering, matching the existing pattern in `assets/js/script.js`.
- If adding scripts or markup, ensure they work with the existing `index.html` and `assets/pages/assignment.html` flow.

## Tone and Style
- Write in a friendly, classroom-appropriate tone.
- Use second-person perspective when addressing students (e.g. “You will practice…”).
- Focus on clarity and encouragement rather than technical jargon.
- Keep instructions short and easy to follow.

## When Updating This Repository
- Keep changes scoped to the educational portal.
- Do not add unrelated tools, frameworks, or dependencies.
- Maintain the repository’s structure and the focused learning experience.
