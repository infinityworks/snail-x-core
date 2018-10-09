import Vue from 'vue'
import Router from 'vue-router'
import RegisterComponent from "./views/Register.vue"
import HomeComponent from "./views/Home.vue"
import LoginComponent from "./views/Login.vue"

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: "home",
            component: HomeComponent
        },
        {
            path: '/login',
            name: "login",
            component: LoginComponent
        },
        {
            path: "/register",
            name: "Register.vue",
            component: RegisterComponent
        }
    ]
})
