# Console To-Do List

A straightforward, beginner-friendly to-do list application that runs in the console. This script allows you to manage your tasks, which are saved to a local text file, so you never lose them.

---

## Features

* **View Tasks**: See all your current tasks in a clean, numbered list.
* **Add Tasks**: Add new tasks to your list.
* **Remove Tasks**: Delete tasks you have completed.
* **Persistent Storage**: Your tasks are automatically saved to a `tasks.txt` file, so they are always there when you restart the application.

---

## Requirements

* **Python 3.x**

No external libraries are needed. This script uses only standard Python libraries.

---

## How to Run

1.  **Save the Code**: Make sure the Python script (e.g., `todo.py`) is saved on your computer.

2.  **Open a Terminal**:
    * **Windows**: Open Command Prompt, PowerShell, or Windows Terminal.
    * **macOS/Linux**: Open the Terminal application.

3.  **Navigate to the Directory**: Use the `cd` command to go to the folder where you saved the `todo.py` file.
    ```bash
    cd path/to/your/folder
    ```

4.  **Run the Script**: Execute the following command in your terminal:
    ```bash
    python todo.py
    ```

5.  **Follow the Menu**: Once running, the application will show you a menu with options to manage your tasks.

---

## How It Works

This application manages tasks by storing them in a Python `list`.

Whenever you add or remove a task, the script immediately updates a file named `tasks.txt`. This file is a simple text file where each task is stored on a new line. When you start the application, it reads this file to load all your previously saved tasks.
