
<template>
    <div id="app">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <div class="navbar navbar-light bg-light" id="nav">
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <h3>SNAIL RACING</h3>
                <router-link to="/register" class="nav-link">Register</router-link>
            <router-link v-if="authenticated" to="/login" v-on:click.native="logout()" replace>Logout</router-link>
            </nav>
        </div>
        <div>
            <center>
              <img style="position: absolute; height: 85px; width: 145px; padding-top: 10px;" src="https://banner2.kisspng.com/20180225/avw/kisspng-escargot-sea-snail-clip-art-brown-cartoon-snail-5a92648eaab006.4875330315195434386992.jpg"/>
            </center>
        </div>

        <div id="sidebanner">
            <img style="padding-top:100px; padding-left: 1000px; position: absolute" src="http://www.shakeout.org/2008/downloads/ShakeOut_BannerAds_GetReady_160x600_v8.gif">
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
    }
</style>
