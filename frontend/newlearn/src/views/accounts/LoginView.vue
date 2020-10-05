<template>
    <div class="login">
       
       <div style="text-align: center; vertical-align: middle;">
            <a href="/"> <h1 style="font-size: 100px; color: white;"> New Learn </h1></a>
        </div>

         <br>
         <br>
         <br>

        <div class="signup-box">
        <h2>Login</h2> 
        <form onsubmit="return false;">
 
  
          <div class = "user-box">
            <input v-model="loginData.username" id="username" type="text"/>
            <label for="username"><p style="color: white;">id</p></label>
          </div>
      
          <div class="user-box">
            <input v-model="loginData.password" id="password" type="password"/>
            <label for="password"><p style="color: white;">password</p></label>
          </div>
      
          <button @click="login()" class="btn btn-dark btn-lg btn-block">Log in</button>
    
          <span class="forgot-password" style="float:left;">아직 회원이 아니신가요?</span>

          <span class="btn-signup"><router-link to="/accounts/signup" class="btn--text">가입하기</router-link></span>
        
          
          
   <!-- <div class="add-option mt-4">
        <div class="text">
          <p>혹시</p>
          <div class="bar"></div>
        </div>
        <div class="wrap">
          <p>비밀번호를 잊으셨나요?</p>
          <router-link to="/find/password" class="btn--text" style="float-right:true;">비밀번호 찾기</router-link>
        </div>
        <div class="wrap">
          <p>아직 회원이 아니신가요?</p>
          <router-link to="/accounts/signup" class="btn--text">가입하기</router-link>
        </div>
   </div>  -->

                  </form>  
              </div>
            </div>
</template>


<script>

import http from '../../util/http-common.js'
// import Logo from "../../components/user/Logo.vue";
import '@/assets/css/main.css'

export default {
    name: 'LoginView',

    // components:{
    //   Logo,
    // },

    data() {
        return {
            loginData: {
                username: null,
                password: null,
            }
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

      login() {
        http.post('/rest-auth/login/', this.loginData)
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
            console.log(err)
          })
      },
    }
}
</script>

<style scoped>
  html {
    height: 100%;
  }

  body {
    margin: 0;
    padding: 0;
    font-family: sans-serif;
    background: linear-gradient(#141e30, #243b55);
  }

  .signup-box {
    position: absolute;
    top: 60%;
    left: 50%;
    width: 400px;
    padding: 40px;
    transform: translate(-50%, -50%);
    background: rgba(0, 0, 0, 0.5);
    box-sizing: border-box;
    box-shadow: 0 15px 25px rgba(0, 0, 0, 0.6);
    border-radius: 10px;
  }

  .signup-box h2 {
    margin: 0 0 30px;
    padding: 0;
    color: #fff;
    text-align: center;
  }

  .signup-box .user-box {
    position: relative;
  }

  .signup-box .user-box input {
    width: 100%;
    padding: 10px 0;
    font-size: 16px;
    color: #fff;
    margin-bottom: 30px;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    background: transparent;
  }
  .signup-box .user-box label {
    position: absolute;
    top: 0;
    left: 0;
    padding: 10px 0;
    font-size: 16px;
    color: #fff;
    pointer-events: none;
    transition: 0.5s;
  }

  .signup-box .user-box input:focus ~ label,
  .signup-box .user-box input:valid ~ label {
    top: -30px;
    left: 0;
    color: #000;
    font-size: 12px;
  }

  .signup-box form a {
    position: relative;
    display: inline-block;
    padding: 10px 20px;
    color: #03e9f4;
    font-size: 16px;
    text-decoration: none;
    text-transform: uppercase;
    overflow: hidden;
    transition: 0.5s;
    margin-left: 45px;
    margin-top: 7px;
    letter-spacing: 4px;
  }

  .signup-box a:hover {
    background: #03e9f4;
    color: #fff;
    border-radius: 5px;
    box-shadow: 0 0 5px #03e9f4, 0 0 25px #03e9f4, 0 0 50px #03e9f4,
      0 0 100px #03e9f4;
  }

  .signup-box a span {
    position: absolute;
    display: block;
  }

  .signup-box a span:nth-child(1) {
    top: 0;
    left: -100%;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #03e9f4);
    animation: btn-anim1 1s linear infinite;
  }

  @keyframes btn-anim1 {
    0% {
      left: -100%;
    }
    50%,
    100% {
      left: 100%;
    }
  }

  .signup-box a span:nth-child(2) {
    top: -100%;
    right: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(180deg, transparent, #03e9f4);
    animation: btn-anim2 1s linear infinite;
    animation-delay: 0.25s;
  }

  @keyframes btn-anim2 {
    0% {
      top: -100%;
    }
    50%,
    100% {
      top: 100%;
    }
  }

  .signup-box a span:nth-child(3) {
    bottom: 0;
    right: -100%;
    width: 100%;
    height: 2px;
    background: linear-gradient(270deg, transparent, #03e9f4);
    animation: btn-anim3 1s linear infinite;
    animation-delay: 0.5s;
  }

  @keyframes btn-anim3 {
    0% {
      right: -100%;
    }
    50%,
    100% {
      right: 100%;
    }
  }

  .signup-box a span:nth-child(4) {
    bottom: -100%;
    left: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(360deg, transparent, #03e9f4);
    animation: btn-anim4 1s linear infinite;
    animation-delay: 0.75s;
  }

  @keyframes btn-anim4 {
    0% {
      bottom: -100%;
    }
    50%,
    100% {
      bottom: 100%;
    }
  }
</style>