import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from "../views/Home.vue"
import Happeed from "../views/Happeed.vue"
import NotFound404 from "../views/NotFound404.vue"
import Happling from "../views/Happling.vue"
import Happlossome from "../views/Happlossome.vue"
import Happlower from "../views/Happlower.vue"

Vue.use(VueRouter)

const routes = [
  {
    path : '/404',
    name : 'NotFound404',
    component : NotFound404,
  },
  {
    path : '/',
    name : 'home',
    component : Home
  },
  {
    path : '/happeed',
    name : 'happeed',
    component : Happeed,
    beforeEnter(to, from, next) {
      if (from.name === 'happling') {
        alert('이전 진화단계로 돌아갈 수 없습니다.')
        next({name : 'happling'})
      }
      else (
        next()
      )
    }
  },
  {
    path : '/happling',
    name : 'happling',
    component : Happling,
    beforeEnter(to, from, next) {
      if (from.name === 'happlossome') {
        alert('이전 진화단계로 돌아갈 수 없습니다.')
        next({name : 'happlossome'})
      }
      else (
        next()
      )
    }
  },
  {
    path : '/happlossome',
    name : 'happlossome',
    component : Happlossome,
    beforeEnter(to, from, next) {
      if (from.name === 'happlower') {
        alert('이전 진화단계로 돌아갈 수 없습니다.')
        next({name : 'happlower'})
      }
      else (
        next()
      )
    }
  },
  {
    path : '/happlower',
    name : 'happlower',
    component : Happlower
  },
  {
    path : '*',
    redirect: '/404'
  }
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
