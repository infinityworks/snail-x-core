<template>
    <div id="login">
        <h3 class="page-title">Login</h3>
        <hr>
        <form action="#" @submit.prevent="login">>
            <input class="form-control" type="text" name="username"
                   v-model="input.username" placeholder="Username"/>
            <input class="form-control" type="password" name="password"
                   v-model="input.password" placeholder="Password"/>
            <button style="float: right" class="btn btn-primary" type="button" v-on:click="login()">Login</button>
            <button style="margin-right: 1em; float: right" type="button" class="btn btn-warning" onclick="window.history.back()">Back</button>
        </form>
    </div>
</template>

<script>

    export default {
        name: 'Login',
        data() {
            return {
                username: "",
                password: ""
            }
        },
        methods: {
            methods: {
                login() {
                  this.$store.dispatch('loginUser', {
                    username: this.username,
                    password: this.password,
                  })
                    .then(response => {
                      this.$router.push({ name: 'home' })
                    })
                }
              }
        }
    }
</script>

<style scoped>
    #login {
        position: fixed;
        left: 24.5%;
        top: 15%;
        width: 50%;
        border: 1px solid grey;
        background-color: white;
        margin: 200px auto auto;
        padding: 20px;
    }

    input {
        margin-bottom: 1em;
    }
</style>