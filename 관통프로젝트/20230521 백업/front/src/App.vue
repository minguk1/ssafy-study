<template>
  <div id="app" :class="{'overflow':mainCheck, 'overflow2':!mainCheck}">
    <MainView v-if="mainCheck"/>
    <div v-else>
      <router-view/>
      <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
      <div class="nav-box" id="nav-box-id">
        <nav class="d-flex justify-content-between">
          <i class="d-flex" @click="toHome"><h3>무비</h3><h5>의</h5><h3>민족</h3></i>
          <div>
            <router-link to="/">홈</router-link><span> | </span>
            <router-link v-if="JWTToken" :to="{name:'movies'}">영화</router-link><span v-if="JWTToken"> | </span>
            <router-link v-if="JWTToken" :to="{name:'community'}">커뮤니티</router-link><span v-if="JWTToken"> | </span>
            <router-link v-if="!JWTToken" :to="{name:'login'}">로그인</router-link>
            <router-link v-if="JWTToken" :to="{name:'mypage'}">내 정보</router-link><span v-if="JWTToken"> | </span>
            <span v-if="JWTToken" class="logout" @click="logout">로그아웃</span>
          </div>
        </nav>
      </div>
    </div>
    <img class="mascot" src="./assets/무민.png" alt="" id="moo" @click="toHome">
  </div>
</template>

<script>
import MainView from './components/MainView.vue';

export default {
  name: 'APP',
  data() {
    return {
      showNavBar: false
    }
  },
  components: {
    MainView,
  },
  methods: {
    toHome() {
      if (document.URL === 'http://localhost:8080/') {
        return
      } else {
        this.$router.push({name:'home'})
      }
    },
    logout() {
      this.$store.dispatch('logout')
      if (document.URL === 'http://localhost:8080/') {
        this.$router.go(0);
      } else {
        this.$router.push({name:'home'})
      }
    },
  },
  computed: {
    mainCheck() {
      return this.$store.state.mainCheck
    },
    JWTToken() {
      return this.$store.state.JWTToken ? true : false
    }
  },
  mounted() {
    const bottomElement = document.getElementById('nav-box-id');

    window.addEventListener('scroll', () => {
      const scrollPosition = window.scrollY || window.pageYOffset;
      const windowHeight = window.innerHeight;

      if (scrollPosition + windowHeight >= document.body.offsetHeight) {
        bottomElement.classList.add('show');
      } else {
        bottomElement.classList.remove('show');
      }
    });
  }
}
</script>

<style>
/* 기본 글꼴 및 페이지 화면 구성 작성 */
@font-face {
  font-family: "Riders-font";
  src: url("./assets/fonts/BMHANNAPro.ttf");
}
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  overflow: auto;
}

#app {
  /* font-family: 'Gowun Dodum', sans-serif; */
  font-family: 'Riders-font';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-color: rgb(42 193 188);
  height: 100%;
  /* overflow: auto; */
}

/* 이부분 수정 필요 */
.nav-box {
  position: sticky;
  bottom: -100px;
  width: 100%;
  transition: transform 0.3s;
  transform: translateY(100%); /* 초기에 숨겨진 상태로 설정 */
}

#nav-box-id:hover {
  transform: translateY(0); /* 마우스를 올렸을 때 요소를 보이게 함 */
}

nav {
  padding: 10px 150px 10px;
  line-height: 60px;
}

nav a {
  font-weight: bold;
  color: rgb(166 229 227);
  text-decoration: none;
}

nav a:hover {
  color: #0d6efd;
}

nav a.router-link-exact-active {
  color: #2c3e50;
}

.logout {
  font-weight: bold;
  color: rgb(166 229 227);
  text-decoration: none;
  cursor: pointer;
}

.logout:hover {
  color: #0d6efd;
}

.overflow {
  overflow: hidden;
}

.overflow2 {
  overflow: auto;
}

#moo {
  width: 150px;
  height: 100px;
  position: fixed;
  bottom: 20px;
  left: 20px;
}

#moo:hover {
  animation: rotate_image 3s linear infinite;transform-origin: 50% 50%;
}

@keyframes rotate_image{
    100% {
        transform: rotate(360deg);
    }
}
</style>
