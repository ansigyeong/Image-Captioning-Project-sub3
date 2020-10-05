<template>
<div data-app="true" class="vue-tempalte">
  <div class = "App">
    <!-- <div class="vertical-center"> -->
      <!-- <div class="inner-block"> -->
        <router-view :key="$route.fullPath" ></router-view>
      <!-- </div> -->
    <!-- </div> -->
  </div>
</div>
</template>

<script scoped>
import http from '@/util/http-common.js'

export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false,
      errorMessages: null,

      drawer: null,
      dropDrawer: null,
    }
  },
  methods: {
      setCookie(token) {
        this.$cookies.set('auth-token', token)
        this.isLoggedIn = true
      },

      createattendance() {
          const config = {
              headers: {
                  'Authorization': `Token ${this.$cookies.get('auth-token')}`
              }
          }
          http.post('/accounts/attendance/', null, config)
            .then()
            .catch(err => {
                console.log(err)
            })
      },

      signup(signupData) {
        http.post('/rest-auth/signup/', signupData)
          .then(res => {
            this.setCookie(res.data.key)
            alert('회원가입 성공')
            this.$router.push({ name: 'Home' })
          })
          .catch(err => {
          alert('회원가입 실패')
          this.errorMessages = err.response.data})
      },

      login(loginData) {
        
        http.post('/rest-auth/login/', loginData)
          .then(res => {
            // console.log(res.data.key)
            // console.log(res.data)

            this.setCookie(res.data.key)

            this.createattendance()

            alert('로그인 성공')
            this.$router.push({ name: 'Home' })
          })
          .catch(err => {
            alert('로그인 실패')
            this.errorMessages = err.response.data})
      },

      logout() {
        const config = {
          headers: {
            'Authorization': `Token ${this.$cookies.get('auth-token')}`
          }
        }

        http.get('/rest-auth/logout/', null, config)
          // .then(() => {})
          .catch(err => console.log(err.response))
          .finally(() => {
            this.$cookies.remove('auth-token')
            this.isLoggedIn = false
            alert('로그아웃 성공')
            this.$router.push({ name: 'Home' })
          })
      },
      goHome() {
        this.$router.push('/')
      },
      goSignup() {
        this.$router.push('/accounts/signup')
      },
      goSignin() {
        this.$router.push('/accounts/login')
      },
      goPointList() {
            this.$router.push('/mypage/pointList')
      },
      goAttendance() {
          this.$router.push('/mypage/attendance')
      },
      goMyinfo() {
          this.$router.push('/mypage/myinfo')
      },
      goVocList() {
          this.$router.push('/mypage/voclist')
      },
      goWordbook() {
          this.$router.push('/english/wordbook')
      },
      goSpeaking() {
          this.$router.push('/english/speaking')
      },
      goNotice() {
          this.$router.push('/notice')
      },
      goListening() {
          this.$router.push('/english/listening')
      },
      goMyWordbook() {
          this.$router.push('/english/userwordbook')
      }
      
    },
    mounted() {
      // cookie 에 auth-token 이 존재하는가 체크
      this.isLoggedIn = this.$cookies.isKey('auth-token')
      // if (this.$cookies.isKey('auth-token')) {
      //   this.isLoggedIn = true
      // } else {
      //   this.isLoggedIn = false
      // }
    },
  }






