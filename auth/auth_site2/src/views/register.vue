<template>
    <div id="login">
        <form
          id="reg"
          @submit="checkForm"
          action="register()"
          method="post"
          novalidate="true"
        >
        <center>
        <h1>Register</h1>
            <hr>
        <div class="form-group">
            <input type="text" class="form-control" name="fistName" v-model="input.firstName" placeholder="First Name" />
            <br>
            <input type="text" class="form-control" name="lastName" v-model="input.lastName" placeholder="Last Name" />
            <br>
            <input type="email" class="form-control" name="email" v-model="input.email" placeholder="Email" /><br>
            <input type="password" class="form-control" name="password" v-model="input.password" placeholder="Password" />
            <br>
            <button type="button" class="btn btn-dark" v-on:click="register()">Register</button>
        </div>
        </center>
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
                    username: "",
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
                var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                return re.test(email);
            },


            register() {
                var post_data = this.input;
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
    #login {
        width: 600px;
        border: 1px solid #CCCCCC;
        background-color: #FFFFFF;
        margin: auto;
        margin-top: 100px;
        padding: 20px;
    }
</style>
