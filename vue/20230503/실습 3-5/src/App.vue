<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model='app_input'>
    
    <h3>parentData : {{parent_input}}</h3>
    <h3>childData : {{child_input}}</h3>
    <div>
    <app-parent
      :send-to-parent="{app_input,}"
      @send-to-app="getFromParent"
    />
    </div>
  </div>
</template>

<script>
import AppParent from './components/Appparent.vue'


export default {
  name: 'App',
  components: {
    AppParent,
  },
  data : function () {
    return {
      app_input : '',
      parent_input : '',
      child_input : '',
    }
  },
  methods : {
    getFromParent (child_input, parent_input) {
      this.parent_input = parent_input
      this.child_input = child_input
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
  margin-top: 60px;
}
</style>
