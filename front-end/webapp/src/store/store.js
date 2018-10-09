import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        user: localStorage.getItem('user_email') || null,
    },
    getters: {
        loggedIn(state) {
            return state.user !== null
        },
        userEmail(state) {
            return state.user
        }
    },
    actions: {
        loginUser(context, credentials) {
            return new Promise((resolve, reject) => {
                axios.post('http://127.0.0.1:5000/login-user', {
                    username: credentials.username,
                    password: credentials.password,
                })
                    .then(response => {
                        const user_email = response.data;
                        localStorage.setItem('user_email', user_email);
                        context.commit('loginUser', user_email);
                        resolve(response);
                    })
                    .catch(error => {
                        console.log(error);
                        reject(error);
                    })
            })
        }
    }
});