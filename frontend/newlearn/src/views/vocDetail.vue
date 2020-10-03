<template>
  <div class="container">
    <Navbar/>
    <div class="bin"></div>

    <!-- <div style="text-align: center;"><h1>👩 Voice Of the Customer 👨</h1></div> -->
    <!-- <br> -->
    <!-- <br> -->

    <!-- 1. title & etc -->
    <div class="title">
      <h1>{{ suggestion.suggestion.title }}</h1>
    </div>
    <!-- <div style="text-align: right;">
    </div> -->
    <div style="text-align: right;">
      <v-btn icon style="margin-right: 50px;">{{ suggestion.suggestion.created_at | moment('YYYY-MM-DD') }}</v-btn>
      <v-btn icon @click="goEdit" style="margin-right: 50px;"><v-icon left>mdi-pencil</v-icon>EDIT</v-btn>
      <v-btn icon @click="goDelete" style="margin-right: 50px;"><v-icon left>mdi-cancel</v-icon>DELETE</v-btn>
    </div>
    <hr>

    <!-- 2. content -->
    <h3><div v-html="suggestion.suggestion.content" style="margin:20px; min-height: 250px;" class="contentbox"></div></h3>
    <hr>
    <!-- 3. 댓글 리스트 -->
    <p><v-icon>fas fa-edit</v-icon> Comments</p>
    <hr>
    <!-- <p>Comment List</p> -->
    <div v-for="comment in suggestion.comments" :key="comment.id">
      <div style="background-color: #F5F5F5;">
        <h6 style="display: inline-block; margin-left: 20px;">{{ comment.user.username }}</h6>
        <v-btn icon x-small @click="deleteComment(comment.id)" style="display: inline-block; float: right; margin-right: 50px;"><v-icon left>mdi-cancel</v-icon>DELETE</v-btn>
        <v-btn icon x-small style="display: inline-block; float: right; margin-right: 50px;"><v-icon left>mdi-pencil</v-icon>EDIT</v-btn>
        <p style="display: inline-block; float: right; margin-right: 50px;"><small>{{ comment.created_at | moment('YYYY-MM-DD') }}</small></p>
      </div>
      <div v-html="comment.content" style="margin: 10px 0px 0px 20px;" class="contentbox"></div>
      <hr>
    </div>

    <!-- 4. 댓글 작성 -->
    <div>
      <editor api-key="vem3wnp12tvfllgyuf92uzd6e04f9ddz4ke9mzv8uh71ctgq" :init="{
          height: 120,
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
        }" v-model="commentData.content" id="comment" />
        <br>
        <div style="text-align: right;">
          <v-btn tile @click="createComment"><v-icon>mdi-pencil</v-icon>Submit</v-btn>
        </div>
    </div>
  </div>
</template>

<script>
import http from '../util/http-common.js'
import Editor from '@tinymce/tinymce-vue'
import Navbar from "../components/common/Navigation"

export default {
  name: 'vocDetail',
  components: {
    'editor': Editor,
    Navbar,
  },
  data() {
    return {
      suggestion: [],
      commentData: {
        content: null,
      },
    }
  },
  created() {
    this.suggestion_pk = this.$route.params.suggestion_pk
    this.fetchDetail()
  },
  methods: {
    // 1. 게시글
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
      this.$router.push('/mypage/editvoc/' + this.suggestion_pk)
    },
    // 2. 답글
    createComment() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      http.post(`/community/suggestion/` + this.suggestion_pk + `/commentcreate/`, this.commentData, config)
        .then(res => {
          console.log(res.data)
          alert('댓글이 성공적으로 작성되었습니다.')
          this.$router.go() // 현재 페이지로 새로고침
        })
        .catch(err => {
          console.log(err)})
    },
    deleteComment(commentId) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      http.delete('/community/suggestion/' + this.suggestion_pk + '/', commentId, config)
      this.$router.go()
    },
  },
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