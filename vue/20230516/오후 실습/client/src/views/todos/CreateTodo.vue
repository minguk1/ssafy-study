<template>
  <div>
    <input 
      type="text" 
      v-model.trim="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'
// const API_URL = " http://127.0.0.1:8000"

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    createTodo: function () {
      const jwtToken = localStorage.getItem('jwt')
      const Token = JSON.parse(jwtToken)
      console.log(Token)
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/todos/',
        data : { title : this.title},
        headers : {
          Authorization: `Bearer ${Token}`
        }
      })
      .then((res)=>{
        console.log(res)
        this.$router.push({name : 'TodoList'})

      })
      .catch((err)=>{
        console.log(err)
      })
      
    }
  }
}
</script>
