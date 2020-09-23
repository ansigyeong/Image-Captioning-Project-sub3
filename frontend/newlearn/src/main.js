import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import store from './store'
import router from './router'
import VueCookies from 'vue-cookies'

import VueMoment from 'vue-moment'

// import axios from 'axios'

// 뷰 오디오 레코더 패키지
import AudioRecorder from 'vue-audio-recorder'

Vue.use(AudioRecorder)

Vue.use(VueMoment);

Vue.use(VueCookies)
Vue.config.productionTip = false

// axios.defaults.headers.post['Access-Control-Allow-Origin'] = 'http://localhost:8080/'

new Vue({
  vuetify,
  store,
  router,
  render: h => h(App)
}).$mount('#app')
