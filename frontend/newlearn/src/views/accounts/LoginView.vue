<template>
 <!-- <section id="login" v-bind:class="isShake"> -->
 <div class="login" id="login">
   <form>
  <!-- <div class="info" v-bind:class="good">
   <p>{{ alert.message }}</p>
   <p v-show="login.login && login.password">{{ login.login}} / {{ login.password}}</p>
  </div> -->
    <Logo :component="component" />

      <input type="text" v-model="loginData.login" placeholder="Username" />
      <input type="password" v-model="loginData.password" placeholder="Password" />
      <button v-on:click="login">Log in</button>
    </form>
 

  <div class="add-option mt-4">
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
          <router-link to="/user/join/1" class="btn--text">가입하기</router-link>
        </div>
   </div>

</div>

</template>

<script>

import http from '@/util/http-common.js'
import Logo from "../../components/user/Logo.vue";

export default {
    name: 'LoginView',

    components:{
      Logo,
    },

    data() {
        return {
            loginData: {
                username: null,
                password: null,
            }
        }
    },
    methods: {
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
    }
}
</script>

<style scoped>
  html, body{
	width:100%;
	height:100%;
	margin:0px;
	font-family: 'Work Sans', sans-serif;
}

body{
  height:100%;
	background-size: cover;
	display: flex;
	flex-direction:column;
	justify-content:center;
	align-items:center;
	color:#0e678a;
}

section{
	background-color: #fff4f4;
	width:25%;
  height:100%;
	display:flex;
	flex-direction:column;
	margin-left:auto;
	margin-right:auto;
}
form{
	display:flex;
	flex-direction:column;
  height:100%;
	padding: 15px; 
}

h2{
	font-family: 'Archivo Black', sans-serif;
	color:#e0dada;
	margin-left:auto;
	margin-right:auto;
}

.info{
	width:100%;
	padding: 1em 5px;
	text-align:center;
	min-height:45px;
	display:flex;
	flex-direction:column;
	justify-content:center;
	align-items:center;
}

.info p{
	margin:auto;
	padding:5px;
}
.info.good{
	border:1px solid #416d50;
	background-color: #47cf73;
	color:#416d50;
}

input{
	height:35px;
	padding: 5px 5px;
	margin: 10px 0px;
	background-color:#e0dada;
	border:none;
}

button{
	height:40px;
	padding: 5px 5px;
	margin: 10px 0px;
	font-weight:bold;
	background-color:#be5256;
	border:none;
	color:#e0dada;
	cursor:pointer;
	font-size:16px;
}

button:hover{
	background-color:#711f1b;
}

@-webkit-keyframes shake{
    from, to{
      -webkit-transform: translate3d(0, 0, 0);
      transform:translate3d(0,0,0);
    }
    10%,30%,50%,70%,90%{
      -webkit-transform: translate3d(-10px, 0, 0);
      transform:translate3d(-10px,0,0);
    }
    20%,40%,60%,80%{
		-webkit-transform: translate3d(10px, 0, 0);
		transform:translate(10px,0,0);
	}
}

.shake{
	animation-name: shake;
	animation-duration:1s;
	/*animation-fill-mode: both;*/
}

@media screen and (max-width: 780px) {
	section{
		width:90%;
	}
}
</style>
