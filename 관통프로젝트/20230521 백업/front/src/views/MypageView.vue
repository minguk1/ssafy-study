<template>
  <div class="container">
    <br>
    <h1>고마운분, {{ username }} 님</h1>
    <div class="d-flex">
      <h3>팔로워: {{ followers }} | </h3>
      <h3>팔로잉: {{ followings }}</h3>
    </div>
    <hr>
    <div class="d-flex justify-content-between">
      <h1>장바구니</h1>
      <h1>포인트 : 1000 점</h1>
    </div>
    <br>
    <h3>내가 선택한 영화들</h3>
    <div class="carousel-wrapper">
      <div class="left-icon-wrapper">
        <i class="fa-solid fa-angle-left icon-btn" @click="carouselBtn(false)">왼</i>
      </div>
      <div class="carousel">
        <div class="wrapper">
          <div class="carousel-content">
            <img
              v-for="(movie, idx) in baskets"
              :key="idx"
              class="card-img"
              :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
              @click="toMovieDetail(movie)"
            />
          </div>
        </div>
      </div>
      <div class="right-icon-wrapper">
        <i class="fa-solid fa-angle-right icon-btn" @click="carouselBtn(true)">오</i>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

// const URL = "http://localhost:8000/accounts/follow/"
const basketURL = "http://127.0.0.1:8000/movies/get_basket/"


export default {
  name: "MypageView",
  data() {
    return{
      mypageURL: "",
      followers: "",
      followings: "",
      baskets: []
    }
  },
  computed: {
    username (){
      return this.$store.state.username
    },
    JWTToken() {
      return this.$store.state.JWTToken
    },
    userpk() {
      return this.$store.state.userpk
    }
  },
  methods: {
    getUserInfo() {
      console.log("??",this.userpk)
      console.log(this.JWTToken)
      axios({
        method: "POST",
        url: this.mypageURL,
        headers: {
          Authorization: `Bearer ${this.JWTToken}`
        },
    })
    .then((res)=>{
      console.log(res)
      this.followers = res.data.followers
      this.followings = res.data.followings
    })
    .catch(err=>console.log(err))
    },
    makeURL() {
      this.mypageURL = "http://localhost:8000/accounts/follow/" + this.$store.state.userpk + "/"
    },
    getBasketInfo() {
      axios({
        method: "GET",
        url: basketURL + this.$store.state.userpk + '/',
        // headers: {
        //   Authorization: `Bearer ${this.JWTToken}`
        // }
      })
      .then((res)=>{
        console.log('basketinfo : ',res)
        this.baskets = res.data
      })
      .catch(err=>console.log(err))
    },
    toMovieDetail(movie) {
      console.log(movie)
      this.$router.push({name:'movie', params: {pk: movie.id}})
    },
    carouselBtn(isRight) {
      const carousel = document.querySelector(".carousel");
      const cardWidth = carousel.querySelector(".card-img").offsetWidth + 7;
      const scrollAmount = isRight ? cardWidth : -cardWidth;

      const currentScrollLeft = carousel.scrollLeft;
      const targetScrollLeft = currentScrollLeft + scrollAmount;

      carousel.scrollTo({
        left: targetScrollLeft,
        behavior: 'smooth'
      });
    },
  },
  mounted() {
    this.makeURL()
    this.getUserInfo()
    this.getBasketInfo()
  }
}
</script>

<style>
.carousel-wrapper {
  display: flex;
  align-items: center;
}

.left-icon-wrapper,
.right-icon-wrapper {
  flex: 0 0 auto;
}

.left-icon-wrapper i,
.right-icon-wrapper i {
  display: flex;
  align-items: center;
  justify-content: center;
  padding-right: 10px;
  padding-left: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
  height: 500px;
  margin-top: -24px;
}

.carousel {
  flex: 1;
  overflow: hidden;
}

.carousel-content {
  display: flex;
}

.carousel .card-img {
  height: 500px;
  object-fit: cover;
  width: 333px;
  cursor: pointer;
  margin-left: 14px;
  border: 0;
}

.carousel .card-img:nth-of-type(1) {
  margin-left: 0px;
}

.left-icon-wrapper i:hover,
.right-icon-wrapper i:hover {
  background-color: rgba(0, 0, 0, 0.2);
}

.left-icon-wrapper::before,
.right-icon-wrapper::before {
  content: "";
  display: inline-block;
  vertical-align: middle;
  height: 100%;
}
</style>