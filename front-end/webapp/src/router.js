import Vue from 'vue'
import Router from 'vue-router'
import RegisterComponent from "./components/auth/Register.vue"
import HomeComponent from "./components/Home.vue"
import LoginComponent from "./components/auth/Login.vue"

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
