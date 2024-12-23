# def printFunction():
#     return {"name": "Hasnain"}

students = {
    1:{
        "name": "Abbas",
        "age": 20,
        "class": 12
    },
    2:{
        "name": "Ali",
        "age": 28,
        "class": 12
    },
}
async def printFunction():
    return {"name": "Hasnain"}

async def get_student_by_id(student_id: int):
    student = students.get(student_id)
    if not student:
       return { "detail" : "student not found" }
    return student

# async def get_student_by_name(name: str):
#     student = students.get(name)
#     if student:
#         print(student)
#         return student
#     return {"Data": "Nothing there"}

async def get_student_by_name(name: str):
    # print(name)
    # student = students["id"].get(name)
    # print(student)
    # if student:
        # return student
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Nothing found for this name"}


async def register_user(user):
    print(user)
    return {"message": "user register"}