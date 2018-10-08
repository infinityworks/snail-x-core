import Vue from 'vue'
import Router from 'vue-router'
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
        }
  ]
})
