<template>
  <div class="container">
    <div style="text-align: center;"><h1>🔉 Notice 🔉</h1></div>
    <br>
    <br>
    <div style="text-align: right;"><v-btn @click='goCreateNotice'>공지사항 작성(관리자)</v-btn></div>
    <br>
    <br>
    <div style="text-align: center;"> 
      <v-row>
          <v-col cols="3">번호</v-col>
          <v-col cols="6">제목</v-col>
          <v-col cols="3">작성 일자</v-col>
      </v-row>
      <hr>
      <div v-for="notice in notices" :key="`notice_${notice.id}`">
          <v-row>
              <v-col cols="3">{{ notice.id }}</v-col>
              <v-col cols="6" @click="goDetail(notice.id)">{{ notice.title }}</v-col>
              <v-col cols="3">{{ notice.created_at }}</v-col>
          </v-row>
      </div>
    </div>
  </div>
</template>

<script>
import http from '../util/http-common.js'

export default {
  name: 'noticeList',
  data() {
    return {
      notices: []
    };
  },
  methods: {
    fetchData() {
      http.get("/community/notice/")
        .then(res => this.notices = res.data)
        .catch(err => console.error(err))
    },
    goCreateNotice() {
      const config = {
          headers: {
              'Authorization': `Token ${this.$cookies.get('auth-token')}`
          }
      }
      http.post('/community/notice/check/', null, config)
      .then(res => {
        if (res.data == '통과') {
          this.$router.push('/notice/createnotice/')
        } else {
          alert('운영자만 공지사항을 작성할 수 있습니다')
        }
      })
    },
    goDetail(id) {
      this.$router.push('/notice/noticedetail/' + id)
    }
  },
  created() {
    this.fetchData()
  }
}
</script>

<style>

</style>