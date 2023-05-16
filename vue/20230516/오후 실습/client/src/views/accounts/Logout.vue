<template>
  <div>
    <!-- <h3>username : <input type="text" v-model="username"></h3>
    <h3>password : <input type="text" v-model="password"></h3> -->
    
    <button @click="logout"> 로그아웃 하기 </button>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'Logout',
  props : {
    logOut : Boolean
  },
  data: function () {
    return {
      // username : null,
      // password : null,
    }
  },
  mounted() {
    if (this.logOut == false) {
      this.$router.push({name : 'Login'})
      // console.log(this.logOut)
    }
  },
  methods: {
    logout () {
        // console.log(this.logOut)
        console.log("logout")
        this.$emit('logout')
        
        

      
    }
  }
}
</script>
