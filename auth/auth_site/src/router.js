import Vue from 'vue'
import Router from 'vue-router'
import SecureComponent from "./views/secure.vue"
import RegisterComponent from "./views/register.vue"

Vue.use(Router)

export default new Router({
  routes: [
    {
            path: '/',
            redirect: {
                name: "register"
            }
        },
        {
            path: "/register",
            name: "register",
            component: RegisterComponent
        },
        {
            path: "/secure",
            name: "secure",
            component: SecureComponent
        }
  ]
})
