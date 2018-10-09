<template>
    <div id="app" class="container">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
              integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
              crossorigin="anonymous">
        <div>
            <img id="snail-logo"
                 src="https://banner2.kisspng.com/20180225/avw/kisspng-escargot-sea-snail-clip-art-brown-cartoon-snail-5a92648eaab006.4875330315195434386992.jpg"/>
        </div>

        <div class="navigation-bar" id="navbar">
            <ul class="nav">
                <li><router-link to="/" class="nav-link">Home</router-link></li>
                <li><router-link to="/" class="nav-link">Enter</router-link></li>
                <li><router-link to="/" class="nav-link">Results</router-link></li>
                <li><router-link to="/" class="nav-link">Leaderboards</router-link></li>
                <li><router-link to="/login" class="nav-link">Login</router-link></li>
                <li><router-link to="/register" class="nav-link">Register</router-link></li>
                <li><router-link v-if="authenticated" to="/login" v-on:click.native="logout()" replace>Logout</router-link></li>
            </ul>
        </div>

        <div id="sidebanner"></div>
        <router-view @authenticated="setAuthenticated"/>
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
            if (!this.authenticated) {
                this.$router.replace({name: "Register.vue"});
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

    .container {
        max-width: 60%;
    }

    .navigation-bar {
        background-color: whitesmoke;
        border: 1px grey solid;
        width: 50%;
        position: fixed;
        left: 24.5%;
        top: 28%;
        padding-left: 1em;
        margin-bottom: 1em;
    }

    body {
        width: 1024px;
        background-image: url("https://3c1703fe8d.site.internapcdn.net/newman/gfx/news/hires/2014/1-newstaugusti.jpg");

    }

    h1 {
        padding: 0;
        margin-top: 0;
    }

    #app {
        width: 1024px;
        margin: auto;
        position: center;
    }

    #snail-logo {
        top: 5%;
        left: 40%;
        position: fixed;
        height: 20%;
        width: 18%;
    }

    li {
        font-weight: bold;
    }
</style>
