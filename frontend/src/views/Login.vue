<template>
  <div class="login-container">
    <div class="login-box">
      <h1 style="font-size: 28px">实验室预约系统</h1>
      <div style="margin-top: 5px; margin-bottom: 30px">基于Agent智能预约系统</div>

      <el-form ref="formRef" :rules="rules" :model="form" label-width="0px" style="max-width: 100%">
        <el-form-item prop="username">
          <el-input
            size="large"
            v-model="form.username"
            placeholder="请输入账号"
            :prefix-icon="User"
          />
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            type="password"
            size="large"
            v-model="form.password"
            placeholder="请输入密码"
            :prefix-icon="Lock"
            show-password
          />
        </el-form-item>
        <div>
          <el-button
            type="primary"
            size="large"
            style="width: 100%"
            @click="handleLogin"
            :loading="loadingValue"
          >
            登 录
          </el-button>
          <div style="text-align: right; margin-top: 20px">
            没有账号？请
            <router-link style="color: var(--el-color-primary)" to="/register">注册</router-link>
          </div>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { User, Lock } from '@element-plus/icons-vue'
import { loginApi } from '@/api/auth'
import { useUser } from '@/utils/user' //应用于保存登录信息
import { ElMessage } from 'element-plus'
import router from '@/router'
const { saveLoginData } = useUser()

//登录表单数据
const formRef = ref()

const form = reactive({
  username: '',
  password: ''
})

const loadingValue = ref(false)

//登录表单校验规则
const rules = {
  username: [{ required: true, message: '请输入账号', trigger: 'blur' }],
  password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
}

//登录
const handleLogin = async () => {
  //表单验证，登录表单填完并验证通过才会向后端发起请求
  const valid = await formRef.value.validate().catch(() => false)
  if (!valid) {
    return
  }

  loadingValue.value = true

  //之前的写法可能会因网络后端抖动卡在loading状态，现在更新写法
  try {
    const res = await loginApi(form)

    // console.log(res)
    if (res.code === 200) {
      saveLoginData(res.data) //保存登录信息
      ElMessage.success('登录成功')
      await router.push('/manager/home')
      //不用写否则，在request里已经写过了
    }
  } finally {
    loadingValue.value = false //有了结果就设false，不然会一直转圈
  }
}
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-box {
  width: 380px;
  border-radius: 8px;
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
  padding: 30px;
  text-align: center;
  background-color: withite;
}
</style>
