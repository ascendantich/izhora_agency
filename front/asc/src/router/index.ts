import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'

import Home from '../pages/Home.vue'
import About from '../pages/About.vue'  // импортируем About

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',           // URL страницы
    name: 'about',            // имя маршрута
    component: About          // компонент страницы
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router