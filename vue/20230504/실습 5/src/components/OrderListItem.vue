<template>
<div>
  <li>
    <img :src="order.menu.image" alt="">
    {{order.menu.title}} 
    사이즈 : {{order.size.name}}
    가격 : {{totalPrice}}
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
      return this.order.menu.price + this.order.size.price
    },
  },
}
</script>

<style>
</style>