<template>
  <div id="home" @click="onClickChange">
    <br>
    <!-- <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h1>홈 화면 입니다.</h1>
    <h2 v-if="JWTToken">토큰 있음</h2>
    <h2 v-else>토큰 없음</h2>
    <b-spinner label=""></b-spinner>
    <div class="img-box">
      <img id="bm-img-1" src="https://www.baemin.com/_next/static/images/img-shoppinglive_re.png" alt="">
    </div>
  </div>
</template>

<script>
export default{
  name: "HomeView",
  methods: {
    onClickChange() {
      if (this.$store.state.mainCheck) {
        this.warpSpeed = this.warpSpeed > 0 ? 0 : 1;
        setTimeout(() => {
            // this.$router.push({name:"home"})
            this.$store.commit("MainChange")
        }, 5000);
      }
    }
  },
  computed: {
    JWTToken () {
      return this.$store.state.JWTToken
    }
  }
}

</script>

<style>
img {
  overflow-clip-margin: content-box;
  overflow: clip;
}

.img-box{
  display: block;
  margin-top:auto;
  margin-bottom: 0;
  align-items: right;
}

#bm-img-1{
  width: 600px;
  height: 600px;
}
</style>