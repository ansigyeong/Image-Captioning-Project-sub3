<template>
    <div class="container" style="text-align:center;">
        <h1>💻 Points 💻</h1>
        <br>
        <br>
        <h3>Total Points {{ totalPoint }}</h3>
        <v-row>
            <v-col cols="3">구분</v-col>
            <v-col cols="3">점수</v-col>
            <v-col cols="3">내용</v-col>
            <v-col cols="3">날짜</v-col>
        </v-row>
        <hr>
        <div v-for="(list) in pointList" :key="list.pid">
            <v-row>
                <v-col cols="3" v-if="list.use_type">적립</v-col>
                <v-col cols="3" v-else>사용</v-col>
                <v-col cols="3">{{ list.value }}</v-col>
                <v-col cols="3">{{ list.content }}</v-col>
                <v-col cols="3">{{ $moment(list.date).format('YYYY-MM-DD HH:mm') }}</v-col>
            </v-row>
        </div>
    </div>
</template>

<script>
import http from '../util/http-common.js'

export default {
    components: {
    },
    data () {
        return {
            totalPoint: 0,
            pointList: [],
        }
    },
    created() {
        this.getPoints()
    },
    methods: {
        getPoints() {
            const config = {
                headers: {
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            }
            // 테스트용으로 '2번' 유저에 대해 요청을 보냄.
            // 연동 완료 시 요청보내는 유저로 보낼 것
            http.get(`/accounts/point/list/`, config)
            .then(res => {
                this.totalPoint = res.data.total_points
                this.pointList = res.data.point_list
            })
        }
    }
}
</script>

<style>

</style>