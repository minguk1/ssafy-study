<template>
  <div id="app">
    <div id="nav">
      <span>
        <router-link :to="{ name: 'TodoList' }">Todo List</router-link> | 
        <router-link :to="{ name: 'CreateTodo' }">Create Todo</router-link> |
      </span>
      <span>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> |
        <router-link :to="{ name: 'Logout' }">Logout</router-link>
      </span>
    </div>
    <router-view @login="login_true" :log-out="isLogin" @logout="logout" />
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin : false,
    }
  },
  methods: {
    login_true () {
      this.isLogin = true
      console.log("successfully logged in")
      console.log(this.isLogin)
    },
    logout() {
        localStorage.removeItem('jwt')
        this.isLogin = false
        console.log(this.isLogin)
      
      
    }
  },
  created() {
    if (localStorage.getItem('jwt')) {
      this.isLogin = true
      
      console.log("token is here")
      console.log(this.isLogin)
    }
    else {
      this.isLogin = false
      console.log("token is not")
    }
    
  },

}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
