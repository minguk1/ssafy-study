<template>
  <div class="wrap">
    <h2>시작</h2>
    <div class="detail d-flex ">
        <div class="prev d-flex align-items-center" @click="toHome"><span class="btn">
            이전</span></div>
        <div><img src="../assets/happeed.png" alt="" class="image"></div>
        <div class="next d-flex align-items-center" @click="toNext"><span class="btn">다음</span></div>
    </div>
    <h2>해피드</h2>
  </div>
</template>

<script>
export default {
    name : "Happeed",
    methods: {
        toHome() {
            this.$router.push({name : 'home'})
        },
        toNext() {
            this.$router.push({name : 'happling'})
        }
    }
}
</script>

<style>
.wrap {
    text-align: center;
    border : 1px solid gray;
    padding : 20px;
    margin-top: 50px;
    border-radius: 10px;
    box-shadow: lightgray 6px 6px 12px 12px;
}
.image {
    width : 200px
}
.d-flex {
    display: flex;
}
.align-items-center {
    align-items: center;
}
.btn {
    border : 1px solid black;
    border-radius: 3px;
    padding : 10px;


}
</style>
