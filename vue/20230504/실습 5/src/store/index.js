import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {  title : '아메리카노',
        price : 4500,
        selected : false,
        image : 'https://source.unsplash.com/featured/?americano',
      },
      {  title : '카페라떼',
        price : 5000,
        selected : false,
        image : 'https://source.unsplash.com/featured/?cafelatte',
      },
      {  title : '아이스티',
        price : 3000,
        selected : false,
        image : 'https://source.unsplash.com/featured/?icetea',
      },
    ],
    sizeList: [
      {  name : 'small',
        price : 500,
        selected : false,
      },
      {  name : 'tall',
        price : 1000,
        selected : false,
      },
      {  name : 'grande',
        price : 1500,
        selected : false,
      },
      
    ],
    finalPrice : 0
  },
  getters: {
    totalOrderCount(state) {
      return state.orderList.length
    },
    totalOrderPrice(state) {
      state.finalPrice = 0
      state.orderList.forEach( order => {
        state.finalPrice += order.size.price + order.menu.price
    })
    return state.finalPrice
  }
  },
  mutations: {
    addOrder (state) {
      state.menuList.forEach( menu => {
        state.sizeList.forEach( size => {
          if ( menu.selected === true && size.selected === true) { 
            state.orderList.push({menu, size})
        }})
      })
    },
    updateMenuList (state, menu) {
      
      state.menuList.forEach( menu1 => {
        if (menu1.title === menu.title) {
          menu1.selected = true
        }
        else {
          menu1.selected = false
        }
      })
      
    },
    updateSizeList: function (state, size) {
      state.sizeList.forEach( size1 => {
        if (size1.name ===  size.name) {
          size1.selected = true
        }
        else {
          size1.selected = false
        }
      })
      console.log(state.sizeList)
    },
  },
  actions: {
  },
  modules: {
  }
})