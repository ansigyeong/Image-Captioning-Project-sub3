<template>
    <div class="bg">
        <Navbar/>
        <div style="min-height: 100%;">
            <div class="bin"></div>

            <div style="text-align: center;"><h1>📅 Attendance 📅</h1></div>
            <br>
            <br>
            <v-row>
                <v-col cols="12" md="4" offset-md="2" style="text-align:center; ">
                    <v-date-picker v-model="picker"
                    :events="functionEvents"></v-date-picker>
                </v-col>
                <v-col cols="12" md="4"  style="text-align:center;">
                    <p style="margin-bottom:10px;">{{ $moment(picker).format('YY년 MM월 DD일') }} 오늘은</p>
                    <div v-if="daily.length >= 1">
                        <p style="margin-bottom:10px;">스피킹 {{ daily[0].image_speak_count }} 회</p>
                        <p style="margin-bottom:10px;">리스닝 {{ daily[0].listening_count }} 회</p>
                        <p style="margin-bottom:10px;">단어장 {{ daily[0].vocabulary_count }} 회</p>
                        <p>공부하셨습니다</p>
                    </div>
                    <div v-else style="text-align:center;">
                        <p>활동 내역이 없습니다</p>
                    </div>
                    <GChart
                        type="ColumnChart"
                        :data="chartData"
                        :options="chartOptions"
                    />
                </v-col>
            </v-row>
        </div>
        <Footer/>
    </div>
</template>

<script>
import http from '../util/http-common.js'
import Navbar from "../components/common/Navigation"
import Footer from "../components/common/footer"

import { GChart } from 'vue-google-charts'
import '@/assets/css/background.css'

export default {
    name: 'Attendance',

    components: {
        GChart,
        Navbar,
        Footer
    },
    data () {
        return {
            daily: '',
            month: '',
            picker: new Date().toISOString().substr(0, 10),
            day: '',
            chartData: [
                ['kinds', 'count'],
                ['Speaking', 0],
                ['Listening', 0],
                ['Wordbook', 0]
            ],
            chartOptions: {
                chart: {
                title: 'Today Study',
                }
            },
            speak: 0,
            listen: 0,
            voca: 0,
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
                if(this.daily.length > 0) {
                    this.chartData = [
                        ['kinds', 'count'],
                        ['Speaking', this.daily[0].image_speak_count],
                        ['Listening', this.daily[0].listening_count],
                        ['Wordbook', this.daily[0].vocabulary_count]
                    ]
                } else {
                    this.chartData = [
                        ['kinds', 'count'],
                        ['Speaking', 0],
                        ['Listening', 0],
                        ['Wordbook', 0]
                    ]
                }
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
    .bin{
        height: 70px;
    }
    @media(max-width: 480px){
        h1{
            font-size: 30px;
        }
    }
    .theme--light.v-card{
        background-color: lightblue;
    }
    .v-date-picker-table .v-btn.v-btn--active{
        color: black;
    }
    .v-date-picker-table__events > div{
        background-color: lightgreen;
    }
    .v-date-picker-table .v-btn{
        border: none;
    }
</style>