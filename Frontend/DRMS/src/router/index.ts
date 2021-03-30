import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import Tab3 from '../views/Tab3.vue'
import Tab2 from '../views/Tab2.vue'
import Tab1 from '../views/Tab1.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Tab3,
  },
  {
    path: '/Tutorial',
    name: 'Tutorial',
    component: Tab2,
  },
  {
    path: '/Prediction',
    name: 'Prediction',
    component: Tab1,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
