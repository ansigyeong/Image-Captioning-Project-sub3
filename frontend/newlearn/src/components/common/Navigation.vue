<template>
  <div class="fixed-top">

    <!-- Header & Nav 시작 -->
    <div class="Navi">
            <div class="draw">
                <div @click.stop="drawer = !drawer" style="cursor:pointer;">
                    <i class="fas fa-bars fa-2x"></i>
                </div>
            </div>

            <div class="user">
                
                <v-menu bottom transition="slide-y-transition">
                    <template v-slot:activator="{ on, attrs }">
                        <div v-bind="attrs" v-on="on">
                            <i class="fas fa-user fa-2x"></i>
                        </div>
                    </template>
                    
                    <!-- <v-list v-if="!isLoggedIn">
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
                    </v-list> -->

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
    

        <!-- 사이드바 항목은 목업 내용 그대로 넣었음 -->
        <!-- 간격, 크기 등 조절해야 함 -->

        <v-navigation-drawer v-if="isLoggedIn" v-model="drawer" absolute temporary>
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

    <!-- <router-view @submit-login-data="login" @submit-signup-data="signup"/> -->
  </div>
</template>

<script scoped>
import http from '@/util/http-common.js'

export default {
  name: 'NavBar',
  data() {
    return {
      isLoggedIn: false,
      errorMessages: null,
      drawer: null,
      dropDrawer: null,
    }
  },
  methods: {

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
    //   goSignup() {
    //     this.$router.push('/accounts/signup')
    //   },
    //   goSignin() {
    //     this.$router.push('/accounts/login')
    //   },
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
  .Navi{
    background-color: #95bfd3;
    height: 50px;
   }

   .draw{
       float:left; 
       margin: 8px 0px 0px 10px; 
   }  

   .user{
       float:right; 
       margin: 8px 10px 0px 0px;
   }
</style>
