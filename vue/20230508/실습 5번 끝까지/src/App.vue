<template>
  <div id="app" class="bg-secondary">
    <h1>Coffee Order App</h1>
    <div class="d-flex">
      <MenuList class="col-4"/>
      <SizeList class="col-4"/>
      <OptionList class="col-4"/>
    </div>
    <div class="d-flex align-items-center" >
    <button @click="addToCart" class="btn btn-primary">장바구니 담기</button>
    </div>
    <div>
      <OrderList/>
    </div>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList.vue'
import SizeList from '@/components/SizeList.vue'
import OrderList from '@/components/OrderList.vue'
import OptionList from '@/components/OptionList.vue'


export default {
  name: 'App',
  components : {
    MenuList,
    SizeList,
    OrderList,
    OptionList,
  },
  methods : {
    addToCart () {
      this.$store.commit('addOrder')
    }
  },
  mounted () {
    this.$store.commit('storage')
    console.log(this.$store.state.orderList)
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
