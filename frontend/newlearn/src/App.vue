<template>
  <v-app id="app">
    <Header/>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link v-if="!isLoggedIn" :to="{ name: 'Login' }">Login</router-link> | 
      <router-link v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</router-link>
      <router-link v-if="isLoggedIn" to="/accounts/logout" @click.native="logout" >Logout</router-link>
      <div>
        {{ errorMessages }}
      </div>
    </div>

    <main>
      <router-view @submit-login-data="login" @submit-signup-data="signup"/>
    </main>
  </v-app>
</template>

<script scoped>
import http from '@/util/http-common.js'
import Header from './components/Header.vue'

export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false,
      errorMessages: null,
    }
  },
  components : {
    Header,
  },
  methods: {
      setCookie(token) {
        this.$cookies.set('auth-token', token)
        this.isLoggedIn = true
      },

      signup(signupData) {
        http.post(`/rest-auth/signup/`, signupData)
          .then(res => {
            this.setCookie(res.data.key)
            this.$router.push({ name: 'Home' })
          })
          .catch(err => this.errorMessages = err.response.data)
      },

      login(loginData) {
        http.post(`/rest-auth/login/`, loginData)
          .then(res => {
            this.setCookie(res.data.key)
            this.$router.push({ name: 'Home' })
          })
          .catch(err => this.errorMessages = err.response.data)
      },

      logout() {
        const config = {
          headers: {
            'Authorization': `Token ${this.$cookies.get('auth-token')}`
          }
        }

        http.post(`/rest-auth/logout/`, null, config)
          // .then(() => {})
          .catch(err => console.log(err.response))
          .finally(() => {
            this.$cookies.remove('auth-token')
            this.isLoggedIn = false
            this.$router.push({ name: 'Home' })
          })
      },
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
</script>


<style scoped>

</style>
