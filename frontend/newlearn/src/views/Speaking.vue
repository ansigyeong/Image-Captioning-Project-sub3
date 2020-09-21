<template>
    <div>
        <h1 style="text-align:center;">스피킹</h1>
        <div style="text-align:center;">
            <v-btn @click="callRandomImage" style="margin:1%;">
                랜덤 이미지 가져오기
            </v-btn>
            <v-btn @click="imageUpload" style="margin:1%;">
                이미지 업로드하기
            </v-btn>
        </div>
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
import axios from "axios"

const BACK_URL = 'http://127.0.0.1:8000'

export default {
    data () {
      return {
        image: null,
        capText: '',
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
        imageUpload() {
            axios.post(`${BACK_URL}/english/imagecaption/`)
        }
    }
}
</script>

<style>

</style>