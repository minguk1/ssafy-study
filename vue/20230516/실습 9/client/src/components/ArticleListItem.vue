<template>
  <div class="box">
    <h1>{{ article.title }}</h1>
    <h2>{{article.content}}</h2>
    <hr>
    <p>작성자 : {{article.author_username}}</p>
    <p>{{ article.created_at }}</p>
    
    
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  }
}
</script>

<style>
.box {
    border : 1px solid;
    width : 70%;
    margin-left : auto;
    margin-right : auto;
}
</style>