<template>
  <div >
    <h1>1. 음료를 고르세요.</h1>
    
    <MenuListItem v-for="menu in menuList" :key="menu.id" 
    :menu="menu"  class="menu-box" :class={menuselect:menu.selected}  />
    
  </div>
</template>

<script>
import MenuListItem from '@/components/MenuListItem.vue'

export default {
  name: 'MenuList',
  components: {
    MenuListItem
  },
  computed: {
    menuList () {
      return this.$store.state.menuList
    },
  },
  methods: {
    
  },
}
</script>

<style>
  

  
.menu-box:hover {
  background-color: yellow;
  color: white;
  cursor: pointer;
}

.menuselect {
    background-color: green;
    color : white;
  }

</style>