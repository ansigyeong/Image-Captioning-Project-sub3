<template>
    <div style="text-align:center;">
        <h1 style="text-align:center;">스피킹</h1>
        <div style="text-align:center;">
            <v-btn @click="callRandomImage" style="margin:1%;">
                랜덤 이미지 가져오기
            </v-btn>
            <input
                type="file"
                ref="files"
                accept="image/*"
                @change="imageUpload" />
        </div>
        <div style="text-align:center;">
            <img v-if="previewImg.preview" :src="previewImg.preview" style="min-width:100px; max-width:600px;">
            <br>
            <v-btn @click="pushImage">이미지 업로드하기</v-btn>
            <v-btn v-if="capText != ''" @click="viewText" style="margin:1%;">
                예시 답안 보기
            </v-btn>
            <!-- <p>{{ this.capText }}</p> -->
            <p v-if="showText == true">
                {{ this.capText }}
            </p>
        </div>
        <br>
        <div v-if="image">
            <h3 style="text-align:center;">
                <img :src = "`${this.image}`" style=""/>
            </h3>
            <br>
            <h3 style="text-align:center;">
                {{ this.capText }}
            </h3>
        </div>
        <audio-recorder
            upload-url="/english/imageupload/"
            :attempts="1"
            :time="1"
            :before-recording="callback"
            :pause-recording="callback"
            :after-recording="callback"
            :select-record="callback"
            :before-upload="callback"
            :successful-upload="callback"
            :failed-upload="callback"
            style="margin-left:25%; margin-right:25%;"/>
        <br>
        <v-btn @click="checkVoice" style="margin:1%;">
            녹음 파일 확인하기
        </v-btn>
    </div>
</template>

<script>
import http from '../util/http-common.js'

import axios from "axios"

const BACK_URL = 'http://127.0.0.1:8000'
const kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
const rest_api_key = "4b1318b8f31e1675d1e5e72a4638636f"

export default {
    data () {
      return {
        image: null,
        capText: '',
        showText: false,
        previewImg: {
            file: "",
            preview: "",
            voice: "",
        },
      }
    },
    created() {
        // console.log(localStorage.words)
    }
    ,
    methods: {
        callRandomImage() {
            axios.post(`${BACK_URL}/english/speaking/`)
            .then(res => {
                console.log(res.data)
                this.image = BACK_URL + res.data[0].image
                this.capText = res.data[0].cap_text
            })
        },
        checkCaption() {
            axios.post(`${BACK_URL}/english/imagecaption/`)
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
            http
            .put(`/english/imageupload/`, InputData)
            .then((res) => {
                this.capText = res.data
                console.log(res.data)
            })
        },
        callback (data) {
            console.debug(data)
            this.voice = data
        },
        checkVoice() {
            var voiceHeader = {
                "Content-Type": "application/octet-stream",
                "Authorization": "KakaoAK " + rest_api_key,
            }
            axios.post(`${kakao_speech_url}`, voiceHeader, this.voice)
            .then(res => {
                console.log(res.data)
            })
            .catch(res => {
                console.log(res.data)
            })
        },
        viewText() {
            this.showText = !this.showText
        }
    }
}
</script>

<style>

</style>