
<template>
    <div id="app">
        <div id="nav">
          <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
            <router-link v-if="authenticated" to="/login" v-on:click.native="logout()" replace>Logout</router-link>
        </div>
        <router-view @authenticated="setAuthenticated" />
    </div>
</template>

<script>
    export default {
        name: 'App',
        data() {
            return {
                authenticated: false,
                mockAccount: {
                    username: "James",
                    password: "password"
                }
            }
        },
        mounted() {
            if(!this.authenticated) {
                this.$router.replace({ name: "register" });
            }
        },
        methods: {
            setAuthenticated(status) {
                this.authenticated = status;
            },
            logout() {
                this.authenticated = false;
            }
        }
    }
</script>

<style>
    body {
        background-color: #F0F0F0;
    }
    h1 {
        padding: 0;
        margin-top: 0;
    }
    #app {
        width: 1024px;
        margin: auto;
    }
</style>
