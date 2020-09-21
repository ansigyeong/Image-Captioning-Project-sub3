<template>
    <div>
        <h1 style="text-align:center;">스피킹</h1>
        <div style="text-align:center;">
            <v-btn @click="callRandomImage" style="margin:1%;">
                랜덤 이미지 가져오기
            </v-btn>
            <v-btn @click="checkCaption" style="margin:1%;">
                캡셔닝 체크하기
            </v-btn>
            <input
                type="file"
                ref="files"
                accept="image/*"
                @change="imageUpload" />
        </div>
        <img v-if="previewImg.preview" :src="previewImg.preview">
        <v-btn v-if="previewImg.preview" @click="pushImage">이미지 업로드하기</v-btn>
        <div v-if="image">
            <h3 style="text-align:center;">
                <img :src = "`${this.image}`" style=""/>
            </h3>
            <br>
            <h3 style="text-align:center;">
                {{ this.capText }}
            </h3>
        </div>
    </div>
</template>

<script>
import http from '../util/http-common.js'

import axios from "axios"

const BACK_URL = 'http://127.0.0.1:8000'

export default {
    data () {
      return {
        image: null,
        capText: '',
        previewImg: {
            file: "",
            preview: "",
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
            .then(() => {

            })
        },
    }
}
</script>

<style>

</style>