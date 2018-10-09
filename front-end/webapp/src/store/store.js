import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        user: null,
    },
    getters: {
        loggedIn(state) {
            return state.user !== null
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
                        console.log(user_email);
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