<template>
  <div class="container">
    <div style="text-align: center;"><h1>🔉 Notice 🔉</h1></div>
    <br>
    <br>

    <!-- title & etc -->
    <div class="title">
      <h1>{{ this.notice.title }}</h1>
    </div>
    <div style="text-align: right;">
      <p>{{ this.notice.created_at }}</p>
    </div>
    <div style="text-align: right;">
      <v-btn>EDIT</v-btn>
      <!-- <v-btn @click="goDelete">DELETE</v-btn> -->
    </div>

    <hr>

    <!-- content -->
    <div v-html="this.notice.content" style="margin:20px" class="contentbox"></div>
    <!-- <div class="content">
      <h3>{{ this.suggestion.content }}</h3>
    </div> -->
  </div>
</template>

<script>
import http from '../util/http-common.js'

export default {
  name: 'noticeDetail',
  data() {
    return {
      notice: [],
    }
  },
  created() {
    this.notice_pk = this.$route.params.notice_pk
    this.fetchDetail()
  },
  methods: {
    fetchDetail() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      http.get("/community/notice/" + this.notice_pk, config)
      .then((res) => {
        this.notice = res.data
      })
      .catch(err => console.log(err))
    }
  }
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