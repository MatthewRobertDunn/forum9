import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import QuestionsView from '../views/QuestionsView.vue'
import QuestionView from '@/views/QuestionView.vue'
import AskView from '@/views/AskView.vue'
const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: QuestionsView,
    },
    {
      path: '/question/:id',
      name: 'question',
      component: QuestionView,
    },
    {
      path: '/ask/',
      name: 'ask',
      component: AskView,
    }
  ],
})

export default router
