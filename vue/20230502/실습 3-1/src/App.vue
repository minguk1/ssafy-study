<template>
  <div id="app">
    <About></About>
    <Home></Home>
  </div>
</template>
<script>
import About from './views/About.vue';
import Home from './views/Home.vue';

export default {
    name: 'app',
    components : {
      About,
      Home,
    }
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

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

