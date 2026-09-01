import sqlite3


DB_NAME = "students.db"


def create_connection():
    """Create and return a SQLite database connection."""
    connection = sqlite3.connect(DB_NAME)
    return connection


def create_table(connection):
    """Create the students table if it does not already exist."""
    pass


def add_student(connection, name, age, grade, major):
    """Insert a new student record into the database."""
    pass


def list_students(connection):
    """Return all student records from the database."""
    pass


def update_student_grade(connection, student_id, new_grade):
    """Update the grade for a student with the given ID."""
    pass


def delete_student(connection, student_id):
    """Delete a student record by ID."""
    pass


def main():
    connection = create_connection()
    create_table(connection)

    # Add sample students here
    # list_students(connection)
    # update_student_grade(connection, 1, "A")
    # delete_student(connection, 2)

    connection.close()


if __name__ == "__main__":
    main()
