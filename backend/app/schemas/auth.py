from pydantic import BaseModel, EmailStr

from app.schemas.user import UserResponse


class LoginRequest(BaseModel):  # 接收前端传回JSON转成Python对象
    username: str
    password: str


class LoginResponse(BaseModel):
    token: str
    user: UserResponse
