<template>
  <div class="container">
    <!-- 1 -->
    <!-- <h1>건의 & 불편 신고</h1>
    <v-form>
      <v-autocomplete
        v-model="selected"
        :items="['Trevor Handsen', 'Alex Nelson']"
        chips
        label="Category"
        full-width
        hide-details
        hide-no-data
        hide-selected
        multiple
        single-line
      ></v-autocomplete>
      <v-divider></v-divider>
      <v-text-field
        label="Subject"
        value="Title"
        single-line
        full-width
        hide-details
      ></v-text-field>
      <v-divider></v-divider>
      <v-textarea
        v-model="title"
        label="Message"
        counter
        maxlength="120"
        full-width
        single-line
      ></v-textarea>
    </v-form>
    <div class="button">
      <input type="submit" style="text-align: right;" value="Submit" @click="goSubmit">
    </div> -->

    <!-- 2 -->
    <div style="text-align: center;"><h1>👩 Voice Of the Customer 👨</h1></div>
    <br>
    <br>
   
    <div>
      <h1>New Article</h1>
      <div>
        <label for="title">title:</label>
        <input v-model="articleData.title" id="title" type="text" />
      </div>
      <div>
        <label for="content">content:</label>
        <textarea v-model="articleData.content" id="content" cols="30" rows="10"></textarea>
      </div>
      <div>
        <button @click="createArticle">Submit!</button>
    </div>
    </div>
    <!-- 3 -->
    <!-- <div>
      <label for="title">title:</label>
      <input v-model="articleData.title" id="title" type="text" />
    </div>
    <div>
      <label for="content">content:</label>
      <textarea v-model="articleData.content" id="content" cols="30" rows="10"></textarea>
    </div>
    <div>
      <button @click="createArticle">Submit!</button>
    </div> -->
  </div>
</template>

<script>
// import axios from 'axios'
  import http from '../util/http-common.js'
  
  // import Editor from '@tinymce/tinymce-vue'

  export default {
    name: 'createVoc',
    // components: {
    //   'editor': Editor
    // },
    // data () {
    //   return {
    //     selected: [],
    //     items: [],
    //     title: '',
    //   }
    // },
    // methods: {
    //   goSubmit() {

    //   }
    // }
    data() {
      return {
        articleData: {
          title: null,
          content: null,

        },
        // editorText: 'This is initialValue.',
        // editorOptions: {
        //   hideModeSwitch: true
        // },
      };
    },
    methods: {
      createArticle() {
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        // article 생성은 Header: Token / Body: { title: , content: }
        http.post('/community/suggestion/create/', this.articleData, config)
          .then(res => { 
            console.log(res.data) 
            this.$router.push({ name: 'vocList' })
          })
          .catch(err => console.log(err.response.data))
      },
    },
  }
</script>

<style scoped>
  /* input[type='submit'] {
    background-color: #3d8fc5;
    color: #eee;
    font-weight: 700;
    text-transform: uppercase;
  }

  input[type='submit']:focus,
  input[type='submit']:hover {
    background-color: #073a5c;
  }

  .button {
    margin-top: 30px;
    text-align: right;
  } */
</style>