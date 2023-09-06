# Task Manager CLI

A command-line interface (CLI) application for managing tasks with a relational database and sorting algorithm.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create and manage user accounts.
- Add, update, and delete tasks.
- Categorize tasks and list them by category.
- Sort tasks using a QuickSort algorithm.
- Organize tasks by user.
- SQLite database for data storage.

## Project Structure

The project is organized into modules and follows best practices:

task_manager_cli/
├── task_manager/
│ ├── init.py
│ ├── models.py
│ ├── database.py
│ └── tasks.py
├── cli.py
└── Pipfile

bash
Copy code

- **task_manager:** Contains SQLAlchemy models, database configuration, and task-related functions.
- **cli.py:** The main CLI application with user commands.
- **Pipfile:** Dependency management file for Pipenv.

## Getting Started

### Prerequisites

Make sure you have the following software installed:

- Python 3.x
- Pipenv

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/task-manager-cli.git
   cd task-manager-cli
2. Create a virtual environment and install dependencies:

bash
Copy code
pipenv --python 3.8  # Choose your Python version
pipenv install
# Usage

To use the Task Manager CLI, follow these steps:

* Create the database tables:

bash
Copy code
pipenv run python cli.py
* Add a user:

bash
Copy code
pipenv run python cli.py add_user
* Add tasks:

bash
Copy code
pipenv run python cli.py add_task
* List tasks:

bash
Copy code
pipenv run python cli.py list_tasks

For more commands and options, see the Commands section.

# Commands

* add_user: Add a user to the system.

bash
Copy code
pipenv run python cli.py add_user --username USERNAME
* add_task: Add a task for a user.

bash
Copy code
pipenv run python cli.py add_task --title TASK_TITLE --description TASK_DESCRIPTION --username USER_USERNAME --category TASK_CATEGORY
* list_tasks: List tasks for a user.

bash
Copy code
pipenv run python cli.py list_tasks --username USER_USERNAME

For more commands and options, refer to the CLI help messages.

# Contributing 

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

* Fork the repository.
* Create a new branch for your feature or bug fix.
* Make your changes and write tests if applicable.
* Ensure all tests pass.
* Create a pull request with a clear description of your changes.
# License

This project is licensed under the  MIT License.
