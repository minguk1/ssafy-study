<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <child-component name="임준환" @money="giveMoney"></child-component>
    <child-component-2></child-component-2>
  </div>
</template>

<script>
import childComponent from './components/childComponent.vue'
import childComponent2 from './components/childComponent2.vue'


export default {
  name: 'App',
  components: {
    childComponent,
    childComponent2,
  },
  methods : {
    giveMoney(money) {
      alert(`용돈 ${money}원`)
    }
  },
  created() {
    console.log('App Created')

  },
  mounted() {
    console.log('App mounted')
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
  margin-top: 60px;
}
</style>
