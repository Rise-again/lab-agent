//仅供组件setup函数使用

import { ref } from 'vue'
import { getUserInfo, setToken, setUserInfo } from './auth'

const userInfo = ref(getUserInfo()) //加上ref包装成响应式对象，可以随时更新最新的值

//提供一个hook，把工具方法封装在一起
export function useUser() {
  function saveLoginData(data) {
    setToken(data.token)
    setUserInfo(data.user)
    userInfo.value = data.user
  }

  function updateUser(user) {
    setUserInfo(user)
    userInfo.value = data.useUser
  }

  function reloadUser() {
    userInfo.value = getUserInfo()
  }

  return {
    userInfo,
    saveLoginData,
    updateUser,
    reloadUser
  }
}
