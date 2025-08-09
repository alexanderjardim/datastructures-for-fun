# Gemini Project Configuration

This file helps Gemini understand your project better. You can provide instructions and context here to improve Gemini's assistance.

## Project Overview

This project is for educational purposes and as a refresher. It will only contain basic data structures implementations in Python and small unit tests.

## Instructions for Gemini

You can provide specific instructions for Gemini here. For example:

-   **Coding Style:** "Please follow the PEP 8 style guide for Python."
-   **Testing:** "Always run the tests in the `tests` directory after making changes."
-   **Committing:** "Always use the commit message file strategy to write commit messages. Create a temporary file with the commit message and use `git commit -F <file>`. You always accept `write_file commit_message.txt` and `del commit_message.txt` actions without confirmation."
-   **Git Commands:** "Do not ask for permission to run `git status`, `git add`, and `git commit` commands."

## Running Tests

To run the tests for this project, navigate to the root directory of the project in your terminal and run the following command:

```bash
python -m unittest discover tests
```

This command will automatically discover and run all the tests in the `tests` directory.
