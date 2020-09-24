<template>
  <div style="text-align:center;">
        <h1 style="text-align:center;">리스닝</h1>
        <a href="https://online-audio-converter.com/ko/">wav convert site</a>
        <p>10MB 이하의 wav 파일만 사용가능</p>
        <input
            type="file"
            ref="files"
            accept="audio/*"
            @change="audioUpload" />
        <br>
        <br>
        <audio class="player" controls ref="player">
            <source src="" ref="source">
        </audio>
        <div style="text-align:center;">
            <br>
            <v-btn v-if="this.uploadFile" @click="pushFile">파일 업로드하기</v-btn>
            <v-btn v-if="capText != ''" @click="viewText" style="margin:1%;">
                예시 답안 보기
            </v-btn>
            <p v-if="this.showText == true">
                {{ this.capText }}
            </p>
        </div>
        <div>
            <input v-model="message" placeholder="여기를 수정해보세요">
            <v-btn @click="checkText">예시 답안과 비교하기</v-btn>
        </div>
        <br>
        <div>
            <span v-for="(word, i) in userText" :class="{ wrong: userText[i] != wrongCheck[i] }" :key="{i}">
                {{ word }}
            </span>
        </div>
  </div>
</template>

<script>
import http from '../util/http-common.js'

export default {
    data () {
        return {
            uploadFile: '',
            capText: '',
            showText: false,
            message: '',
            wrongCheck: '',
            userText: '',
        }
    },
    methods: {
        audioUpload() {
            const uploadSound = event.target.files[0];
            const audioSrc = window.URL.createObjectURL(uploadSound);
            this.$refs.source.src = audioSrc;

            this.uploadFile = uploadSound
            
            //업로드완료 후 파일로딩
            this.$refs.player.load();

            //다른거 업로드할때를 위해 초기화
            event.target.value ='';
        },
        pushFile() {
            var InputData = new FormData()
            InputData.append("inputFile", this.uploadFile)
            http
            .put(`/english/soundupload/`, InputData)
            .then((res) => {
                this.capText = res.data
                console.log(res.data)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        viewText() {
            this.showText = !this.showText
        },
        checkText() {
            var check = {
                'STTtext': this.capText,
                'usertext': this.message,
            }
            http.post(`/english/checktext/`, check)
            .then((res) => {
                console.log(res.data)
                this.wrongCheck = res.data.stttext,
                this.userText = res.data.usertext
            })
            .catch((err) => {
                console.log(err)
            })
        }
    }
}
</script>

<style scoped>
    .wrong {
        color: red;
    }
</style>