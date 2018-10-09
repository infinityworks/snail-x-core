<template>
    <div id="register">
        <form id="reg"
              @submit="checkForm"
              action="register()"
              method="post"
              novalidate="true">

            <h1>Register</h1>
            <hr>
            <div class="form-group">
                <input type="text" class="form-control" name="firstName" v-model="input.firstName"
                       placeholder="First Name"/>
                <br>
                <input type="text" class="form-control" name="lastName" v-model="input.lastName"
                       placeholder="Last Name"/>
                <br>
                <input type="email" class="form-control" name="email" v-model="input.email"
                       placeholder="Email"/><br>
                <input type="password" class="form-control" name="password" v-model="input.password"
                       placeholder="Password"/>
                <br>
                <button style="float: right;" type="button" class="btn btn-success" v-on:click="register()">Register</button>
                <button style="margin-right: 1em; float: right" type="button" class="btn btn-warning" onclick="window.history.back()">Back</button>
            </div>
        </form>
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
                    email: "",
                    password: ""
                }
            }
        },

        methods: {

            checkForm: function (e) {
                this.errors = [];

                if (!this.name) {
                    this.errors.push("Name required.");
                }
                if (!this.email) {
                    this.errors.push('Email required.');
                } else if (!this.validEmail(this.email)) {
                    this.errors.push('Valid email required.');
                }

                if (!this.errors.length) {
                    return true;
                }

                e.preventDefault();
            },
            validEmail: function (email) {
                const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                return re.test(email);
            },

            register() {
                let post_data = this.input;
                console.log(post_data);
                const requestOptions = {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
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
    #register {
        position:fixed;
        top: 18%;
        left: 15%;
        width: 50%;
        border: 1px solid #CCCCCC;
        background-color: #FFFFFF;
        margin: 10em;
        padding: 20px;
    }
</style>