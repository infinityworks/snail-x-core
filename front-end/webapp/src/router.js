import Vue from 'vue'
import Router from 'vue-router'
import RegisterComponent from "./components/Register.vue"
import HomeComponent from "./components/Home.vue"
import LoginComponent from "./components/Login.vue"

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
