import Vue from 'vue'
import App from './App.vue'
import router from './router'
import {store} from './store/store'
import VueResource from "vue-resource"
import Vuex from 'vuex'
import 'es6-promise/auto'


Vue.use(Vuex);

Vue.config.productionTip = false;
Vue.use(VueResource);

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresVisitor)) {
        if (this.$store.getters.loggedIn) {
            next({
                name: 'home',
            })
        } else {
            next()
        }
    } else {
        next()
    }
});

new Vue({
    router,
    store: store,
    render: h => h(App)
}).$mount('#app');
