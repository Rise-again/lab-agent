//这个request就是request.js里最后导出的service
import request from '@/utils/request'

//登录请求，以后所有请求都如此封装
export function loginApi(data) {
  return request({
    url: '/api/auth/login',
    method: 'post',
    data
  })
}
