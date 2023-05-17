<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = " http://127.0.0.1:8000"

export default {
  name: 'CreateView',
  data() {
    return {
      title : null,
      content : null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목을 입력해라')
        return
      }
      else if (!content) {
        alert('내용 입력해라')
        return
      }
    //   function getCSRFToken() {
    //   const cookieValue = document.cookie
    //     .split('; ')
    //     .find((cookie) => cookie.startsWith('csrftoken='))
    //     .split('=')[1];
    //   return cookieValue;
    // }

    // // Axios의 기본 설정에 CSRF 토큰 헤더를 추가
    // axios.defaults.headers.common['X-CSRFToken'] = getCSRFToken();


      axios({
        method : 'POST',
        url : `${API_URL}/accounts/signup/`,
        data : {title, content},
        // headers: {'Content-Type': 'application/json',
        // 'X-CSRFToken': 'lmaBzgIbqGbQv3FkxTgjqkFiQWej7gjwOCE0cmKWm5vzQFp9hGMuT1WBXoJp7oW8'}

      })
      .then((res) => {
        console.log(res)
        this.$router.push({name : 'ArticleView'})
      })
      .catch((err) => {
        console.log(err)
      })

    }
  }
}
</script>

<style>

</style>
