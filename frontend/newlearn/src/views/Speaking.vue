<template>
    <div class="bg">
        <Navbar/>
        <div style="min-height: 100%;">
            <div class="bin"></div>

            <h1><i class="fas fa-volume-up" style="font-size:50px;"></i> Speaking</h1>

            <div class="link">
                <span style="background-color:yellow"><i class="fa fa-exclamation-triangle" aria-hidden="true" style="color:red;"></i>
                jpg 파일만 사용가능 (<a href="https://convertio.co/kr/png-jpg/">jpg convert site</a>)</span>
            </div>

            <h2><i class="fa fa-download" aria-hidden="true" style="font-size:30px;"></i> Picture Upload</h2>

            <div class="putfile">

                <div class="putfile">
                    <input
                        type="file"
                        class="fileload"
                        ref="files"
                        accept="image/*"
                        @change="imageUpload" />
                </div>

                <img v-if="previewImg.preview" :src="previewImg.preview" style="min-width:100px; max-width:600px;">

                <div v-if="image">
                    <img src = "`${this.image}`" />
                    <p class = "res">{{ this.capText }}</p>
                </div>
                <div>
                    <v-btn class="button button1" v-if="previewImg.preview" @click="pushImage">Image Captioning</v-btn>
                    <v-btn class="button button1" v-if="capText != ''" @click="viewText" style="margin:1%;">
                        Example Answer
                    </v-btn>
                </div>
                <p class = "res" v-if="this.showText == true">
                    {{ this.capText }}
                </p>
            </div>

            <h2 class="myvoice"><i class="fa fa-file" aria-hidden="true" style="font-size:30px;"></i> My Voice Recorder</h2>
            
            <div class="recorder">
                <audio-recorder 
                    upload-url="YOUR_API_URL"
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
            </div>

            <h2><i class="fa fa-download" aria-hidden="true" style="font-size:30px;"></i> My Voice RecorderFile Upload</h2>
            
            <div class="putfile">
                <input
                    type="file"
                    class="fileload"
                    ref="audio"
                    accept="audio/*"
                    @change="audioUpload" />
                <br>
                <br>
                <audio class="player" controls ref="player">
                    <source src="" ref="source">
                </audio>
                <br>
                <v-btn class="button button1" v-if="this.uploadFile" @click="pushFile">Voice To Text</v-btn>

                <v-btn class="button button1" v-if="userVoice != ''" @click="viewText" style="margin:1%;">
                    Your Vocie Text
                </v-btn>
                <p class = "res" v-if="this.showText == true">
                    {{ this.userVoice }}
                </p>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
import http from '../util/http-common.js'
import Navbar from "../components/common/Navigation"
import Footer from "../components/common/footer"
import '@/assets/css/background.css'

export default {
    components: {
        Navbar,
        Footer
    },
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
            this.userVoice = '';
            //다른거 업로드할때를 위해 초기화
            //event.target.value ='';
        },
         pushFile() {
            var InputData = new FormData()
            InputData.append("inputFile", this.uploadFile)
            http
            .put(`/english/speaksound/`, InputData)
            .then((res) => {
                this.userVoice = res.data
                // console.log(res.data)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        callRandomImage() {
            http.post(`/english/speaking/`)
            .then(res => {
                // console.log(res.data)
                this.image = "http://localhost:8000" + res.data.serializer[0].image
                this.capText = res.data.return_text
            })
        },
        checkCaption() {
            http.post(`/english/imagecaption/`)
            .then()
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
        },
        viewText() {
            this.showText = !this.showText
        },
        speakSituation() {
            http
            .post(`/english/speakSituation/`)
            .then((res) => {
                // console.log(res)
                this.userVoice = res.data
            })
        }
    }
}
</script>

<style scoped>
    .bin{
        height: 70px;
    }
    .res{
        font-family: 'Secular One', sans-serif;
        font-size: 20px;
    }
    .recorder{
        max-width: 420px;
        /* border-style:double dashed; */
        margin: auto;
    }
    .fileload{
        border-style: solid;
        border-width: thin medium thick 5px;
        padding:10px;
        font-size: 15px;
        font-weight: 700;
        text-align: center;
    }
    h2{
        margin: 20px;
        font-family: 'Secular One', sans-serif;
        font-size: 30px ;
        text-align: center;
    }
    h1{
        margin: 20px;
        font-family: 'Secular One', sans-serif;
        font-size: 50px ;
        text-align: center;
    }
    img {
        width: 400px;
        height: 400px;
        object-fit: contain;
    }
    .link, .putfile, .mytext, .compare{
        font-family: 'Secular One', sans-serif;
        text-align: center;
        margin: 20px;
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

    @media(max-width: 480px){
        .recorder{
           display: none;
        }
        .res{
         font-family: 'Secular One', sans-serif;
         font-size: 10px;
        }
        .fileload{
            border-style: solid;
            border-width: thin medium thick 5px;
            padding: 10px;
            font-size: 10px;
            font-weight: 200;
            text-align: center;
        }
        h2{
            margin: 20px;
            font-family: 'Secular One', sans-serif;
            font-size: 15px ;
            text-align: center;
        }
        .myvoice{
            display: none;
        }
        h1{
            margin: 10px;
            font-family: 'Secular One', sans-serif;
            font-size: 50px ;
            text-align: center;
        }
        img {
            width: 200px;
            height: 200px;
            object-fit: contain;
        }
        .link, .putfile, .mytext, .compare{
            font-weight: 900;
            font-family: 'Secular One', sans-serif;
            text-align: center;
            margin: 10px;
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
            font-size: 10px;
            margin: 4px 2px;
            transition-duration: 0.4s;
            cursor: pointer;
        }

        .button1 {
            background-color: white; 
            color: black; 
            border: 2px solid #4CAF50;
            margin-left: 25%;
            margin-right: 25%;
        }  
    }
    
</style>