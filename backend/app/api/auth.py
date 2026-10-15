# 做登陆注册验证修改密码等，类似于所有权限操作的


from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.auth import LoginRequest
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse


router = APIRouter(prefix="/api/auth", tags=["权限验证"])


@router.post("/login")#post请求，用于传递JSON数据，前端传回JSON数据，FastAPI自动转成Python对象
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()

    # 账号和密码是否正确
    if not user or user.password != data.password:
        return {"code": 400, "message": "账号或密码错误"}
    return {
        "code": 200,
        "message": "操作成功",
        "data": UserResponse.model_validate(user),
    }
# from fastapi import APIRouter

# router = APIRouter(prefix="/api/auth", tags=["权限验证"])


# @router.post("/login")
# def login_test():
#     return {"msg": "测试登录"}
