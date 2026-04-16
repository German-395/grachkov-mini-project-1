from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class Semester(str, Enum):
    fall = "Fall"
    spring = "Spring"
    summer = "Summer"

class Enrollment(BaseModel):
    course_name: str = Field(min_length = 3)
    semester: Semester
    grade: int = Field(ge = 0, le = 100)

class Student(BaseModel):
    id: int 
    name: str = (Field(min_length = 4))
    age: int = (Field(gt = 16, lt = 35))
    enrollments: List[Enrollment] = []