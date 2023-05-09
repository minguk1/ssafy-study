import Vue from 'vue'
import Vuex from 'vuex'
import state1 from './modules/todo'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
    bringToday(state) {
      const today = new Date()
      let today_list = []
      
      state.state1.list.forEach(lis => {
        if (lis.dueDateTime === today.toJSON().slice(0, 10) + 'T00:00'
        && lis.isCompleted === false) {
          today_list.push(lis)
          
        }
      })
      return today_list
    },
    bringImportant(state) {
      
      let important_list = []
      
      state.state1.list.forEach(lis => {
        if (lis.isImportant && lis.isCompleted === false) {
          important_list.push(lis)
          
        }
      })
      return important_list
    }
  },
  mutations: {
    plusTodo(state, input) {
      const nowDateObj = new Date()
      state.state1.list.push(
        {
          id: nowDateObj.getTime(),                // nowDateObj.getTime()
          content: input,                   // Todo 내용
          dueDateTime: nowDateObj.toJSON().slice(0, 10) + 'T00:00',  // 마감일
          isCompleted: false,               // 완료된 할 일
          isImportant: false,   
        }
      )
      // const savefile = JSON.stringify(state.state1.list)
      // sessionStorage.setItem('storage', savefile)
    },
    plusTodoimportant(state, input) {
      const nowDateObj = new Date()
      state.state1.list.push(
        {
          id: nowDateObj.getTime(),                // nowDateObj.getTime()
          content: input,                   // Todo 내용
          dueDateTime: nowDateObj.toJSON().slice(0, 10) + 'T00:00',  // 마감일
          isCompleted: false,               // 완료된 할 일
          isImportant: true,   
        }
      )
    },
    changeComplete(state, id) {
      state.state1.list.forEach(lis => {
        if (lis.id === id) {
          lis.isCompleted = !lis.isCompleted
        }
      })
    },
    changeImportant(state, id) {
      state.state1.list.forEach(lis => {
        if (lis.id === id) {
          lis.isImportant = !lis.isImportant}
      })
    },
    // storage (state) {

    //   const savefile = sessionStorage.getItem('storage')
    //   // console.log(savefile)
    //   // const pushfile = JSON.parse(savefile)
    //   // console.log(pushfile)
    //   state.state1.push(JSON.parse(savefile))
    //   // console.log(state)
    // },
    
  },
  actions: {
  },
  modules: {
    state1
  }
})
