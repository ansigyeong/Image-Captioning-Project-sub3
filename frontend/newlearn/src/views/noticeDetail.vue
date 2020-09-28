<template>
  <div></div>
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
      http.get("/notice/noticedetail/" + this.notice_pk, config)
      .then((res) => {
        this.notice = res.data
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>

</style>