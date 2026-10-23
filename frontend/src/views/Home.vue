<template>
  <div>欢迎您：{{ userInfo?.name }}</div>
  <!-- 加上?方式没有名字为None时报错 -->
</template>
<script setup>
import { useUser } from '@/utils/user'
const { userInfo } = useUser() //userInfo是一个全局响应式对象，里面有username和token
</script>
