<template>
  <div class="bg1">
    <Navbar/>
    <div style="min-height: 100%;">
      <div class="bin"></div>

      <div style="text-align: center;"><h1>👩 Voice Of the Customer 👨</h1></div>
      <br>
      <br>
      <div class="container">
        <div style="text-align: right;"><v-btn @click='goCreateVoc'>글 쓰러 가기</v-btn></div>
        <br>
        <br>
        <div class="content-back">
          <div style="text-align: center;"> 
            <v-row>
                <v-col cols="3">번호</v-col>
                <v-col cols="6">제목</v-col>
                <v-col cols="3">답변</v-col>
            </v-row>
            <hr>
            <div v-for="suggestion in calData" :key="`suggestion_${suggestion.id}`">
                <v-row>
                    <v-col cols="3">{{ suggestion.id }}</v-col>
                    <v-col cols="6" @click="goDetail(suggestion.id)">{{ suggestion.title }}</v-col>
                    <v-col cols="3">{{ suggestion.finish }}</v-col>
                </v-row>
            </div>
          </div>
        </div>
        <div class="text-center">
          <v-pagination
            v-model="curPageNum"
            :length="numOfPages"
            circle
          ></v-pagination>
        </div>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
import http from '../util/http-common.js'
import Navbar from "../components/common/Navigation"
import Footer from "../components/common/footer"
import '@/assets/css/background1.css'

export default {
  name: 'vocList',
  components: {
    Navbar,
    Footer
  },
  data() {
    return {
      suggestions: [],
      dataPerPage: 6,
      curPageNum: 1,
    };
  },
  created() {
    this.fetchData()
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
        .catch(err => {
          console.log(err)})
    },
    goCreateVoc() {
      this.$router.push('/mypage/createvoc/')
    },
    goDetail(id) {
      this.$router.push('/mypage/vocdetail/' + id)
    }
  },
  computed: {
    startOffset() {
      return ((this.curPageNum - 1) * this.dataPerPage);
    },
    endOffset() {
      return (this.startOffset + this.dataPerPage);
    },
    numOfPages() {
      return Math.ceil(this.suggestions.length / this.dataPerPage);
    },
    calData() {
      return this.suggestions.slice(this.startOffset, this.endOffset);
    },
  },
};
</script>

<style scoped> /* pagination 스타일링 문제로 scoped 삭제 */
  .bin{
    height: 70px;
  }
  .content-back {
    background-color: rgb(255, 255, 255, 0.9);
    border-radius: 1rem;
  }
  @media(max-width: 480px){
    h1{
      font-size: 20px;
    }
  }
</style>
<style>
  .theme--light.v-pagination .v-pagination__item--active {
    color: black;
  }
</style>