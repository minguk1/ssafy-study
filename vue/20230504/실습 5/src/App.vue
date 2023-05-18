<template>
  <div id="app" >
    <h1>Coffee Order App</h1>
    <img src="assets/logo.png" alt="">
    <img src="assets/무민.png" alt="">
    <div class="d-flex">
      <MenuList class="col-6"/>
      <SizeList class="col-6"/>
    </div>
    <button @click="addToCart">장바구니 담기</button>
    <div>
      <OrderList/>
    </div>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList.vue'
import SizeList from '@/components/SizeList.vue'
import OrderList from '@/components/OrderList.vue'


export default {
  name: 'App',
  components : {
    MenuList,
    SizeList,
    OrderList,
  },
  methods : {
    addToCart () {
      this.$store.commit('addOrder')
    }
  },




}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}
</style>
