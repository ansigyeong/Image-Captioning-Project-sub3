import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import VueCookies from 'vue-cookies'
import VueMoment from 'vue-moment'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// 뷰 오디오 레코더 패키지
import AudioRecorder from 'vue-audio-recorder'
Vue.use(BootstrapVue)
Vue.use(AudioRecorder)
Vue.use(VueMoment);
Vue.use(VueCookies)
Vue.config.productionTip = false

// axios.defaults.headers.post['Access-Control-Allow-Origin'] = 'http://localhost:8080/'

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
