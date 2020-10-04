<template>
    <div class="speak">
        <Navbar/>
        <div class="bin"></div>
        <h1 style="text-align:center;">📑 Word Check 📑</h1>
        <br>

        <!-- section1 분류 -->
        <div style="text-align: right; margin-right: 50px;">
            <v-menu
                transition="scale-transition"
                bottom
                right
            >
                <template v-slot:activator="{ on, attrs }">
                    <v-btn
                        dark
                        v-bind="attrs"
                        v-on="on"
                    >
                        단어 분류
                    </v-btn>
                </template>
                <v-list>
                    <v-list-item>
                        <v-list-item-title @click="callDailyWord">오늘의 단어</v-list-item-title>
                    </v-list-item>
                    <v-list-item>
                        <v-list-item-title @click="callUserWord">내 단어장</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
        </div>
        <br>

        <!-- section2 단어 카드-->
        <div style="text-align: center;">
            <v-card
                width="350"
                height="200"
                v-for="(word, i) in words" 
                :key="i"
                style="margin-bottom: 20px; margin-right: 20px; display: inline-block; vertical-align: middle;"
            >
                <v-card-text style="vertical-align: middle;">
                    <div>
                        <p class="word">
                            {{ word.word }}
                        </p>
                        <p>
                            {{ word.phonetic_symbols }}
                        </p>
                    </div>
                    <div class="text--primary" :style="{ visibility: computedvisible }">
                        {{ word.mean }}
                        <br>
                    </div>
                    <v-btn
                        text
                        color="deep-purple accent-4"
                        style="text-align: center;"
                        @click="displayword()"
                    >
                        표시 전환하기
                    </v-btn>
                </v-card-text>
            </v-card>
        </div>
    </div>
</template>

<script>
import http from '../util/http-common.js'
import Navbar from "../components/common/Navigation"

export default {
    components: {
      Navbar,
    },
    data () {
      return {
        words: JSON.parse(localStorage.getItem("words")),
        userword: '',
        visible: 'hidden',
      }
    },
    computed: {
        computedvisible() {
            return this.visible
        }
    },
    methods: {
        callVocabulary(choice) {
            const config = {
                headers: {
                    'Authorization': `Token ${this.$cookies.get('auth-token')}`
                }
            }
            http.post(`/english/vocabulary/`, choice, config)
            .then(res => {
                this.words = res.data.vocabulary
                localStorage.setItem("words", JSON.stringify(this.words))
                this.today = res.data.today
                localStorage.today = this.today
            })
        },
        callDailyWord() {
            this.words = JSON.parse(localStorage.getItem("words"))
        },
        callUserWord() {
            const config = {
                headers: {
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            }
            http.post(`/english/userwordcheck/`, null, config)
            .then(res => {
                this.words = res.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        displayword() {
            if(this.visible == 'visible') {
                this.visible = 'hidden'
            } else {
                this.visible='visible'
            }
        }
    },
}
</script>

<style scoped>
 .speak{
        background-image: url(../assets/images/Newyork.jpg) !important;
        background-size : cover;
    }
  .word{
    font-size: 30px;
  }
    .bin{
        height: 70px;
    }
    @media(max-width: 480px){
        h1{
            font-size: 30px;
        }
    }
</style>