<template>
  <div class="container">
    <Navbar/>
    <div class="bin"></div>

    <div style="text-align: center;"><h1>🔉 Notice 🔉</h1></div>
    <br>
    <br>
    <div class="content-back">
      <v-form>
        <v-text-field v-model="noticeData.title"
          id="title"
          label="제목을 입력해주세요"
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
          }" v-model="noticeData.content" id="content" />
        <br>
        <br>
        <div style="text-align: right;">
          <v-btn @click="createNotice">Submit</v-btn>
        </div>
      </div>
      </v-form>
    </div>
  </div>
</template>


<script>
import http from '../util/http-common.js'
import Editor from '@tinymce/tinymce-vue'
import Navbar from "../components/common/Navigation"

export default {
  name: 'createNotice',
  components: {
    'editor': Editor,
    Navbar,
  },
  data() {
      return {
        noticeData: {
          title: null,
          content: null,
          created_at: null,
        },
      };
    },
    methods: {
      createNotice() {
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        // 게시글 생성은 Header: Token / Body: { title: , content: }
        http.post('/community/notice/create/', this.noticeData, config)
          .then(res => { 
            console.log(res.data) 
            this.$router.push({ name: 'noticeList' })
          })
          .catch(err => console.log(err.response.data))
      },
    },
  }
</script>

<style scoped>
  .bin{
    height: 70px;
  }
  .content-back {
    /* background-color: rgb(255, 255, 255, 0.9);
    border-radius: 1rem; */
  }
</style>