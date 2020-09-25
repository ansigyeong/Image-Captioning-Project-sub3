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
        <v-text-field
          v-model="name"
          :error-messages="nameErrors"
          :counter="10"
          label="ID"
          required
          @input="$v.name.$touch()"
          @blur="$v.name.$touch()"
        ></v-text-field>

        <!-- 메일 -->
        <v-text-field
            v-model="email"
            :rules="[rules.required, rules.email]"
            label="E-mail"
          ></v-text-field>

        <!-- 비밀번호 -->
        <!-- <v-col cols="12" sm="6"> -->
          <v-text-field
            :append-icon="show4 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.emailMatch]"
            :type="show4 ? 'text' : 'password'"
            name="input-10-2"
            label="Error"
            hint="At least 8 characters"
            value="Pa"
            error
            @click:append="show4 = !show4"
          ></v-text-field>
        <!-- </v-col> -->

        <!-- 비밀번호 확인 -->
        <!-- <v-col cols="12" sm="6"> -->
          <v-text-field
            :append-icon="show4 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.emailMatch]"
            :type="show4 ? 'text' : 'password'"
            name="input-10-2"
            label="Error"
            hint="At least 8 characters"
            value="Pa"
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
  import { required, maxLength, sameAs, minLength } from 'vuelidate/lib/validators'

  export default {
    name: 'Myinfo',
    components: {
    },
    data() {
      return {
        name: '',
        email: '',
        show4: false,
        password: 'Password',
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
          emailMatch: () => ('The email and password you entered don\'t match'),
          email: value => {
            const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            return pattern.test(value) || 'Invalid e-mail.'
          },
        },
      }
    },
    mixins: [validationMixin],
    validations: {
      name: { required, maxLength: maxLength(10) },
      password: {
        required,
        minLength: minLength(6)
      },
      repeatPassword: {
        sameAsPassword: sameAs('password')
      },
    },
    computed: {
      nameErrors () {
        const errors = []
        if (!this.$v.name.$dirty) return errors
        !this.$v.name.maxLength && errors.push('Name must be at most 10 characters long')
        !this.$v.name.required && errors.push('Name is required.')
        return errors
      },
    },
    created() {
      this.getInfo()
    },
    methods: {
      submit () {
        this.$v.$touch()
      },
      clear () {
        this.$v.$reset()
        this.name = ''
        this.password = ''
        this.select = null
        this.checkbox = false
      },
      getInfo() {
        http.post(`/rest-auth/password/change/`)
        .then(res => {
          console.log('비밀번호를 변경하자!')
          console.log(res.data)
          this.password = res.data.password
          this.repeatPassword = res.data.password
          // this.username = res.User.username
          // this.password = res.data.password
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