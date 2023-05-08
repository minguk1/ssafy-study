<template>
  <div class="bg-light rounded m-2">
    <h1>2. 사이즈를 고르세요.</h1>
    <SizeListItem v-for="size in sizeList" :key="size.id" :size="size"
    class="size-box" :class={sizeselect:size.selected} />
  </div>
</template>

<script>
import SizeListItem from '@/components/SizeListItem.vue'

export default {
  name: 'SizeList',
  methods: {
    onSelectMenu: function () {},
  },
  computed: {
    sizeList: function () {
      return this.$store.state.sizeList
    },
  },
  components : {
    SizeListItem
  }
}
</script>

<style>

.size-box:hover {
  background-color: yellow;
  color: white;
  cursor: pointer;
}

.sizeselect {
    background-color: green;
  }
</style>