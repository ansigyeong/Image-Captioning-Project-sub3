<template>
  <div class="container">
    <Navbar/>
    <div class="bin"></div>

    <div style="text-align: center;"><h1>🔉 Notice 🔉</h1></div>
    <br>
    <br>

    <!-- title & etc -->
    <div class="title">
      <h1>{{ this.notice.title }}</h1>
    </div>
    <div style="text-align: right;">
      <p>{{ this.notice.created_at | moment('YYYY-MM-DD') }}</p>
    </div>
    <div style="text-align: right;">
      <v-btn @click="goEdit">EDIT</v-btn>
      <v-btn @click="goDelete">DELETE</v-btn>
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
import Navbar from "../components/common/Navigation"

export default {
  name: 'noticeDetail',
  components: {
        Navbar,
  },
  data() {
    return {
      notice: [],
    }
  },
  created() {
    this.notice_pk = this.$route.params.notice_pk
    this.fetchData()
  },
  methods: {
    fetchData() {
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
    },
    goDelete() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      http.delete(`/community/notice/` + this.notice_pk + `/delete/`, config)
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
      this.$router.push('/notice/editnotice/' + this.notice_pk)
    }
  }
}
</script>

<style scoped>
  .bin{
    height: 70px;
  }
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