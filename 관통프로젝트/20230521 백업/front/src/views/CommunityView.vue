<template>
  <div class="container">
    <br>
    <h1>커뮤니티임</h1>
    <!-- <b-row>
        <label for="input-username" class="text-left">제목</label>
        <b-form-input 
        id="input-username" 
        placeholder="제목" 
        v-model="title" 
        style="font-family: Arial, Helvetica, sans-serif;"
        trim
        ></b-form-input>
    </b-row> -->
    <b-row>
        <label for="input-username" class="text-left">내용</label>
        <b-form-textarea 
        id="input-username" 
        placeholder="내용" 
        v-model="content" 
        style="font-family: Arial, Helvetica, sans-serif;"
        trim
        ></b-form-textarea>
    </b-row>
    <br>
    <button class="btn" @click="createCommnet">작성하기</button>
    <br>
    <hr>
    <CommunityDetail :communitys="communitys"/>
  </div>
</template>

<script>
import CommunityDetail from '@/components/CommunityDetail.vue';
import axios from 'axios';

// 전체가 아닌 일부의 2번 영화 정보에 대한 코멘트로 예시를 들음
const AXIOS_URL = "http://localhost:8000/movies/3/create_comment/"

export default {
  name: "CommunityView",
  data() {
    return {
      user: null,
      content: null,
      movie: null,
      communitys : [],
    }
  },
  computed: {
    JWTToken() {
      return this.$store.state.JWTToken
    } 
  },
  components: {
    CommunityDetail,
  },
  methods: {
    createCommnet() {
      axios({
        method: "POST",
        url: AXIOS_URL,
        headers: {
          Authorization: `Bearer ${this.JWTToken}`,
          'Content-Type': 'multipart/form-data'
        },
        data: {
          content: this.content
        }
      })
      .then((res)=>{
        console.log(res)
        this.communitys.push({username: res.data[res.data.length-1].username,movie_title: res.data[res.data.length-1].movie_title,content: this.content})
        this.content = null
        // this.communitys.push(res.data)
        // this.communitys.push({title:this.title, content: this.content, user:this.user})
      })
      .catch((err)=>{
        console.log(err)
        alert('로그인을 해주세요.')
      })
      // axios post 요청으로 처리할예정
      // 현재는 그냥 data에 저장해두겠음.
    },

    getComment() {
      axios({
        method: "GET",
        url: AXIOS_URL,
        headers: {
          Authorization: `Bearer ${this.JWTToken}`
        },
      })
      .then((res)=>{
        console.log(res.data)
        this.communitys = res.data
      })
      .catch(err=>console.log(err))
      // axios post 요청으로 처리할예정
      // 현재는 그냥 data에 저장해두겠음.
      // this.communitys.push({content: this.content})
    },
  },
  mounted() {
    this.getComment()
  }
}
</script>

<style>
.text-left {
  text-align: left;
}

</style>