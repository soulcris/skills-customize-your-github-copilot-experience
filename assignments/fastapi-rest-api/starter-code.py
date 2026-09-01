from fastapi import FastAPI

app = FastAPI(title="Student API")

students = [
    {"id": 1, "name": "Alice", "grade": "A"},
    {"id": 2, "name": "Ben", "grade": "B"},
    {"id": 3, "name": "Chloe", "grade": "A"},
]


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"detail": "Student not found"}


@app.post("/students")
def create_student():
    return {"message": "Add the student creation logic here"}


@app.put("/students/{student_id}")
def update_student(student_id: int):
    return {"message": f"Add the update logic for student {student_id}"}
