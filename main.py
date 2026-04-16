from fastapi import FastAPI
from model import Student
import uvicorn
import asyncio

app = FastAPI()

students = []

@app.get("/students/")
def read_students():
    return {"Message": students}

@app.get("/students/{student_id}") #/crew_path/(1-4)
async def read_student_by_id(student_id: int):
    for stud in students:
          if stud ["id"] == student_id:
                return stud

@app.post("/students/")
async def add_student(student: Student):
     students.append(student.dict())
     return {"message": "Student added succesfully"}

@app.put("/student/{student_id}")
async def update_student(student_id: int, updated: Student):
     for i, stud in enumerate(students):
          if stud["id"] == student_id:
               students[i]  = updated.dict()
               return{ "message": "Student updated successfully"}
          
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
     for i, stud in enumerate(students):
          if stud ["id"] == student_id:
               del students[i]
               return {"message": "Student deleted successfully"}
        
@app.get("/students-delay/")
async def delayed_students():
     await asyncio.sleep(2)
     return {"message": students}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
