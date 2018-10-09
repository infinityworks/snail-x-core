<template>
    <div id="login">
        <h3 class="page-title">Login</h3>
        <hr>
        <div class="form-group">
            <input class="form-control" type="text" name="username"
                   v-model="input.username" placeholder="Username"/>
            <input class="form-control" type="password" name="password"
                   v-model="input.password" placeholder="Password"/>
            <button style="float: right" class="btn btn-primary" type="button" v-on:click="Login()">Login</button>
            <button style="margin-right: 1em; float: right" type="button" class="btn btn-warning" onclick="window.history.back()">Back</button>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'Login',
        data() {
            return {
                input: {
                    username: "",
                    password: ""
                }
            }
        },
        methods: {
            login() {
                if (this.input.username !== "" && this.input.password !== "") {
                    if (this.input.username === this.$parent.mockAccount.username && this.input.password === this.$parent.mockAccount.password) {
                        this.$emit("authenticated", true);
                        this.$router.replace({name: "secure"});
                    } else {
                        console.log("The username and / or password is incorrect");
                    }
                } else {
                    console.log("A username and password must be present");
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