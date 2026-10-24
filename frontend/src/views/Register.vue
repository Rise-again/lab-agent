<template>
  <div class="register-container">
    <div class="register-box">
      <h1 style="font-size: 24px; margin-bottom: 30px">欢迎注册实验室预约系统</h1>

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
        <el-form-item prop="confirmpassword">
          <el-input
            type="password"
            size="large"
            v-model="form.confirmpassword"
            placeholder="请确认密码"
            :prefix-icon="Lock"
            show-password
          />
        </el-form-item>
        <div>
          <el-button
            type="primary"
            size="large"
            :loading="loadingValue"
            style="width: 100%"
            @click="register"
            >注 册</el-button
          >
          <div style="text-align: right; margin-top: 20px">
            已有账号？请
            <router-link style="color: var(--el-color-primary)" to="/login">登录</router-link>
          </div>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { User, Lock } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import { registerApi } from '@/api/auth'
// import { saveLoginData } from '@/utils/auth'
import router from '@/router'

const form = reactive({
  username: '',
  password: '',
  confirmpassword: ''
})

const loadingValue = ref(false)

const formRef = ref()

//注册表单验证规则，来源于element-plus的表单验证规则
const validatePass = (rule, value, callback) => {
  if (value === '') {
    callback(new Error('请输入密码'))
  } else {
    if (value !== form.password) {
      callback(new Error('两次输入密码不一致'))
    } else {
      callback()
    }
  }
}

//表单红色提示
const rules = {
  username: [{ required: true, message: '请输入账号', trigger: 'blur' }],
  password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
  confirmpassword: [
    { required: true, message: '请确认密码', trigger: 'blur' },
    { validator: validatePass, trigger: 'blur' }
  ]
}

//注册函数，点击注册按钮时触发
const register = async () => {
  //表单验证，登录表单填完并验证通过才会向后端发起请求
  const valid = await formRef.value.validate().catch(() => false)
  if (!valid) {
    return
  }

  loadingValue.value = true

  //之前的写法可能会因网络后端抖动卡在loading状态，现在更新写法
  try {
    const res = await registerApi(form)

    // console.log(res)
    if (res.code === 200) {
      ElMessage.success('注册成功')
      await router.push('/login') //注册成功后跳转到登录页面
      //不用写否则，在request里已经写过了
    }
  } finally {
    loadingValue.value = false //有了结果就设false，不然会一直转圈
  } //res.code!===200的情况不用写，因为在request里已经写过了
}
</script>

<style scoped>
.register-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.register-box {
  width: 380px;
  border-radius: 8px;
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
  padding: 30px;
  text-align: center;
  background-color: withite;
}
</style>
