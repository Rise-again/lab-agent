# from fastapi import FastAPI
# from app.models.user import User
# from app.database import Base, engine

# Base.metadata.create_all(bind=engine)  # 自动创建数据库和数据库表


# app = FastAPI()


# @app.get("/")
# def root():
#     return {"message": "FastAPI工程正在运行中"}


from fastapi import FastAPI
from app.database import Base, engine

# 导入模块，执行user.py全部代码
from app.models import user
from app.api.auth import router as auth_router

# 打印看内存里识别到哪些表！！！
print("====当前metadata内的表====")
print(list(Base.metadata.tables.keys()))

Base.metadata.create_all(bind=engine)

app = FastAPI()

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



