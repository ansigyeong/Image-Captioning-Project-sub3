import Vue from 'vue'
import VueRouter from 'vue-router'
//import Home from '../views/Home.vue'

import SignupView from '../views/accounts/SignupView.vue'
import LoginView from '../views/accounts/LoginView.vue'
import Myinfo from '../views/accounts/Myinfo.vue'

import PointList from '../views/PointList.vue'
import Attendance from '../views/Attendance.vue'

import vocList from '../views/vocList.vue'
import createVoc from '../views/createVoc.vue'
import vocDetail from '../views/vocDetail.vue'
import createVocAnswer from '../views/createVocAnswer.vue'
import vocAnswerDetail from '../views/vocAnswerDetail.vue'

import noticeList from '../views/noticeList.vue'
import createNotice from '../views/createNotice.vue'
import noticeDetail from '../views/noticeDetail.vue'

import Wordbook from '../views/Wordbook.vue'
import Speaking from '../views/Speaking.vue'
import Listening from '../views/Listening.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView,
  },
  // {
  //   path: '/accounts/login',
  //   name: 'Login',
  //   component: LoginView,
  // },
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
    path: '/mypage/voclist',
    name: 'vocList',
    component: vocList,
  },
  {
    path: '/mypage/createvoc',
    name: 'createVoc',
    component: createVoc,
  },
  {
    path: '/mypage/vocdetail/:suggestion_pk',
    name: 'vocDetail',
    component: vocDetail,
  },
  {
    path: '/mypage/createvocanswer',
    name: 'createVocAnswer',
    component: createVocAnswer,
  },
  {
    path: '/mypage/vocAnswerDetail',
    name: 'vocAnswerDetail',
    component: vocAnswerDetail,
  },
  {
    path: '/notice/createnotice',
    name: 'createNotice',
    component: createNotice,
  },
  {
    path: '/notice',
    name: 'noticeList',
    component: noticeList,
  },
  {
    path: '/notice/noticedetail/:notice_pk',
    name: 'noticeDetail',
    component: noticeDetail,
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
  {
    path: '/english/listening',
    name: 'Listening',
    component: Listening,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const publicPages = ['Login', 'Signup', 'Home', 'List', 'Pointlist', 'Attendance', 'Wordbook', 'Speaking', 'Listening']  // Login 안해도 됨
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
