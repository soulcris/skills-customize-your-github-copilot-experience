# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a small REST API using FastAPI that exposes student data, supports CRUD-style operations, and includes basic validation and route design.

## 📝 Tasks

### 🛠️ Build Your First API

#### Description
Create a FastAPI application that defines a simple resource for students. The app should respond to HTTP requests and return JSON data.

#### Requirements
Completed program should:

- Create a FastAPI app instance with a descriptive title.
- Define at least one GET endpoint that returns a list of students.
- Return JSON data in a clean, structured format.
- Use a list or dictionary to store sample student records.

### 🛠️ Add a Detail Endpoint

#### Description
Add a route that retrieves a single student by its identifier and returns the matching record.

#### Requirements
Completed program should:

- Create a route such as `/students/{student_id}`.
- Accept an integer or valid identifier for the student.
- Return the matching student record if it exists.
- Return a helpful error response when the record is not found.

### 🛠️ Create and Update Student Records

#### Description
Extend the API so it can create a new student and update an existing one.

#### Requirements
Completed program should:

- Add a POST endpoint to create a new student.
- Add a PUT or PATCH endpoint to update an existing student.
- Validate required fields such as `name` and `grade`.
- Return the updated item after each successful operation.

### 🛠️ Improve the API Design

#### Description
Refine the application by adding input validation and better API behavior.

#### Requirements
Completed program should:

- Use Pydantic models for request and response validation.
- Add type hints and meaningful route descriptions.
- Ensure the API returns appropriate status codes for success and errors.
- Include a brief explanation of how the app works and which endpoints are available.
