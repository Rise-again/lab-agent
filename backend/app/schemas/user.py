from pydantic import BaseModel, ConfigDict


class UserResponse(BaseModel):
    id: int
    username: str
    email: str | None = None
    name: str
    role: str
    phone: str | None = None
    status: int

    model_config = ConfigDict(from_attributes=True)#Python对象转成JSON对象返回给前端，from_attributes=True表示从属性中获取数据