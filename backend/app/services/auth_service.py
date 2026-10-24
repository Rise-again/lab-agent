# 登陆权限相关逻辑写于此处
from os import name

from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse
from app.schemas.auth import LoginRequest, LoginResponse, RegisterRequest
from app.utils.jwt import creat_access_token
from app.utils.password import verify_password, hash_password
from app.common.exceptions import BusinessException


# 登录
def login(db: Session, data: LoginRequest):
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
    return LoginResponse(token=token, user=UserResponse.model_validate(user))


# 注册
def register(db: Session, data: RegisterRequest):
    # 根据用户账号查询数据库
    user = db.query(User).filter(User.username == data.username).first()
    if user:
        raise BusinessException(message="账号已存在")
    user_model = User(
        username=data.username,
        password=hash_password(data.password),
        name=data.name or data.username,  # username作为默认昵称防止用户没有上传而报错
        role="student",  # 默认注册的都是学生，管理员不用注册
        status=1,
    )
    db.add(user_model)  # 存储
    db.commit()  # 提交
    db.flush()  # 刷新
