<template>
  <div class="container">
    <div style="text-align: center;"><h1>공지사항 작성</h1></div>
    <br>
    <br>
    <v-form>
      <v-text-field v-model="title"
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
        }" v-model="contents"  />
    </div>
      <v-divider></v-divider>
      <v-card-actions style="float:right">
        <v-btn text @click="back">취소</v-btn>
        <v-spacer></v-spacer>
        <v-btn text @click="createNotice">Submit</v-btn>
      </v-card-actions>
    </v-form>
  </div>
</template>


<script>
import http from '../util/http-common.js'
import Editor from '@tinymce/tinymce-vue'

export default {
  name: 'createNotice',
  components: {
    'editor': Editor
  },
  data() {
      return {
        noticeData: {
          title: null,
          content: null,
          editorText: 'This is initialValue.',
          editorOptions: {
            hideModeSwitch: true
          },

        }
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
        http.post("/notice/create", this.noticeData, config)
          .then(res => { 
            console.log(res.data) 
            this.$router.push({ name: 'vocList' })
          })
          .catch(err => console.log(err.response.data))
      },
    },
  }
</script>

<style>

</style>