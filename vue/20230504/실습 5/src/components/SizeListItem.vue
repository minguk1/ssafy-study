<template>
  <div @click="selectSize()" class="d-flex justify-content-between 
  align-items-center mx-5 border border-success rounded-2 ">
    {{size.name}}
    {{size.price}}
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods : {
    selectSize () {
      this.$store.commit('updateSizeList', this.size)
    }
  },


}

</script>

<style>
</style>