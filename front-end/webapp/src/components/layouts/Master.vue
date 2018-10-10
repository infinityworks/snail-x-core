<template>
    <div id="app">
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
                <li>
                    <router-link to="/login" class="nav-link">Login</router-link>
                </li>
                <li>
                    <router-link to="/register" class="nav-link">Register</router-link>
                </li>
                <li>
                    <router-link v-if="authenticated" to="/login" v-on:click.native="logout()" replace>Logout
                    </router-link>
                </li>
            </ul>
        </div>

        <router-view></router-view>
    </div>
</template>

<script>
    export default {
        name: "Master"
    }
</script>

<style scoped>

</style>