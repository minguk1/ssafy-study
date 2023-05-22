<template>
  <div class="movies">
    <br>
    <h1>영화 페이지</h1>
    <div class="carousel-wrapper">
      <div class="left-icon-wrapper">
        <i class="fa-solid fa-angle-left icon-btn" @click="carouselBtn(false)">왼</i>
      </div>
      <div class="carousel">
        <div class="wrapper">
          <div class="carousel-content">
            <img
              v-for="(movie, idx) in movies"
              :key="idx"
              class="card-img"
              :src="movie.srcURL"
              @click="toMovieDetail(movie)"
            />
          </div>
        </div>
      </div>
      <div class="right-icon-wrapper">
        <i class="fa-solid fa-angle-right icon-btn" @click="carouselBtn(true)">오</i>
      </div>
    </div>
    <MovieDetailVue/>
  </div>
</template>

<script>
import MovieDetailVue from '../components/MovieDetail.vue'
import axios from 'axios'

// const API_KEY = process.env.VUE_APP_TMDB_API_KEY
// const AXIOS_URL = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page=1&sort_by=vote_average.desc&without_genres=99,10755&vote_count.gte=200&api_key=${API_KEY}`

const AXIOS_URL = 'http://localhost:8000/movies/'
const imgURL = 'https://image.tmdb.org/t/p/original'
// const carousel = document.querySelector(".carousel")
// const ifrstImgWidth = carousel.querySelectorAll("img")[0].clientWidth + 14;

export default {
  name: "MoviesView",
  data() {
    return {
      // srcURL : imgURL + this.getMovie.poster_path
      movies : [],
    }
  },
  // computed: {
  //   movies() {
  //     return this.$store.state.movies
  //   }
  // },
  components: {
    MovieDetailVue,
  },
  methods: {
    getMovies () {
      axios({
        method: "GET",
        url: AXIOS_URL
      })
      .then((res)=>{
        console.log(res)
        res.data.forEach((element) => {
          const srcURL = imgURL + element.poster_path
          const title = element.title
          const vote_average = element.vote_average
          const pk = element.id

          this.movies.push({
            srcURL: srcURL,
            title: title,
            vote_average: vote_average,
            pk: pk
          })
        });
        // this.$store.dispatch('getMovies', )
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    toMovieDetail(movie) {
      console.log(movie)
      this.$router.push({name:'movie', params: {pk: movie.pk}})
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
    this.getMovies()
  }
}
</script>

<style>
.movies {
  position: relative;
}

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