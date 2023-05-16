<template>
  <b-container role="group" class="p-5 login-form">
    <h1>로그인</h1>
    <b-row>

        <label for="input-username">아이디</label>
        <b-form-input id="input-username" placeholder="ID" v-model="username"
        trim :state="nameState" aria-describedby=" input-live-feedback"
        ></b-form-input>
        <b-form-invalid-feedback id="input-username-feedback" class="text-right">
            알파벳/숫자 3글자 이상
        </b-form-invalid-feedback>
    </b-row>
    <b-row>

        <label for="input-password">비밀번호</label>
        <b-form-input id="input-password" placeholder="PASSWORD" v-model="password"
        trim type="password" :state="passwordState" aria-describedby=" input-live-feedback"></b-form-input>
        <b-form-invalid-feedback id="input-password-feedback" class="text-right">
            비밀번호 5글자 이상
        </b-form-invalid-feedback>
    </b-row>
    <b-button variant="success" @click="login">로그인</b-button>


  </b-container>
</template>

<script>
import axios from 'axios'

export default {
    data () {
        return{
            username : "",
            password : "",
        }
    },
    computed : {
        nameState () {
            return this.username.length >= 3 ? true : false
        },
        passwordState () {
            return this.password.length >= 5 ? true : false
        },
    },
    methods : {
        login() {
           
            axios({
                
                method : 'post',
                url : 'http://127.0.0.1:8000/auth/login/',
                data : {
                    username : this.username, password : this.password
                }
            })
            .then((res) => {
                console.log(res.data)
                this.$store.dispatch('login', res.data)
            })
            .catch((err) => {
                console.log(err)
            })
        }
    }
}
</script>

<style>
.login-form {
    background-color: rgb(214, 228, 240);
    
}
</style>