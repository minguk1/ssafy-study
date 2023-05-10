<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <nav>
      <router-link to="/">Home</router-link> | 
      <router-link :to="{name : 'happeed'}">Start</router-link>
    </nav>
    <router-view/>
  </div>
</template>
<script>
export default {
  
}
</script>
<style>
#app {
  display : flex;
  flex-direction: column;
  align-items: center;
  width: 700px;
}


nav {

}

nav a {
  
}

nav a.router-link-exact-active {
  
}
</style>
