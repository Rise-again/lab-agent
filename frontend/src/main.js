import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus' // 引入 Element Plus
import 'element-plus/dist/index.css' // 引入 Element Plus 样式
import zhCn from 'element-plus/es/locale/lang/zh-cn' // 引入中文语言包
import * as ElementPlusIconsVue from '@element-plus/icons-vue' // 引入 Element Plus 图标组件
import '@/assets/css/global.css' // 引入全局样式

const app = createApp(App)

app.use(router)

// 使用 Element Plus，并设置语言为中文
app.use(ElementPlus, {
  locale: zhCn
})

// 注册 Element Plus 图标组件
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.mount('#app')
