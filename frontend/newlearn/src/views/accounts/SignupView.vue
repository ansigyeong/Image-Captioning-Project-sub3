<template>
  <div class="signUp">
    <div style="text-align: center; vertical-align: middle;">
      <a href="/"><h1>New Learn</h1></a>
    </div>
    <br>
    <br>
    <br>
    <div class="signup-box">
      <h2>Signup</h2>
      <form onsubmit="return false;">
        <div class="user-box">
          <input v-model="signupData.username" id="username" type="text">
          <label for="username"><p style="color: white;">ID</p></label>
        </div>
        <div class="user-box">
          <input v-model="signupData.email" id="email" type="text">
          <label for="email"><p style="color: white;">E-mail</p></label>
        </div>
        <div class="user-box">
          <input v-model="signupData.password1" id="password1" type="password">
          <label for="password1"><p style="color: white;">Password</p></label>
        </div>
        <div class="user-box">
          <input v-model="signupData.password2" id="password2" type="password">
          <label for="password2"><p style="color: white;">Repeat Password</p></label>
        </div>
        <div style="text-align: center;">
          <button @click="signup" style="color: white;">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            Submit
          </button>
        </div>
      </form>
    </div>
  </div>

</template>

<script>
import http from '@/util/http-common.js'
import '@/assets/css/main.css'

export default {
    name: 'SignupView',
    data() {
        return {
            signupData: {
                username: null,
                email: null,
                password1: null,
                password2: null,
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

     signup() {
        http.post('/rest-auth/signup/', this.signupData)
          .then(res => {
            this.setCookie(res.data.key)
            this.createattendance()
            alert('회원가입 성공')
            this.$router.push({ name: 'Home' })
          })
          .catch(err => {
          alert('회원가입 실패')
          this.errorMessages = err.response.data})
      },

    }
}
</script>

<style scoped>
  h1{
    font-size: 100px;
    color: white;
  }
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
    margin-top: 40px;
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
  
  @media(max-width: 480px){
   h1{
     font-size:70px;
   }
  }
</style>
