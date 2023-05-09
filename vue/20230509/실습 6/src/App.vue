<template>
  <div id="app" class="d-flex justify-content-between">
    <div class='col-4 '><SideBar/></div>
    <div class='col-6'><router-view/></div>
    
  </div>
</template>

<script>
import SideBar from '@/components/SideBar'

export default {
  components : {
    SideBar,
  },
  // mounted () {
  //   this.$store.commit('storage')
  //   console.log(this.$store.state.orderList)
  // },
  
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


</style>
