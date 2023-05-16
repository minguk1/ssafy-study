<template>
  <div>
    <h3>username : <input type="text" v-model="usermodel"></h3>
    <h3>password1 : <input type="text" v-model="password1"></h3>
    <h3>password2 : <input type="text" v-model="password2"></h3>
    <button @click="signup"> 입력 완료 </button>
  </div>
</template>
  
<script>
import axios from 'axios'

export default {
  name: 'Singup',
  data: function () {
    return {
      userinformations :[],
      usermodel : null,
      password1 : null,
      password2 : null,
    }
  },
  methods: {
    signup: function () {
      axios({
        method : 'post',
        url : 'http://127.0.0.1:8000/accounts/signup/',
        data : {username : this.usermodel, password1 : this.password1, password2 : this.password2}
      })
      .then((res) => {
        console.log(res)
        this.userinformations.push(res.data)
        this.$router.push({name : 'Login'})
        
      })
      .catch((err) => {
        console.log(err)
      })
      
    }
  }
}
</script>
