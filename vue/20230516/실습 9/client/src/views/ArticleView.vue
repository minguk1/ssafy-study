<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name: 'CreateView' }">[CREATE]</router-link>
    <ArticleList />
    <hr>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      

      // 로그인 되어 있으면 getArticles action 실행
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      }

      // 로그인 안되어 있으면 login 페이지로 이동
      else {
        alert('로그인이 필요한 페이지')
        this.$router.push({ name : 'login'})
      }
    }

  }
}
</script>

<style>

</style>
