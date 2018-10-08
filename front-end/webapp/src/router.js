import Vue from 'vue'
import Router from 'vue-router'
import RegisterComponent from "./views/register.vue"
import IndexComponent from "./views/Index.vue"

Vue.use(Router);

export default new Router({
  routes: [
    {
            path: '/',
            name: "index",
            component: IndexComponent
        },
        {
            path: "/register",
            name: "register",
            component: RegisterComponent
        }
  ]
})
