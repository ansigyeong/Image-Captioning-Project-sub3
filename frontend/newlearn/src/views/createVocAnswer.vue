<template>
  <div>

    <!-- answer 보여줌 voc answer detail로 옮기기 -->
    <!-- <span v-for="(item,idx) in replyitems" :key="idx">
      <b-media right-align>
        <div>
          <div class="bording" style="margin-left:50px" >
            <div style="height:10px"></div>
            <div v-html="item.contents" style="margin:20px"></div>
            <div style="height:10px"></div>
          </div>
        </div>
        <template v-slot:aside>
            <div>
                <v-btn @click="replydelete(item.rpNo)">답변 삭제하기</v-btn>
                <v-btn @click="replyupdate(item.rpNo, item.contents, item.email)">답변 수정하기</v-btn>
            </div>
        </template>
      </b-media> 
    </span> -->

    <!-- <span v-if="isLoggedIn">   -->
      <b-container fluid>
        <div style="text-align:center;">
          <h2>답변 작성</h2>
          <div >
            <editor api-key="vem3wnp12tvfllgyuf92uzd6e04f9ddz4ke9mzv8uh71ctgq" :init="{
                height: 300,
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
                }" v-model="replycontents" />
          </div>
        </div>
        <b-button class="dd" @click="writereply">답변 등록</b-button>
      </b-container>
    <!-- </span> -->

  </div>
</template>

<script>
// import http from '../util/http-common.js'
import Editor from '@tinymce/tinymce-vue'

export default {
    name: 'createVocAnswer',
    data() {
        return {
            replycontents: '',
        }
    },
    components: {
            'editor': Editor,
            // VueCodeHighlight,
    },

}
</script>

<style scoped>

</style>