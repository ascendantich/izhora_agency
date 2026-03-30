import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'

import Home from '../pages/Home.vue'
import About from '../pages/About.vue'
import Objects from '../pages/Objects.vue'
import House from '../pages/House.vue'
import Apartment from '../pages/Apartment.vue'
import Mortgage from '../pages/Mortgage.vue'
import Corporate from '../pages/Corporate.vue'
import Documents from '../pages/Documents.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/objects',
    name: 'objects',
    component: Objects
  },
  {
    path: '/house',
    name: 'house',
    component: House
  },
  {
    path: '/apartment',
    name: 'apartment',
    component: Apartment
  },
  {
    path: '/mortgage',
    name: 'mortgage',
    component: Mortgage
  },
  {
    path: '/corporate',
    name: 'corporate',
    component: Corporate
  },
  {
    path: '/documents',
    name: 'documents',
    component: Documents
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
