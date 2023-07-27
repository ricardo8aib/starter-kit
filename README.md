# starter-kit

This repository is designed to help you manage your Python projects efficiently with `pyenv`, `Poetry`, `Makefile`, and `pre-commit`. Each tool plays a crucial role in Python development, from managing Python versions and dependencies to automating common tasks and enforcing code quality standards. This guide will walk you through the setup and usage of these tools to streamline your development workflow.

## Prerequisites

- Ensure you have Python installed on your system.
- Install [pyenv](https://github.com/pyenv/pyenv) (Python version manager) and [Poetry](https://python-poetry.org/) (Python dependency manager) on your machine.
- Install Make (for Makefile support) and [pre-commit](https://pre-commit.com/) for code quality checks.

1. **Installing Pyenv:**
   Pyenv allows you to install and switch between multiple versions of Python. To install Pyenv, follow the instructions appropriate for your operating system from the official GitHub repository: [https://github.com/pyenv/pyenv#installation](https://github.com/pyenv/pyenv#installation)

   After installation, verify that Pyenv is set up correctly by running the following command:

   ```bash
   pyenv --version
   ```

2. **Installing Poetry:**
   Poetry is a tool for dependency management in Python projects. It simplifies managing project dependencies, virtual environments, and packaging. To install Poetry, follow the instructions from the official documentation: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

   Verify the installation by running:

   ```bash
   poetry --version
   ```

3. **Installing Make (Optional):**
   `Make` is a build automation tool that can simplify repetitive tasks. If you don't already have `Make` installed, follow the instructions for your operating system to install it.

   To check if `Make` is installed, run:

   ```bash
   make --version
   ```

4. **Installing Pre-commit:**
   Pre-commit is a handy tool to manage and enforce code quality checks before committing changes. To install Pre-commit, follow the instructions from the official documentation: [https://pre-commit.com/#installation](https://pre-commit.com/#installation)

   Verify the installation by running:

   ```bash
   pre-commit --version
   ```

5. **Using Pyenv, Poetry, Makefile, and Pre-commit with a Project:**
   Now that you have all the necessary tools installed, you can start managing your Python projects more efficiently.

   - **Create a New Project:**
     Use the following steps to create a new Python project using Pyenv, Poetry, Makefile, and Pre-commit:
     1. Create a new directory for your project:

        ```bash
        mkdir my_project
        cd my_project
        ```

     2. Set the Python version for your project using Pyenv:

        ```bash
        pyenv install 3.x.x   # Install a specific Python version (replace "3.x.x" with the desired version)
        pyenv local 3.x.x     # Set the local Python version for your project
        ```

     3. Initialize a new Poetry project in the current directory:

        ```bash
        poetry init
        ```

        After running this command, Poetry will guide you through the process of setting up your project and creating the `pyproject.toml` file. This file will hold your project's metadata and dependencies.

        - **Adding Dependencies:**
            To add new dependencies to your project, use the following command:

            ```bash
            poetry add package_name
            ```

            Replace `package_name` with the name of the dependencies you want to add. Poetry will handle the installation and update of the package, and it will automatically update your `pyproject.toml` and `poetry.lock` files to keep track of the dependencies.

        Poetry simplifies the process of managing your project's dependencies, ensuring that your project remains consistent across different environments. By following Poetry's instructions, you can effortlessly add, update, and remove dependencies while maintaining a clean and organized project structure.

     4. Create a virtual environment with Poetry:

        Poetry automatically creates and manages virtual environments for your projects. To create a virtual environment for your project, use the following command:

        ```bash
        poetry install
        ```

     5. Create a `Makefile` in your project root directory to define common tasks. A sample Makefile is available in the root folder of this repo. Use the `Makefile` tasks to execute common commands conveniently. For example, run a Python script using:

        ```bash
        make poetry run src/app.py
        ```

     6. Set up `pre-commit` hooks to enforce code quality checks before committing changes. Create a `.pre-commit-config.yaml` file in the project root directory. A sample `.pre-commit-config.yaml` file is available in the root folder of this repo.
     `pre-commit` will automatically check and fix code formatting and style issues before each commit. If any issues are found, pre-commit will prevent the commit until the issues are resolved.

     7. Install the pre-commit hooks:

        ```bash
        pre-commit install
        ```

That's it! You are now all set to manage your Python projects efficiently using Pyenv, Poetry, Makefile, and Pre-commit. These tools provide a robust and consistent way to handle Python versions, project dependencies, virtual environments, and code quality checks, making your development workflow smoother and more organized. Happy coding!
