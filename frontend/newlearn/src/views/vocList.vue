<template>
  <div class="container">
    <Navbar/>
    <div class="bin"></div>

    <div style="text-align: center;"><h1>👩 Voice Of the Customer 👨</h1></div>
    <br>
    <br>
    <div style="text-align: right;"><v-btn @click='goCreateVoc'>글 쓰러 가기</v-btn></div>
    <br>
    <br>
    <div style="text-align: center;"> 
      <v-row>
          <v-col cols="3">번호</v-col>
          <v-col cols="6">제목</v-col>
          <v-col cols="3">답변</v-col>
      </v-row>
      <hr>
      <div v-for="suggestion in suggestions" :key="`suggestion_${suggestion.id}`">
          <v-row>
              <v-col cols="3">{{ suggestion.id }}</v-col>
              <v-col cols="6" @click="goDetail(suggestion.id)">{{ suggestion.title }}</v-col>
              <v-col cols="3">{{ suggestion.finish }}</v-col>
          </v-row>
      </div>
    </div>
  </div>
</template>

<script>
import http from '../util/http-common.js'
import Navbar from "../components/common/Navigation"

export default {
  name: 'vocList',
  components: {
        Navbar,
  },
  data() {
    return {
      suggestions: []
    };
  },
  methods: {
    fetchData() {
      const config = {
                headers: {
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            }
      http.post("/community/suggestion/", null, config)
        .then(res => this.suggestions = res.data)
        .catch(err => console.error(err))
    },
    goCreateVoc() {
      this.$router.push('/mypage/createvoc/')
    },
    goDetail(id) {
      this.$router.push('/mypage/vocdetail/' + id)
    }
  },
  created() {
    this.fetchData()
  }
};
</script>

<style scoped>
    .bin{
        height: 70px;
    }
    @media(max-width: 480px){
        h1{
            font-size: 20px;
        }
    }
</style>