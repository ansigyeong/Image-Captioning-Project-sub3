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
            <br>
            <br>
            <v-btn
                color="deep-purple accent-4"
                style="text-align: center; width:99.35px;"
                @click="displayword()"
            >
                확인하기
            </v-btn>
        </div>
        
        <br>

        <!-- section2 단어 카드-->
        <div style="text-align: center;">
            <v-card
                width="350"
                height="250"
                v-for="(word, i) in words" 
                :key="i"
                style="margin-bottom: 20px; margin-right: 20px; display: inline-block; vertical-align: middle;"
            >
                <v-card-text style="vertical-align: middle;">
                    <div :class="{ hidden: visible && i%2==0 }">
                        <p class="word">
                            {{ word.word }}
                        </p>
                        <p>
                            {{ word.phonetic_symbols }}
                        </p>
                    </div>
                    <div class="text--primary" :class="{ hidden: visible && i%2==1 }">
                        {{ word.mean }}
                        <br>
                    </div>
                    
                </v-card-text>
                <v-text-field label="입력해 보세요" style="width:250px; margin-left:15%;" />
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
        visible: true,
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
            this.visible = !this.visible
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
    .hidden{
        visibility: hidden;
    }
    .theme--light.v-card{
        background-color: white;
    }
</style>