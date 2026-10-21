# 做登陆注册验证修改密码等，类似于所有权限操作的


from fastapi import APIRouter, Depends, HTTPException, status
from app.common.exceptions import BusinessException
from app.common.response import Response
from app.schemas.auth import LoginRequest, LoginResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse
from app.utils.jwt import creat_access_token
from app.utils.password import verify_password

router = APIRouter(prefix="/auth", tags=["权限验证"])


@router.post(
    "/login"
)  # post请求，用于传递JSON数据，前端传回JSON数据，FastAPI自动转成Python对象
def login(data: LoginRequest, db: Session = Depends(get_db)):
    # 根据用户账号哈寻数据库
    user = db.query(User).filter(User.username == data.username).first()
    # 账号和密码是否正确
    if not user or not verify_password(data.password, user.password):
        raise BusinessException(message="账号或密码错误")
    # 验证账号状态
    if user.status != 1:
        raise BusinessException(message="账号已被禁用")
    # 创建token
    token = creat_access_token(user.id)
    # 返回信息
    return Response.success(
        message="登录成功",
        data=LoginResponse(token=token, user=UserResponse.model_validate(user)),
    )


# 已用统一封装格式表达数据
