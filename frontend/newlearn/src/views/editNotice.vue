<template>
  <div class="container">
    
    <div style="text-align: center;"><h1>🔉 Notice 🔉</h1></div>
    <br>
    <br>
    <v-form>
      <v-text-field v-model="notice.title"
        id="title"
        label="제목을 입력해주세요."
        single-line
        full-width
        solo
      ></v-text-field>
      <div>
        <editor api-key="vem3wnp12tvfllgyuf92uzd6e04f9ddz4ke9mzv8uh71ctgq" :init="{
            height: 500,
            menubar: ['file edit view insert format tools'],
            plugins: [
              'advlist autolink lists link image charmap print preview anchor',
              'searchreplace visualblocks code fullscreen',
              'insertdatetime media table paste code help wordcount codesample'
            ],
            toolbar:
              'undo redo codesample | formatselect | bold italic backcolor | \
              alignleft aligncenter alignright alignjustify | \
              bullist numlist outdent indent | removeformat | help'
          }" v-model="notice.content" id="content" />
        <br>
        <br>
        <div style="text-align: right;">
          <v-btn @click="updateNotice">Submit</v-btn>
        </div>
    </div>
    </v-form>
  </div>
</template>

<script>
import http from '../util/http-common.js'
import Editor from '@tinymce/tinymce-vue'

export default {
  name: 'editNotice',
  components: {
    'editor': Editor
  },
  data() {
    return {
      notice: [],
    };
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
    updateNotice() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      http.post(`/community/notice/` + this.notice_pk + `/update/`, this.notice, config)
      .then(() => {
        this.$router.push({ name: 'noticeList' })
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
}
</script>

<style scoped>

</style>