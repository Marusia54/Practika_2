from fastapi import APIRouter, Body
from models.good import MainUser, Main_UserDB, New_Response
from typing import Union, Annotated

users_router = APIRouter()

def password_encryption(code: str):
    result = code * 2

users_list = [Main_UserDB(name="Mozer", id=325, password="**********"), Main_UserDB(name="Popov", id=7777, password="**********")]

def find_user(id: int) -> Union[Main_UserDB, None]:
    for user in users_list:
        if user.id == id:
            return user
    return None


@users_router.get("/api/users", response_model=Union[list[MainUser], None])
def get_users():
    return users_list


@users_router.get("/api/users/{id}", response_model=Union[MainUser, New_Response])
def get_user(id: int):
    user = find_user(id)
    print(user)
    if user is None:
        return New_Response(message="Пользователь не найден")
    return user


@users_router.post("/api/users", response_model=Union[MainUser, New_Response])
def create_user(item: Annotated[MainUser, Body(embed=True, description="Новый пользователь")]):
    user = Main_UserDB(name=item.name, id=item.id, password=password_encryption(item.name))
    users_list.append(user)
    return user


@users_router.put("/api/users", response_model=Union[MainUser, New_Response])
def edit_user(item: Annotated[MainUser, Body(embed=True, description="Изменение данных пользователя по ID")]):
    user = find_user(item.id)
    if user is None:
        return NewResponse(message="Пользователь не найден")
    user.id = item.id
    user.name = item.name
    return user


@users_router.delete("/api/users/{id}", response_model=Union[list[MainUser], None])
def delete_user(id: int):
    user = find_user(id)
    if user is None:
        return NewResponse(message="Пользователь не найден")
    users_list.remove(user)
    return users_list
