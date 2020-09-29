<template>
  <div class="container">
    <div style="text-align: center;"><h1>👩 Voice Of the Customer 👨</h1></div>
    <br>
    <br>

    <!-- 1. title & etc -->
    <div class="title">
      <h1>{{ this.suggestion.title }}</h1>
    </div>
    <div style="text-align: right;">
      <p>{{ this.suggestion.created_at }}</p>
    </div>
    <div style="text-align: right;">
      <v-btn @click="goEdit">EDIT</v-btn>
      <v-btn @click="goDelete">DELETE</v-btn>
    </div>

    <hr>

    <!-- 2. content -->
    <div v-html="this.suggestion.content" style="margin:20px" class="contentbox"></div>
    <!-- <div class="content">
      <h3>{{ this.suggestion.content }}</h3>
    </div> -->
  </div>
</template>

<script>
import http from '../util/http-common.js'

export default {
  name: 'vocDetail',
  data() {
    return {
      suggestion: [],
    }
  },
  created() {
    this.suggestion_pk = this.$route.params.suggestion_pk
    this.fetchDetail()
  },
  methods: {
    fetchDetail() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      http.get("/community/suggestion/" + this.suggestion_pk, config)
      .then((res) => {
        this.suggestion = res.data
      })
      .catch(err => console.log(err))
    },
    goDelete() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      http.delete(`/community/suggestion/` + this.suggestion_pk + `/delete/`, config)
      .then((res) => {
        console.log(res)
        alert('성공적으로 삭제되었습니다.')
        this.$router.go(-1)
        // this.$router.push({ name: 'vocList' })
      })
      .catch((err) => {
        console.log(err)
        alert('성공적으로 삭제되었습니다.') // 여기서 삭제됨, 에러 해결하기
        this.$router.go(-1)
        // this.$router.push({name: 'vocList'})
      })
    },
    goEdit() {
      // const config = {
      //   headers: {
      //     Authorization: `Token ${this.$cookies.get('auth-token')}`
      //   }
      // }
      // const editinfo = {
      //   title: this.suggestion.title,
      //   content: this.suggestion.content,
      // }
      // http.post(`/community/suggestion/` + `${this.suggestion_pk}` + `/update/`, editinfo, config)
      // .then(() => {
      //   this.$router.push('/mypage/editvoc/' + this.suggestion_pk)
      // })
      this.$router.push('/mypage/editvoc/' + this.suggestion_pk)
    },
  },
}
</script>

<style scoped>
  .title {
    margin: 20px;
  }
  .content {
    margin: 20px;
  }
  .v-btn {
    margin: 5px;
  }
</style>