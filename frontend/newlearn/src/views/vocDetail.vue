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

    <!-- 3. 댓글 리스트 -->
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
          <v-btn @click="createComment">Submit</v-btn>
        </div>
    </div>
    <!-- 4. 댓글 작성 -->

  </div>
</template>

<script>
import http from '../util/http-common.js'
import Editor from '@tinymce/tinymce-vue'

export default {
  name: 'vocDetail',
  components: {
    'editor': Editor
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
    // fetchComment() {
    //   const config = {
    //     headers: {
    //       Authorization: `Token ${this.$cookies.get('auth-token')}`
    //     }
    //   }
    //   http.get('')
    // },
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
        })
        .catch(err => {
          console.log(err)})
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