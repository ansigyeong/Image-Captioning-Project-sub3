import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import SignupView from '../views/accounts/SignupView.vue'
import LoginView from '../views/accounts/LoginView.vue'
import Myinfo from '../views/accounts/Myinfo.vue'

import PointList from '../views/PointList.vue'
import Attendance from '../views/Attendance.vue'
import QandA from '../views/QandA.vue'

import Wordbook from '../views/Wordbook.vue'
import Speaking from '../views/Speaking.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/mypage/myinfo',
    name: 'Myinfo',
    component: Myinfo,
  },
  {
    path: '/mypage/pointList',
    name: 'Pointlist',
    component: PointList,
  },
  {
    path: '/mypage/attendance',
    name: 'Attendance',
    component: Attendance,
  },
  {
    path: '/mypage/qanda',
    name: 'QandA',
    component: QandA,
  },
  {
    path: '/english/wordbook',
    name: 'Wordbook',
    component: Wordbook,
  },
  {
    path: '/english/speaking',
    name: 'Speaking',
    component: Speaking,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const publicPages = ['Login', 'Signup', 'Home', 'List', 'Pointlist', 'Attendance', 'Wordbook', 'Speaking']  // Login 안해도 됨
  const authPages = ['Login', 'Signup']  // Login 되어있으면 안됨
  
  const authRequired = !publicPages.includes(to.name)  // 로그인 해야 함
  const unauthRequired = authPages.includes(to.name)  // 로그인 해서는 안됨
  const isLoggedIn = !!Vue.$cookies.isKey('auth-token')

  if(unauthRequired && isLoggedIn) {
    next('/')
  }
  authRequired && !isLoggedIn ? next({ name: 'Login'}) : next()
})

export default router
