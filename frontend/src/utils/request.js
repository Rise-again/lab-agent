//对axios工具进行进一步封装

import axios, { HttpStatusCode } from 'axios'
import { getToken, logout } from './auth'
import { ElMessage } from 'element-plus'
import router from '@/router'

// console.log('VITE_API_BASE_URL:', import.meta.env.VITE_API_BASE_URL)

//设一个service用于处各种请求
const service = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 30000 //30s
})

//请求拦截其器的配置
service.interceptors.request.use(
  (config) => {
    const token = getToken()
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (err) => Promise.reject(err) //可能会有这个err，要把它抛出去
)

//返回拦截器的配置
service.interceptors.response.use(
  (res) => {
    //res.data表示实际请求数据，包括了http状态码、数据对象
    const data = res.data
    if (data.code !== 200) {
      ElMessage.error(data.message || '请求失败')
      if (data.code === 401) {
        logout()
        router.push('/login')
        return Promise.reject(data)
      }
    }
    return data
  },

  //处理请求失败的情况
  (err) => {
    if (err.response) {
      const HttpStatusCode = err.response.status
      if (HttpStatusCode === 401) {
        ElMessage.error('登陆状态已失效，请重新登录')
        logout()
        router.push('/login')
      } else {
        ElMessage.error(err.response.data.message || '请求失败')
      }
    } else {
      //后端没启动，网络异常
      ElMessage.error('网络异常，请检查后端服务')
    }
    return Promise.reject(err)
  }
)

//导出
export default service
