<template>
    <div id="login">
        <h1>Register</h1>
        <input type="text" name="fistName" v-model="input.firstName" placeholder="First Name" /><br>
        <input type="text" name="lastName" v-model="input.lastName" placeholder="Last Name" /><br>
        <input type="text" name="username" v-model="input.username" placeholder="Username" /><br>
        <input type="email" name="email" v-model="input.email" placeholder="Email" /><br>
        <input type="password" name="password" v-model="input.password" placeholder="Password" /><br>
        <button type="button" v-on:click="register()">Register</button>
    </div>
</template>

<script>
    export default {
        name: 'Register',
        data() {
            return {
                input: {
                    firstName: "",
                    lastName: "",
                    username: "",
                    email: "",
                    password: ""
                }
            }
        },

        methods: {
            register() {
                    var post_data = this.input;
                    console.log(post_data);
                    const requestOptions = {
                       method: 'POST',
                       headers: { 'Content-Type': 'application/json' },
                       body: JSON.stringify(post_data)
                   };

                    this.$http.post('http://127.0.0.1:5000/register-user', post_data).then(function () {
                        alert("WORKS");
                  });

            }
        }
    }
</script>

<style scoped>
    #login {
        width: 500px;
        border: 1px solid #CCCCCC;
        background-color: #FFFFFF;
        margin: auto;
        margin-top: 200px;
        padding: 20px;
    }
</style>