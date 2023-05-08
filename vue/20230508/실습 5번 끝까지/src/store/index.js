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
    finalPrice : 0,
    optionList : [
      { name : '샷',
        price : 500,
        count : 0,  
    },
      { name : '헤이즐넛 시럽',
        price : 500,
        count : 0,  
    },
      { name : '바닐라 시럽',
        price : 500,
        count : 0,  
    },
    ],
  },
  getters: {
    totalOrderCount(state) {
      return state.orderList.length
    },
    totalOrderPrice(state) {
      state.finalPrice = 0
      state.orderList.forEach( order => {
        order.option.forEach (opt => {
        state.finalPrice += opt.count *opt.price
    })
    state.finalPrice += order.menu.price + order.size.price
  })
    return state.finalPrice
  }
  },
  mutations: {
    addOrder (state) {
      const option = JSON.parse(JSON.stringify(state.optionList))
      state.menuList.forEach( menu => {
        state.sizeList.forEach( size => {
          if ( menu.selected === true && size.selected === true) { 
            state.orderList.push({menu, size, option})
            console.log(state.orderList)
            state.optionList.forEach(option => {
              option.count = 0
              
            })
            console.log(state.optionList)
        }})
      })
      const savefile = JSON.stringify(state.orderList)
      sessionStorage.setItem('storage', savefile)
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
    increase_count (state, name) {
      console.log(name)
      state.optionList.forEach( option => {
        if (option.name === name) {
          option.count += 1
        }
      })
    },
    
    decrease_count (state, name) {
      console.log(name)
      state.optionList.forEach( option => {
        if (option.name === name && option.count > 0) {
          option.count -= 1
        }
      })
    },
    storage (state) {

      const savefile = sessionStorage.getItem('storage')
      // console.log(savefile)
      // const pushfile = JSON.parse(savefile)
      // console.log(pushfile)
      state.orderList = JSON.parse(savefile) || []
      // console.log(state)
    },
  },
  actions: {
  },
  modules: {
  }
})
