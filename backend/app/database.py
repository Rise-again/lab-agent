from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine, DateTime
from app.config import settings
from datetime import datetime

engine = create_engine(settings.DATABASE_URL)

# 数据库session会话的连接工厂
SessionLocal = sessionmaker(bind=engine, autoflush=False)


# 获取数据库的绘画
def get_db():
    db = SessionLocal()  # 创建工厂实例
    try:
        yield db  # 寄出去
    finally:
        db.close()  # 关闭


# 公共字段存放于base类
class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, comment="主键id"
    )
    create_time: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, comment="创建时间"
    )  # datatime和DataTime类型不一样，defaul=datetime.now()是以运行设备的时间为准，defaul=datetime.now是以数据库服务器的时间为准
    update_time: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, comment="更新时间"
    )  # datatime和DataTime类型不一样，defaul=datetime.now()是以运行设备的时间为准，defaul=datetime.now是以数据库服务器的时间为准
