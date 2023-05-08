<template>
  <div @click="selectMenu()" class="d-flex justify-content-between 
  align-items-center mx-5 border border-success rounded-2">
    <img :src="menu.image" alt="">
    <div>
    {{menu.title}}
    </div>
    <div>
    {{menu.price}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },

  methods: {
    selectMenu () {
      console.log(this.menu)
      this.$store.commit('updateMenuList', this.menu )
    },
  },
}
</script>

<style>
img {
 height : 100px;
 width : 100px; 
}


</style>