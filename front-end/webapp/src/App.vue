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
                <li>
                    <router-link to="/" class="nav-link">Home</router-link>
                </li>
                <li>
                    <router-link to="/" class="nav-link">Enter</router-link>
                </li>
                <li>
                    <router-link to="/" class="nav-link">Results</router-link>
                </li>
                <li>
                    <router-link to="/" class="nav-link">Leaderboards</router-link>
                </li>
                <li v-if="!loggedIn">
                    <router-link to="/login" class="nav-link">Login</router-link>
                </li>
                <li v-if="!loggedIn">
                    <router-link to="/register" class="nav-link">Register</router-link>
                </li>
                <li v-if="loggedIn">
                    <router-link v-if="authenticated" to="/logout" @click.native="logout()">Logout
                    </router-link>
                </li>
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
            }
        },
        mounted() {
            if (!this.authenticated) {
                this.$router.replace({name: "Register.vue"});
            }
        },
        computed: {
            loggedIn() {
                return this.$store.getters.loggedIn
            },
            user() {
                return this.$store.getters.userEmail
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

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2c3e50;
        font-size: 24px;
        height: 100vh;
    }

    .nav {
        display: flex;
        padding: 15px 0;
        justify-content: flex-end;
        margin: 0 0 24px;
        flex-wrap: nowrap !important;
        list-style: none;
    }

    .nav a {
        color: #636b6f;
        padding: 0 25px;
        font-size: 14px;
        font-weight: 800;
        letter-spacing: .1rem;
        text-decoration: none;
        text-transform: uppercase;
    }

    .nav a:hover {
        color: green;
    }

    .btn {
        letter-spacing: .1rem;
        text-decoration: none;
        text-transform: lowercase;
    }

    .container {
        max-width: 60%;
    }

    .navigation-bar {
        background-color: whitesmoke;
        border-top: 1px grey solid;
        border-bottom: 1px grey solid;
        position: fixed;
        left: 27.5%;
        top: 26%;
        padding-left: 1em;
        margin-bottom: 1em;
        width: 750px;
    }

    body {
        width: 1024px;
        background-image: url("https://3c1703fe8d.site.internapcdn.net/newman/gfx/news/hires/2014/1-newstaugusti.jpg");

    }

    #app {
        width: 1024px;
        margin: auto;
        position: center;
    }

    #snail-logo {
        top: 4%;
        left: 40%;
        position: fixed;
        height: 20%;
        width: 18%;
    }

    .page-title {
        font-weight: bold;
        color: grey;
        padding: 0;
        margin-top: 0;

    }
</style>
