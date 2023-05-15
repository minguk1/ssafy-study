<template>
  <div>
    <h3>username : <input type="text" v-model="username"></h3>
    <h3>password : <input type="text" v-model="password"></h3>
    
    <button @click="login"> 입력 완료 </button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      username : null,
      password : null,
    }
  },
  methods: {
    login: function () {
      axios({
        method : 'post',
        url : 'http://127.0.0.1:8000/accounts/',
        data : {username : this.username, password : this.password}
      })
      .then((res) => {
        console.log(res)
        // this.userinformations.push(res.data)
        // this.$router.push({name : 'Login'})
        
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>
