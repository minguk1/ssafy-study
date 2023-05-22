<template>
  <div class="container">
    <br>
    <b-container class="p-5 signup-form w-50">
      <h1>회원가입</h1>
      <br>
      <b-row>
        <label for="id-input">아이디</label>
        <b-form-input 
        id="id-input" 
        v-model="username" 
        :state="usernameState" 
        aria-describedby="input-live-help input-live-feedback" 
        placeholder="아이디를 입력하세요."
        style="font-family: Arial, Helvetica, sans-serif;" 
        trim></b-form-input>
  
        <b-form-invalid-feedback id="id-input-feedback" class="text-right">아이디는 네 글자 이상</b-form-invalid-feedback>
      </b-row>
      <br>
      <b-row>
        <label for="pw-input">비밀번호</label>
        <b-form-input 
        id="pw-input" 
        v-model="password" 
        :state="passwordState" 
        aria-describedby="input-live-help input-live-feedback" 
        placeholder="비밀번호를 입력하세요."
        type="password"
        style="font-family: Arial, Helvetica, sans-serif;" 
        trim></b-form-input>
  
        <b-form-invalid-feedback id="pw-input-feedback" class="text-right">비밀번호는 여덟 글자 이상</b-form-invalid-feedback>
      </b-row>
      <br>
      <b-row>
        <label for="pwconfirm-input">비밀번호 확인</label>
        <b-form-input 
        id="pwconfirm-input" 
        v-model="passwordconfirm" 
        :state="passwordconfirmState" 
        aria-describedby="input-live-help input-live-feedback" 
        placeholder="비밀번호를 입력하세요."
        type="password"
        style="font-family: Arial, Helvetica, sans-serif;" 
        trim></b-form-input>
  
        <b-form-invalid-feedback id="pwconfirm-input-feedback" class="text-right">비밀번호가 일치하지 않습니다.</b-form-invalid-feedback>
      </b-row>
      <br>
      <b-button @click="signup">회원가입</b-button>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'

const URL = "http://127.0.0.1:8000/auth/signup/"

export default {
  name: "SignupView",
  data() {
    return {
      username: "",
      password: "",
      passwordconfirm: ""
    }
  },
  computed: {
    usernameState() {
      return this.username.length >= 4 ? true : false
    },
    passwordState() {
      return this.password.length >= 8 ? true : false
    },
    passwordconfirmState() {
      return this.password === this.passwordconfirm && this.passwordconfirm.length >= 8 ? true : false
    }
  },
  methods: {
    signup() {
      axios({
        method: "POST",
        url: URL,
        data: {
          username: this.username,
          password1: this.password,
          password2: this.passwordconfirm
        }
      })
      .then((res)=>{
        console.log(res.data)
        this.$store.dispatch('signupLogin', res.data)
        this.$router.push({name:"home"})
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }
}
</script>

<style>
.text-right {
  text-align: right;
}

</style>