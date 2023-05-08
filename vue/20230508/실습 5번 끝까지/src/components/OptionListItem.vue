<template>
  <div class="d-flex justify-content-between 
  align-items-center mx-5 border border-success rounded-2">
    <div>
    {{option.name}}
    </div>
    <div>
      {{option.price}}
    </div>
    <div>
      <button @click="decrease">-</button>
      {{option.count}}
      <button @click="increase">+</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  methods: {
    increase() {
      this.$store.commit('increase_count', this.option.name)
    },
    decrease() {
      this.$store.commit('decrease_count', this.option.name)
    },
  },
}
</script>

<style>
</style>