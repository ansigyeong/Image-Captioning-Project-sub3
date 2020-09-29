<template>
  <div>
        <h1><i class="fas fa-headphones-alt" style="font-size:50px;"></i> Listening</h1>

        <div class="link">
            <p><i class="fa fa-exclamation-triangle" aria-hidden="true" style="color:red;"></i>
            10MB 이하의 wav/mp3/mp4 파일만 사용가능 (<a href="https://online-audio-converter.com/ko/">wav/mp3/mp4 convert site</a>)</p>
        </div>

        <div class="putfile">
            <input
                type="file"
                class="fileload"
                ref="files"
                accept="audio/*"
                @change="audioUpload" />
            <br>
            <br>
            <audio class="player" controls ref="player">
                <source src="" ref="source">
            </audio>
            <br>
            <v-btn class="button button1" v-if="this.uploadFile" @click="pushFile">Voice To Text</v-btn>

            <v-btn class="button button1" v-if="capText != ''" @click="viewText" style="margin:1%;">
                Example answer
            </v-btn>
            <p class = "res" v-if="this.showText == true">
                {{ this.capText }}
            </p>
        </div>

        <div class="mytext">
            <textarea v-model="message" id="textbox" onkeyup="charcountupdate(this.value)"> Start typing here to see results</textarea>
            <span id=charcount></span>
            <br>
            <v-btn  class="button button1" @click="checkText">Compare My Text</v-btn>
        </div>

        <div class="compare">
            <span class = "res" v-for="(word, i) in userText" :class="{ wrong: userText[i] != wrongCheck[i] }" :key="{i}">
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
            //event.target.value ='';
        },
        pushFile() {
            var InputData = new FormData()
            InputData.append("inputFile", this.uploadFile)
            const config = {
                headers: {
                    'Authorization': `Token ${this.$cookies.get('auth-token')}`
                }
            }
            http
            .put(`/english/soundupload/`, InputData, config)
            .then((res) => {
                this.capText = res.data
                // console.log(res.data)
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
    @import url('https://fonts.googleapis.com/css2?family=Secular+One&display=swap');
    .res{
         font-family: 'Secular One', sans-serif;
         font-size: 20px;
    }
    .fileload{
        border-style: solid;
        border-width: thin medium thick 5px;
        padding:10px;
        font-size: 15px;
        font-weight: 700;
        text-align: center;
    }
    .link, .putfile, .mytext, .compare{
        font-family: 'Secular One', sans-serif;
        text-align: center;
        margin: 20px;
    }
    h1{
        margin: 20px;
        font-family: 'Secular One', sans-serif;
        font-size: 50px ;
        text-align: center;
    }
    .wrong {
        color: red;
    }
    textarea {
        font-family: 'Secular One', sans-serif;
        border: 2px;
        background-color:#008c9e;
        color: white;
        border-color: black;
        width: 400px;
        height: 100px;
    }
    .button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 16px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-family: 'Secular One', sans-serif;
        font-size: 20px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }

    .button1 {
        background-color: white; 
        color: black; 
        border: 2px solid #4CAF50;
    }
</style>