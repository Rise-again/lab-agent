# from fastapi import FastAPI
# from app.models.user import User
# from app.database import Base, engine

# Base.metadata.create_all(bind=engine)  # 自动创建数据库和数据库表


# app = FastAPI()


# @app.get("/")
# def root():
#     return {"message": "FastAPI工程正在运行中"}


from email.policy import HTTP
import http

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from app.database import Base, engine

# 导入模块，执行user.py全部代码
from app.models import user
from app.api.auth import router as auth_router
from app.api import api

# 导入异常处理器
from app.common.exceptions import (
    BusinessException,
    bussiness_expecton_hadler,
    http_expecton_hadler,
    validation_expecton_hadler,
    global_expecton_hadler,
)

# 打印看内存里识别到哪些表！！！
print("====当前metadata内的表====")
print(list(Base.metadata.tables.keys()))

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api)


# 注册自定义异常
app.add_exception_handler(BusinessException, bussiness_expecton_hadler)
app.add_exception_handler(HTTPException, http_expecton_hadler)
app.add_exception_handler(RequestValidationError, validation_expecton_hadler)
# 全局异常兜底，必须放在最后注册
app.add_exception_handler(Exception, global_expecton_hadler)


# ====新增调试打印====
from app.api.auth import router as auth_router

print(f"====auth_router路由条数：{len(auth_router.routes)}====")
for r in auth_router.routes:
    print(f"path={r.path}, include_in_schema={r.include_in_schema}")

app.include_router(auth_router)

# ===================


@app.get("/debug")
def debug():
    return {
        "tables_in_memory": list(Base.metadata.tables.keys()),
        "engine_url": str(engine.url),
    }


@app.get("/")
def root():
    return {"message": "FastAPI工程正在运行中"}
