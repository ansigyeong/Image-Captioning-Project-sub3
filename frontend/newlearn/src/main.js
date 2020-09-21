import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import VueCookies from 'vue-cookies'

import VueMoment from 'vue-moment'

Vue.use(VueMoment);

Vue.use(VueCookies)
Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
