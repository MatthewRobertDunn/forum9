import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import SpinnerPlugin from './plugins/spinner'

const app = createApp(App)

app.use(router)
app.use(SpinnerPlugin)
app.mount('#app')