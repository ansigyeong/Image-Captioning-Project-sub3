import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import VueCookies from 'vue-cookies'

import VueMoment from 'vue-moment'

// 뷰-구글 차트
import VueGoogleCharts from 'vue-google-charts'

// import axios from 'axios'

// 뷰 오디오 레코더 패키지
import AudioRecorder from 'vue-audio-recorder'

Vue.use(AudioRecorder)

Vue.use(VueMoment);

Vue.use(VueCookies)
Vue.config.productionTip = false

Vue.use(VueGoogleCharts)

// axios.defaults.headers.post['Access-Control-Allow-Origin'] = 'http://localhost:8080/'

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
