<template>
<div>
  <h1>SideBar</h1>

    <nav>
      <router-link :to="{name : 'all'}" class="border ">모든</router-link> <br>
      <router-link :to="{name : 'today'}" class="border">오늘</router-link> <br>
      <router-link :to="{name : 'important'}" class="border">중요</router-link>
    </nav>
    
</div>
</template>

<script>
export default {
    
}
</script>

<style>

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