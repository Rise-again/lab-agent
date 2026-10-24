# 做登陆注册验证修改密码等，类似于所有权限操作的

from fastapi import APIRouter, Depends


from app.common.response import Response
from app.schemas.auth import LoginRequest, RegisterRequest
from sqlalchemy.orm import Session
from app.database import get_db

from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["权限验证"])


# 登录
@router.post("/login")
# post请求，用于传递JSON数据，前端传回JSON数据，FastAPI自动转成Python对象
def login(data: LoginRequest, db: Session = Depends(get_db)):
    """登录的API接口，返回token和用户信息"""
    result = auth_service.login(db, data)
    # 返回信息
    return Response.success(
        message="登录成功",
        data=result,
    )


# 注册
@router.post("/register")
# post请求，用于传递JSON数据，前端传回JSON数据，FastAPI自动转成Python对象
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    """注册的API接口"""
    auth_service.register(db, data)  # 向数据库写入注册信息
    # 返回信息
    return Response.success(
        message="注册成功",
    )
