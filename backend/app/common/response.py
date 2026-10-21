# 用于封装统一的返回格式


from email import message
from typing import Any
from pydantic import BaseModel


class Response(BaseModel):
    """统一封装的返回格式"""

    # 状态码，反应请求成功或失败
    code: int
    # 反应具体什么错误
    message: str
    # 返回数据库数据
    data: Any = None

    # 定义类级别的方法@classmethod
    @classmethod
    def success(cls, message: str = "请求成功", data: Any = None):
        return cls(code=200, message=message, data=data)

    @classmethod
    def error(cls, code: int = 500, message: str = "请求失败"):
        return cls(code=code, message=message)
