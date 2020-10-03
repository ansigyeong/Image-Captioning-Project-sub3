<template>
  <v-container>
    <Navbar/>
    <div class="bin"></div>
    
    <h1 style="text-align:center;">📑 Word of the Day 📑</h1>
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
          <!-- <v-list-item
            v-for="(item, i) in items"
            :key="i"> -->
            <!-- <v-list-item-title>{{ item.title }}</v-list-item-title> -->
            <v-list-item-title @click="callToeicVocabulary">TOEIC</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title @click="callToeicVocabulary">OPIc</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title @click="callSATVocabulary">SAT</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
    <br>

    <!-- section2 단어 카드-->
    <div v-if="words" style="text-align: center;">
      <!-- <h3 style="text-align:center;">
          {{ $moment(today).format('YYYY년 MM월 DD일') }}의 단어
      </h3>
      <br> -->
      
      <v-card
        width="350"
        height="200"
        v-for="(word) in words" 
        :key="word.pid"
        style="margin-bottom: 20px; margin-right: 20px; display: inline-block; vertical-align: middle;"
      >
        <v-card-text style="vertical-align: middle;">
          <!-- <div>Word of the Day</div> -->
          <p class="word">
            {{ word.word }}
          </p>
          <p>
              {{ word.phonetic_symbols }}
          </p>
          <div class="text--primary">
            {{ word.mean }}<br>
            <!-- 예시 -->
          </div>
        </v-card-text>
        
        <v-btn
          text
          color="deep-purple accent-4"
          style="text-align: center;"
          @click="addword(word)"
        >
          + 내 단어장에 추가
        </v-btn>
      </v-card>

      <!-- original -->
      <!-- <li v-for="(word) in words" :key="word.pid" style="margin-left:20%;">
          {{ word.word }} : {{ word.mean }}
      </li> -->

    </div>
  </v-container>
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
        today: localStorage.getItem("today"),
        choice: '',
      }
    },
    created() {
        // console.log(localStorage.words)
    }
    ,
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
        callToeicVocabulary() {
            this.choice = {'Toeic': true}
            this.callVocabulary(this.choice)
        },
        callOpicVocabulary() {
            this.choice = {'Opic': true}
            this.callVocabulary(this.choice)
        },
        callSATVocabulary() {
            this.choice = {'korean_SAT': true}
            this.callVocabulary(this.choice)
        },
        addword(thisword) {
            const data = {
                "word": thisword.word,
                "phonetic_symbols": thisword.phonetic_symbols,
                "mean": thisword.mean
            }
            const config = {
                headers: {
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            }
            http.post(`/english/adduserword/`, data, config)
            .then(res => {
                // console.log(res)
                if(res.data == '존재함') {
                  alert('이미 단어장에 추가한 단어입니다.')
                }
            })
            .catch(err => {
                console.log(err)
            })
        },

    }
}
</script>

<style scoped>
  .word{
    font-size: 30px;
  }
    .bin{
        height: 70px;
    }
</style>