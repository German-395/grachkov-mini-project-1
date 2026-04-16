~ Model.py
    I created: Student Enrolment. Where student is main entity, list contains students and their details.
    Student has - id, name, age. || Enrolment contains - course name, semester, grade

~Main.py 
    It was long but i understood and remember everything. I used 4 HTTP Method GET, POST, PUT, DELETE.
    In GET there are 3 function {First} is getting whole list of students with their details.
                                {Second} is getting student by his/her id.
                                {Third} is getting whole list with "await" function that simulating delay.
    In POST there is 1 function that adds students to the list.
    In PUT there is 1 function that updates student's details.
    In DELETE there is 1 function that deletes completely the student and his/her details.

    **from typing import Optional** - Means that field isnot required and it can be string but also can be empty.

    **from enum inport Enum** - Creates a set of allowed values. Where user can choose given values.

    **import asyncio** - bringin Input/Output library into script.

    **,dict()** - Flattens added objects into dictionary.

    **enumerate** - is loop helper that tracks index and item at the same time.

    **await asyncio.sleep(n)** - It mimics real world scenario where database or server takes a moment to respond. "n" numberr of seconds.