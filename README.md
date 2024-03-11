# School Library Management System

This Python-based School Library Management System allows for easy management of student book transactions. The system is implemented using a simple Tkinter GUI and utilizes pandas for data storage.

## Features

- Add books to a student's register with date and time stamps.
- Return books and update the register accordingly.
- View the list of books currently checked out by a student.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/savasakan22/library-app.git
    cd school-library-management
    ```

2. Install the required dependencies:

    ```bash
    pip install pandas
    pip install numpy
    ```

3. Run the application:

    ```bash
    python Library_GUI.py
    ```

## Usage

1. Enter the student's name and lastname.
2. To add a book, provide the book number and name and click the "Add Book" button.
3. To return a book, enter the book number and click the "Return Book" button.
4. Use the "Show Books" button to display the books currently checked out by the student.

## File Structure

- `Library_GUI.py`: Main script containing the Tkinter GUI and user interactions.
- `Library_Class.py`: Module defining the LibraryManager class for book management.
- `library_log.csv`: CSV file storing the book transaction log.

## Requirements

- Python 3.x
- pandas

## Contributing

Feel free to contribute to the development of this project by submitting pull requests. Bug reports and feature requests can be submitted through the GitHub issues page.
