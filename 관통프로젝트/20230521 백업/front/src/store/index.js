import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

// const persistedState = createPersistedState({
//   key="my-app",
//   storage: window.sessionStorage,
//   reducer: state => ({
//     mainCheck: state.mainCheck
//   })
// })

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    mainCheck : true,
    username: "",
    JWTToken: "",
    userpk: "",
    movies: []
  },
  getters: {
  },
  mutations: {
    MainChange(state) {
      state.mainCheck = false
    },
    SET_JWTTOKEN(state, data) {
      state.JWTToken = data.access
      state.username = data.user.username
      state.userpk = data.user.pk
      // console.log(state.userpk)
    },
    DEL_JWTTOKEN(state) {
      state.JWTToken = ""
      state.username = ""
      state.userpk = ""
    }
  },
  actions: {
    signupLogin(context, data) {
      context.commit('SET_JWTTOKEN', data)
    },
    logout(context) {
      context.commit('DEL_JWTTOKEN')
    }
  },
  modules: {
  }
})
