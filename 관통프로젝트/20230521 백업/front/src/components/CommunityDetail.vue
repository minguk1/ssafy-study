<template>
  <div>
    <h1>커뮤니티 글들</h1>
    <div v-for="(community, idx) in communitys" :key="idx" class="d-flex">
      <!-- <p>{{ community.title }}</p> -->
      
      <p>유저: <span class="user-btn" @click="toUserInfo(community)">{{ community.username }}</span> </p> &nbsp;|&nbsp;
      <p>영화: {{ community.movie_title }} </p> &nbsp;|&nbsp;
      <p>내용: {{ community.content }} </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "CommunityDetail",
  props: {
    communitys: Array
  },
  methods: {
    toUserInfo(data){
      console.log(data)
      console.log(data.user)
      this.$router.push({name : 'yourpage', params: {pk:data.user}})
    }
  }
}
</script>

<style>
.user-btn {
  color: greenyellow;
}
.user-btn:hover {
  cursor: pointer;
}
</style>