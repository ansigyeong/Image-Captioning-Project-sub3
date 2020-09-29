<template>
    <div style="text-align:center;">
        <h1 style="text-align:center;">스피킹</h1>
         <a href="https://convertio.co/kr/png-jpg/">jpg convert site</a>
        <p>jpg 파일만 사용가능</p>
        <div style="text-align:center;">

            <input
                type="file"
                ref="files"
                accept="image/*"
                @change="imageUpload" />
        </div>
        <div style="text-align:center;">
            <img v-if="previewImg.preview" :src="previewImg.preview" style="min-width:100px; max-width:600px;">
            <br>
            <v-btn v-if="previewImg.preview" @click="pushImage">이미지 업로드하기</v-btn>
            <v-btn v-if="capText != ''" @click="viewText" style="margin:1%;">
                예시 답안 보기
            </v-btn>
            <p v-if="this.showText == true">
                {{ this.capText }}
            </p>
        </div>
        <br>
        <div v-if="image">
                <img src = "`${this.image}`"  />
            <br>
            <h3 style="text-align:center;">
                {{ this.capText }}
            </h3>
        </div>
        <br>

        <audio-recorder
            upload-url="YOUR_API_URL"
            filename="asdasd"
            :attempts="3"
            :time="2"
            :headers="headers"
            :before-recording="callback"
            :pause-recording="callback"
            :after-recording="callback"
            :select-record="callback"
            :before-upload="callback"
            :successful-upload="callback"
            :failed-upload="callback"/>

        <input
            type="file"
            ref="audio"
            accept="audio/*"
            @change="audioUpload" />
        <br>
        <br>
        <audio class="player" controls ref="player">
            <source src="" ref="source">
        </audio>
        <br>
        <v-btn v-if="this.uploadFile" @click="pushFile">
            Voice To Text
        </v-btn>
        <p>{{ this.userVoice }}</p>
    </div>
</template>

<script>
import http from '../util/http-common.js'

export default {
    data () {
      return {
        uploadFile: '',
        image: null,
        capText: '',
        showText: false,
        previewImg: {
            file: "",
            preview: "",
            voice: "",
        },
        userVoice: '',
      }
    },
    created() {
        // console.log(localStorage.words)
    }
    ,
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
                this.userVoice = res.data
                console.log(res.data)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        callRandomImage() {
            http.post(`/english/speaking/`)
            .then(res => {
                console.log(res.data)
                this.image = "http://localhost:8000" + res.data.serializer[0].image
                this.capText = res.data.return_text
            })
        },
        checkCaption() {
            http.post(`/english/imagecaption/`)
            .then(res => {
                console.log(res.data)
            })
        },
        imageUpload() {
            this.previewImg = {
                file: this.$refs.files.files[0],
                preview: URL.createObjectURL(this.$refs.files.files[0]),
            }
        },
        pushImage() {
            var InputData = new FormData()
            InputData.append("inputImage", this.previewImg.file)
            const config = {
                headers: {
                    'Authorization': `Token ${this.$cookies.get('auth-token')}`
                }
            }
            http
            .put(`/english/imageupload/`, InputData, config)
            .then((res) => {
                this.capText = res.data
                // console.log(res.data)
            })
        },
        callback (data) {
            console.debug(data)
            this.userVoice = data
        },
        viewText() {
            this.showText = !this.showText
        },
        speakSituation() {
            http
            .post(`/english/speakSituation/`)
            .then((res) => {
                console.log(res)
                this.userVoice = res.data
            })
        }
    }
}
</script>

<style>
  
</style>