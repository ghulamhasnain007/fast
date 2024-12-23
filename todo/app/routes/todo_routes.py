from fastapi import APIRouter, Path;
from app.controllers.todo_controller import printFunction, get_student_by_id, get_student_by_name;
from typing import Optional

router = APIRouter()

@router.get('/todos')
async def add_todo():
    return await printFunction()


@router.get('/student/{student_id}')
async def get_students(student_id: int = Path(..., description="Write the ID of the student", gt=0)):
    return await get_student_by_id(student_id)


@router.get('/get-by-name/{student_id}')
async def student_name(*,student_id, name: Optional[str] = None, test: int):
    return await get_student_by_name(name)


    
# @router.get('/student/{student_id}')
# async def get_students(student_id: int):
#     return await get_student_by_id(student_id)

# gt -> greater than
# lt -> less than
# ge -> greater than equal to 