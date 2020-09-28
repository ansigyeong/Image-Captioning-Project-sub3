<template>
    <div class="container">
        <div style="text-align: center;"><h1>📅 Attendance 📅</h1></div>
        <br>
        <br>
        <v-row>
            <v-col cols="12" md="4" offset-md="2" style="text-align:center;">
                <v-date-picker v-model="picker"
                :event-color="date => date[9] % 2 ? 'red' : 'yellow'"
                :events="functionEvents"></v-date-picker>
            </v-col>
            <v-col cols="12" md="4" v-if="daily.length >= 1" style="text-align:center;">
                <p>{{ daily[0].date }}</p>
                <p>이미지 스피킹 : {{ daily[0].image_speak_count }}</p>
                <p>리스닝 : {{ daily[0].listening_count }}</p>
                <p>단어장 : {{ daily[0].vocabulary_count }}</p>
            </v-col>
            <v-col cols="12" md="4" v-else style="text-align:center;">
                <p>활동 내역이 없습니다</p>
            </v-col>
        </v-row>
    </div>
</template>

<script>
import http from '../util/http-common.js'

export default {
    name: 'Attendance',
    components: {
    },
    data () {
        return {
            daily: '',
            month: '',
            picker: new Date().toISOString().substr(0, 10),
            day: '',
        }
    },
    created() {
        this.getLists()
    },
    mounted() {
    },
    watch: {
        picker: function () {
            this.getLists()
        }
    },
    methods: {
        getLists() {
            const config = {
                headers: {
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            }
            this.day = { 'day' : this.picker }
            // 테스트용으로 '2번' 유저에 대해 요청을 보냄.
            // 연동 완료 시 요청보내는 유저로 보낼 것
            // 수정완료
            http.post(`/accounts/daily/`, this.day, config)
            .then(res => {
                this.daily = res.data.day
                this.month = res.data.month
            })
        },
        functionEvents (date) {
            const [,, day] = date.split('-')
            if (this.month.includes(parseInt(day, 10))) return ['green']
            return false
        },
    }
}
</script>

<style>

</style>