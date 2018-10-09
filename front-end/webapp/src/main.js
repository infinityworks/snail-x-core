import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Master from './components/layouts/Master'
import { store } from './store/store'
import VueResource from "vue-resource"
import Vuex from 'vuex'
import 'es6-promise/auto'


Vue.use(Vuex);

Vue.config.productionTip = false;
Vue.use(VueResource);

new Vue({
    router,
    store: store,
    components: {Master},
    template: '<Master/>',
    render: h => h(App)
}).$mount('#app');
