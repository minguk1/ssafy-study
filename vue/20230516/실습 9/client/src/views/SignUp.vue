<template>
  <b-container role="group" class="p-5 login-form">
    <h1>회원가입</h1>
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

        <label for="input-password1">비밀번호</label>
        <b-form-input id="input-password1" placeholder="PASSWORD" v-model="password1"
        trim type="password" :state="passwordState1" aria-describedby=" input-live-feedback"></b-form-input>
        <b-form-invalid-feedback id="input-password1-feedback" class="text-right">
            비밀번호 5글자 이상
        </b-form-invalid-feedback>
    </b-row>
    <b-row>

        <label for="input-password2">비밀번호</label>
        <b-form-input id="input-password2" placeholder="PASSWORD확인" v-model="password2"
        trim type="password" :state="passwordState2" aria-describedby=" input-live-feedback"></b-form-input>
        <b-form-invalid-feedback id="input-password2-feedback" class="text-right">
            비밀번호 5글자 이상
        </b-form-invalid-feedback>
    </b-row>

    <b-row>

        <label for="input-email">이메일</label>
        <b-form-input id="input-email" placeholder="E-mail" v-model="email"
        trim :state="emailState" aria-describedby=" input-live-feedback"></b-form-input>
        <b-form-invalid-feedback id="input-password2-feedback" class="text-right">
            이메일 형식에 맞추세요.
        </b-form-invalid-feedback>
    </b-row>
    <b-button variant="success" @click="signup">회원가입</b-button>


  </b-container>
</template>

<script>
import axios from 'axios'

export default {
    data () {
        return{
            username : "",
            password1 : "",
            password2 : "",
            email : "",
        }
    },
    computed : {
        nameState () {
            return this.username.length >= 3 ? true : false
        },
        passwordState1 () {
            return this.password1.length >= 5 ? true : false
        },
        passwordState2 () {
            return this.password2.length >= 5 ? true : false
        },
        emailState () {
            return this.email.includes("@") ? true : false
        },
    },
    methods : {
        signup() {
            

            
            console.log(this.email)
            axios({
                method : 'post',
                url : 'http://127.0.0.1:8000/auth/signup/',
                data : {
                    username : this.username, password1 : this.password1, password2: this.password2
                }
            })
            .then((res) => {
                console.log(res.data)
                this.$store.dispatch('signUp', res.data)
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