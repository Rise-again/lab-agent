//这个request就是request.js里最后导出的service
import request from '@/utils/request'

//登录请求，以后所有请求都如此封装,注意后端请求路径不要写错
export function loginApi(data) {
  return request({
    url: '/api/auth/login',
    method: 'post',
    data
  })
}

//注册的API
export function registerApi(data) {
  return request({
    url: '/api/auth/register',
    method: 'post',
    data
  })
}
