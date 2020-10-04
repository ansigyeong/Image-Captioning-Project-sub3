<template>
  <div class="bg">
    <Navbar/>
    <div class="bin"></div>

    <div style="text-align: center;"><h1>👩 Voice Of the Customer 👨</h1></div>
    <br>
    <br>
    <v-form>
      <v-text-field v-model="suggestion.suggestion.title"
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
          }" v-model="suggestion.suggestion.content" id="content" />
        <br>
        <br>
        <div style="text-align: right;">
          <v-btn @click="updateVoc">Submit</v-btn>
        </div>
    </div>
    </v-form>
  </div>
</template>

<script>
import http from '../util/http-common.js'
import Editor from '@tinymce/tinymce-vue'
import Navbar from "../components/common/Navigation"
import '@/assets/css/background.css'

export default {
  name: 'editVoc',
  components: {
    'editor': Editor,
    Navbar,
  },
  data() {
    return {
      suggestion: [],
    };
  },
  created() {
    this.suggestion_pk = this.$route.params.suggestion_pk
    this.fetchData()
  },
  methods: {
    fetchData() {
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
    updateVoc() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      http.post(`/community/suggestion/` + this.suggestion_pk + `/update/`, this.suggestion, config)
      .then(() => {
        this.$router.push({ name: 'vocList' })
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
}
</script>

<style scoped>
    .bin{
        height: 70px;
    }
       @media(max-width: 480px){
        h1{
            font-size: 20px;
        }
    }
</style>