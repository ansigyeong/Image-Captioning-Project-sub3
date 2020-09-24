<template>
  <v-app id="app">

    <!-- Header & Nav 시작 -->
    <div class="HeaderNav">
        <div style="background: #536976; -webkit-linear-gradient(to right, #292E49, #536976); linear-gradient(to right, #292E49, #536976); height:50px;">
            <div style="float:left; margin-left:10px; margin-top:8px;">
                <div @click.stop="drawer = !drawer" style="cursor:pointer;">
                    <i class="fas fa-bars fa-2x"></i>
                </div>
            </div>
            <div style="float:right; margin-right:10px; margin-top:8px;">
                <v-menu bottom transition="slide-y-transition">
                    <template v-slot:activator="{ on, attrs }">
                        <div v-bind="attrs" v-on="on">
                            <i class="fas fa-user fa-2x"></i>
                        </div>
                    </template>
                    
                    <v-list v-if="!isLoggedIn">
                      <v-list-item @click="goSignup" style="margin-left:20px;">
                          <v-list-item-content>
                              <v-list-item-title>Sign Up</v-list-item-title>
                          </v-list-item-content>
                      </v-list-item>
                      <v-list-item @click="goSignin" style="margin-left:20px;">
                          <v-list-item-content>
                              <v-list-item-title>Sign In</v-list-item-title>
                          </v-list-item-content>
                      </v-list-item>
                    </v-list>

                    <v-list v-if="isLoggedIn">
                        <v-list-item @click.stop="dropDrawer = !dropDrawer">
                            <v-list-item-content>
                                <v-list-item-title>My Page</v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                        <v-list v-if="dropDrawer">
                            <v-list-item @click="goAttendance" style="margin-left:20px;">
                                <v-list-item-content>
                                    <v-list-item-title>Attendance</v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                            <v-list-item @click="goMyinfo" style="margin-left:20px;">
                                <v-list-item-content>
                                    <v-list-item-title>My Information</v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                            <v-list-item @click="goPointList" style="margin-left:20px;">
                                <v-list-item-content>
                                    <v-list-item-title>Points</v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                            <v-list-item @click="goVocList" style="margin-left:20px;">
                                <v-list-item-content>
                                    <v-list-item-title>Voice of Customer</v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                        </v-list>
                        <v-divider></v-divider>
                        <v-list-item to="/accounts/logout" @click.native="logout">
                            <v-list-item-content>
                                <v-list-item-title>Logout</v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                    </v-list>
                    </v-menu>
            </div>
        </div>

        <!-- 사이드바 항목은 목업 내용 그대로 넣었음 -->
        <!-- 간격, 크기 등 조절해야 함 -->
        <v-navigation-drawer v-model="drawer" absolute temporary>
            <v-list-item @click="goListening" style="margin-top:100px;">
                <v-list-item-icon>
                    <i class="fas fa-headphones-alt"></i>
                </v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title>Listening</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item @click="goSpeaking">
                <v-list-item-icon>
                    <i class="fas fa-volume-up"></i>
                </v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title>Speaking</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item @click="goWordbook">
                <v-list-item-icon>
                    <i class="fas fa-atlas"></i>
                </v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title>Wordbook</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-divider></v-divider>
            <v-list-item @click="goNotice">
                <v-list-item-icon>
                    <i class="fas fa-bullhorn"></i>
                </v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title>Notice</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-navigation-drawer>
    </div>
    <!-- Header & Nav 끝 -->

    <!-- <div id="nav">
      <router-link to="/">New Learn</router-link> |
      <router-link v-if="!isLoggedIn" :to="{ name: 'Login' }">Login</router-link> 
      <router-link v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</router-link>
      <router-link v-if="isLoggedIn" to="/accounts/logout" @click.native="logout" >Logout</router-link>
      <div>
        {{ errorMessages }}
      </div>
    </div> -->

    <main>
      <router-view @submit-login-data="login" @submit-signup-data="signup"/>
    </main>
  </v-app>
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
            console.log(res.data.key)
            console.log(res.data)
            this.setCookie(res.data.key)
            // this.$router.push({ name: 'Home' })
          })
          .catch(err => this.errorMessages = err.response.data)
      },

      logout() {
        const config = {
          headers: {
            'Authorization': `Token ${this.$cookies.get('auth-token')}`
          }
        }

        http.get(`/rest-auth/logout/`, null, config)
          // .then(() => {})
          .catch(err => console.log(err.response))
          .finally(() => {
            this.$cookies.remove('auth-token')
            this.isLoggedIn = false
            this.$router.push({ name: 'Home' })
          })
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
  html #app {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    min-height: 800px;
    background-size: 100% 100%;
    background: #536976;
    background: -webkit-linear-gradient(to right, #292E49, #536976);
    background: linear-gradient(to right, #292E49, #536976); 
  }
</style>
