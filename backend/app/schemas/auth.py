from pydantic import BaseModel, EmailStr




class LoginRequest(BaseModel):#接收前端传回JSON转成Python对象
    username: str
    password: str