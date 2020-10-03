<template>
    <v-container>
        <h1 style="text-align:center;">📑 My Wordbook 📑</h1>
        <br>
        <div style="text-align: center;">
            <v-card
            width="350"
            height="230"
            v-for="(word) in words" 
            :key="word.pid"
            style="margin-bottom: 20px; margin-right: 20px; display: inline-block; vertical-align: middle;"
            >
                <v-card-text style="vertical-align: middle;">
                    <!-- <div>Word of the Day</div> -->
                    <p class="display-1 text--primary">
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
                    @click="delword(word)"
                >
                    + 내 단어장에서 빼기
                </v-btn>
            </v-card>
        </div>
    </v-container>
</template>

<script>
import http from '../util/http-common.js'

export default {
    data () {
      return {
        words: '',
      }
    },
    created() {
        const config = {
            headers: {
                'Authorization': `Token ${this.$cookies.get('auth-token')}`
            }
        }
        http.post(`/english/userwordlist/`, null, config)
            .then(res => {
                this.words = res.data
            })
    },
    methods: {
        delword(thisword) {
            const data = {
                "word": thisword.word,
            }
            const config = {
                headers: {
                    'Authorization': `Token ${this.$cookies.get('auth-token')}`
                }
            }
            http.post(`/english/deleteuserword/`, data, config)
            .then(res => {
                console.log(res)
                this.$router.go()
            })
            .catch(err => {
                console.log(err)
            })
        }
    }
}
</script>

<style scoped>

</style>