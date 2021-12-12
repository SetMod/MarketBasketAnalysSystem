import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'

export const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/transactions',
    name: 'Transactions',
    component: () => import('../views/TransactionsView.vue')
  },
  {
    path:'/analyse',
    name: 'Analyse',
    component:()=>import('../views/AnalyseView.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import( '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
