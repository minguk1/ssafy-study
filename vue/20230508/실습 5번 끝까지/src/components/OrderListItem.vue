<template>
<div class="d-flex justify-content-between 
  align-items-center mx-5 border border-success rounded-2">
  <li class=" justify-content-between">
    <img :src="order.menu.image" alt="">
    {{order.menu.title}} /
    사이즈 : {{order.size.name}} /
    가격 : {{totalPrice}}원 /
    
    <!-- {{order.state}} -->
    <span v-for="opt in order.option" :key="opt.id">{{opt.name}} {{opt.count}}회,     </span>
  </li>
  </div>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    totalPrice() {
      let optionprice = 0
      this.order.option.forEach( opt => {
        optionprice += opt.price*opt.count
      })
      return optionprice + this.order.menu.price + this.order.size.price
    },
  },
}
</script>

<style>
</style>