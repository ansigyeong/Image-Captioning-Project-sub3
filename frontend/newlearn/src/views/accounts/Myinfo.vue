<template>
  <v-app>
    <div class="container">
      <!-- 로고 -->
      <div style="text-align:center;"><h1>🏡 My Information 🏡</h1></div>
      <br>
      <br>

      <!-- 1. 프로필 카드 -->
      <v-card class="mx-auto" max-width="434" tile>
        <v-img height="100%" src="@/assets/profile.jpg">
          <v-row align="end" class="fill-height">
            <v-col align-self="start" class="pa-0" cols="12">
              <!-- <v-avatar class="profile" color="grey" size="164" tile>
                <v-img src="@/assets/profile.jpg"></v-img>
              </v-avatar> -->
            </v-col>
            <v-col class="py-0">
              <v-list-item color="rgba(0, 0, 0, .4)" dark>
                <v-list-item-content>
                  <!-- <v-list-item-title class="title">{{ }}</v-list-item-title> -->
                  <v-list-item-subtitle>Network Engineer</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-col>
          </v-row>
        </v-img>
      </v-card>

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
          <v-btn class="mr-4" @click="submit">Save Profile</v-btn>
          <v-btn @click="clear">Delete Account</v-btn>
        </div>
      </form>
    </div>
  </v-app>
</template>

<script>
  import http from '../../util/http-common.js'
  import { validationMixin } from 'vuelidate'
  import { required, maxLength } from 'vuelidate/lib/validators'

  export default {
    name: 'Myinfo',
    components: {
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
        const dummy = {
          'dummy' : 'dummy',
        }
        http.post(`accounts/userwithdraw/`, dummy, config)
        .then(() => {
          console.log('회원탈퇴')
          this.$router.push('/')
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
</style>