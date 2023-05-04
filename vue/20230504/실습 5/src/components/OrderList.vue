<template>
  <div>
    <h1>주문내역</h1>
    <h3>{{totalOrderCount}} 건의 주문 내역</h3>
    <h3>총 {{totalOrderPrice}}원 결제 예정</h3>
    <OrderListItem v-for="order in orderList" :key="order.id"
      :order="order" />
    
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem.vue'

export default {
  name: 'OrderList',
  computed: {
    orderList () {
      return this.$store.state.orderList
    },
    totalOrderCount () {
      return this.$store.getters.totalOrderCount
    },
    totalOrderPrice() {
      return this.$store.getters.totalOrderPrice
    },
  },
  components: {
    OrderListItem
  }
}
</script>

<style>
</style>