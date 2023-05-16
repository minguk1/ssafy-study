import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
// import router from "../router"

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [
    ],
    token : null
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
      console.log(articles)
    },
    
    // signup & login => 토큰 발급 
    SAVE_TOKEN(state, token) {
      state.token = token
      // router.push({name : 'ArticleView'}) // store 내  router 접근 불가 > import 필수
    
    }
  },
  actions: {
    
    getArticles(context) {
      console.log(context.state.token)
      axios({
        method: 'get',
        url: `${API_URL}/articles/`,
        headers : {
          Authorization : `Bearer ${context.state.token}`
        }
      })
        .then((res) => {
        // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    signUp(context, data) {
      // const username = payload.username
      // const password1 = payload.password1
      // const password2 = payload.password2
      context.commit('SAVE_TOKEN', data.access)
      
    },
    login(context, data) {
      // const username = payload.username
      // const password = payload.password
      context.commit('SAVE_TOKEN', data.access)
      
    }
  },
  modules: {
  }
})

