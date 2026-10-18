import jwt
from datetime import datetime, timedelta

from app.config import settings


# 创建
def creat_access_token(user_id: int) -> str:
    """创建JWT token"""
    expire = datetime.now() + timedelta(hours=settings.JWT_EXPIRE_HOURS)  # 定义过期时间

    payload = {"user_id": user_id, "exp": expire}  # exp是固定key

    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGOITHM)


# 解析
def decode_access_token(token: str) -> dict:
    """解析JWT token"""
    # print(token)
    return jwt.decode(
        token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
    )


# algorithm有两种形式，单数和复数，API要求必须用复数，并且后面必须跟一个列表，而不能是字符串
