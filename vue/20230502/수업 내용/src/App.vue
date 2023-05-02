<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <MovieComponent title=" 범죄도시3" description="마동석짱"> </MovieComponent>
    <MovieComponent title=" 아바타" description="자연"> </MovieComponent>
    <MovieComponent title=" 범죄도시3" description="마동석짱"> </MovieComponent>
    <MovieComponent title=" 범죄도시3" description="마동석짱"> </MovieComponent>
    <MovieComponent title=" 범죄도시3" description="마동석짱"> </MovieComponent>
    <MovieComponent title=" 범죄도시3" description="마동석짱"> </MovieComponent>
    <button class="btn btn-primary">버튼</button>
  </div>
</template>

<script>

import MovieComponent from './components/MovieComponent.vue'

export default {
  name: 'App',
  components: {
    MovieComponent
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
  margin-top: 60px;
}
</style>
