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
    }
});