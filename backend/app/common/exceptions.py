# 异常处理


from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.common.response import Response


class BusinessException(Exception):
    """自定义业务异常"""

    # 构造函数
    def __init__(self, message: str, code: int = 500):
        self.message = message
        self.code = code
        super().__init__(message)


async def bussiness_expecton_hadler(reques: Request, exc: BusinessException):
    """自定义业务异常处理器"""
    return JSONResponse(
        status_code=200,
        # model_dump数据转成字典
        content=Response.error(code=exc.code, message=exc.message).model_dump(),
    )


async def http_expecton_hadler(reques: Request, exc: HTTPException):
    """二次封装Http异常处理器"""
    return JSONResponse(
        status_code=exc.status_code,
        content=Response.error(code=exc.status_code, message=exc.detail).model_dump(),
    )


async def validation_expecton_hadler(reques: Request, exc: RequestValidationError):
    """二次封装参数异常处理器"""
    return JSONResponse(
        status_code=422,
        content=Response.error(code=422, message="请求参数校验错误").model_dump(),
    )


async def validation_expecton_hadler(reques: Request, exc: RequestValidationError):
    """二次封装参数异常处理器"""
    return JSONResponse(
        status_code=422,
        content=Response.error(code=422, message="请求参数校验错误").model_dump(),
    )


async def global_expecton_hadler(reques: Request, exc: Exception):
    """二次封装全局异常处理器"""
    return JSONResponse(
        status_code=500,
        content=Response.error(code=422, message="服务器内部错误").model_dump(),
    )
