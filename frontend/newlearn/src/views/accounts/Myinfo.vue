<template>
  <v-app>
    <div class="bg1">
      <Navbar/>
      <div style="min-height: 100%;">
      <div class="bin"></div>

      <!-- 로고 -->
      <div style="text-align:center;"><h1>🏡 My Information 🏡</h1></div>
      <br>
      <br>

      <!-- 1. 프로필 카드 -->

      <br>
      <br>

      <!-- 2. 회원 정보 수정(닉네임, 비밀번호, 비밀번호 확인) & 회원탈퇴  -->

      <!-- 이름 -->
      <form class="user_info">
        <div>
          <p>
            {{ this.name }}
          </p>
        </div>

        <!-- 메일 -->
        <v-text-field
            v-model="email"
            :rules="[rules.required, rules.email]"
            label="E-mail"
          ></v-text-field>

        <!-- 기존 비밀번호 입력 -->
        <!-- <v-col cols="12" sm="6"> -->
          <v-text-field
            :append-icon="show4 ? 'mdi-eye' : 'mdi-eye-off'"
            v-model="pastpassword"
            :rules="[rules.required]"
            :type="show4 ? 'text' : 'password'"
            name="input-10-2"
            label="기존 비밀번호를 입력해 주세요"
            hint="At least 8 characters"
            :value="this.pastpassword"
            @click:append="show4 = !show4"
          ></v-text-field>
        <!-- </v-col> -->

        <!-- <v-col cols="12" sm="6"> -->
            <v-text-field
              :append-icon="show4 ? 'mdi-eye' : 'mdi-eye-off'"
              v-model="password"
              :rules="[rules.required, rules.min]"
              :type="show4 ? 'text' : 'password'"
              name="input-10-2"
              label="Error"
              hint="At least 8 characters"
              :value="this.password"
              error
              @click:append="show4 = !show4"
            ></v-text-field>
          <!-- </v-col> -->

          <!-- 비밀번호 확인 -->
          <!-- <v-col cols="12" sm="6"> -->
            <v-text-field
              :append-icon="show4 ? 'mdi-eye' : 'mdi-eye-off'"
              v-model="repeatPassword"
              :rules="confirmPasswordRules.concat(passwordConfirmationRule)"
              :type="show4 ? 'text' : 'password'"
              name="input-10-2"
              label="Error"
              hint="At least 8 characters"
              :value="this.repeatPassword"
              error
              @click:append="show4 = !show4"
            ></v-text-field>
          <!-- </v-col> -->

          <br>
          <br>
          <div class="button">
            <v-btn @click="submit">Save Profile</v-btn>
            <v-btn @click="clear">Delete Account</v-btn>
          </div>
        </form>
      </div>
      <Footer/>
    </div>
  </v-app>
</template>

<script>
  import http from '../../util/http-common.js'
  import { validationMixin } from 'vuelidate'
  import { required, maxLength } from 'vuelidate/lib/validators'
  import Navbar from "../../components/common/Navigation"
  import Footer from "../../components/common/footer"
  import '@/assets/css/background1.css'

  export default {
    name: 'Myinfo',
    components: {
      Navbar,
      Footer
    },
    data() {
      return {
        name: '',
        email: '',
        show4: false,
        pastpassword: '',
        password: '',
        repeatPassword: '',
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
          email: value => {
            const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            return pattern.test(value) || 'Invalid e-mail.'
          },
        },
        confirmPasswordRules: [v => !!v || "Required."],
      }
    },
    mixins: [validationMixin],
    validations: {
      name: { required, maxLength: maxLength(10) },
    },
    computed: {
      nameErrors () {
        const errors = []
        if (!this.$v.name.$dirty) return errors
        !this.$v.name.maxLength && errors.push('Name must be at most 10 characters long')
        !this.$v.name.required && errors.push('Name is required.')
        return errors
      },
      passwordConfirmationRule() {
        return () =>
          this.password === this.repeatPassword || "password you entered don't match";
      }
    },
    created() {
      this.getInfo()
    },
    methods: {
      submit () {
        const config = {
            headers: {
                Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
        }
        const passdata = {
          'old_password': this.pastpassword,
          'new_password1': this.password,
          'new_password2': this.repeatPassword
        }
        http.post(`rest-auth/password/change/`, passdata, config)
        .then(() => {
          this.$router.push('/')
          // console.log(res)
          // console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      },
      clear () {
        const config = {
            headers: {
                Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
        }
        http.post(`accounts/userwithdraw/`, null, config)
        .then(() => {
          console.log('회원탈퇴')
          this.$cookies.remove('auth-token')
          this.$router.push({ name: 'Home' })
        })
        .catch((err) => {
          console.log(err)
        })
      },
      getInfo() {
        const config = {
            headers: {
                Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
        }
        http.get(`/rest-auth/user/`, config)
        .then(res => {
          this.name = res.data.username
          this.email = res.data.email
        })
      },
    },
  }
</script>

<style scoped>
  /* form {
    max-width: 50%;
  } */
  .bin{
        height: 70px;
    }
  .user_info {
    max-width: 50%;
    margin: auto;
  }
  .v-application .error {
    background-color: rgb(0, 0, 0, 0) !important;
    border-color: rgb(0, 0, 0, 0) !important;
  }
  .button {
    text-align: center !important;
    justify-content: center !important;
  }  
  @media(max-width: 480px){
        h1{
          font-size: 30px;
        }
        .bin{
          height: 70px;
        }
        .user_info {
          max-width: 90%;
          margin: auto;
        }
        .v-application .error {
          background-color: rgb(0, 0, 0, 0) !important;
          border-color: rgb(0, 0, 0, 0) !important;
        }
        .button {
          font-size: 15px;
        }  
    }
</style>