# 📘 Assignment: Student Database with SQLite

## 🎯 Objective

Learn how to store and manage information in a database using Python and SQLite. This assignment will help you practice creating tables, inserting records, and performing CRUD-style operations with real data.

## 📝 Tasks

### 🛠️ Create the Student Database

#### Description
Create a Python program that connects to a SQLite database and creates a table named `students` to store student information.

#### Requirements
Completed program should:

- Connect to a SQLite database file named `students.db`
- Create a `students` table with columns for `id`, `name`, `age`, `grade`, and `major`
- Use appropriate data types for each column
- Print a confirmation message once the table is created

### 🛠️ Add and View Student Records

#### Description
Extend the program so it can insert student records and display all students in the database.

#### Requirements
Completed program should:

- Add at least 3 sample student records to the `students` table
- Include a function to insert a new student
- Include a function to list every student in the database
- Print each student's information in a readable format

### 🛠️ Update and Remove Records

#### Description
Add functions to search for a student, update their grade, and delete a student from the database.

#### Requirements
Completed program should:

- Add a function to find a student by `id`
- Add a function to update a student's `grade` or `major`
- Add a function to delete a student by `id`
- Demonstrate updating and deleting at least one record
- Show the final list of students after changes are made

### 🛠️ Challenge: Simple Student Dashboard

#### Description
Create a simple command-line dashboard that lets a user choose actions like add, view, update, and delete students.

#### Requirements
Completed program should:

- Display a menu with options for the user
- Let the user choose an action from the menu
- Handle invalid input safely
- Keep the program running until the user decides to exit
