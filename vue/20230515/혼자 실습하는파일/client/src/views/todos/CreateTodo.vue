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
const API_URL = " http://127.0.0.1:8000"

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    createTodo: function () {
      axios({
        method : 'post',
        url : `${API_URL}/todos/`,
        data : {title : this.title, iscompleted : false}

      })
      .then((res)=>{
        console.log(res)
        this.$router.push({name : 'TodoList'})

      })
      
    }
  }
}
</script>
