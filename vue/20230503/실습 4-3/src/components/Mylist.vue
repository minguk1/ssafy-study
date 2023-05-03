<template>
  <div class='col-6 right'>
        <h2>상담 신청 현황</h2>
        <br>
        <h3>상담 선생님</h3>
        <br>
        <h4>성함 : {{sendToChild.teacher}}</h4>
        <hr>
        <h3>예약 현황</h3>
        <br>
        <h5>시간들 : <span v-for="(time,index) in times" :key="index"><span v-if="sendToChild.select_list[index]">{{time }} </span></span></h5>
        <hr>
        <img src="../assets/ssafy-logo.png"/>
      </div>
</template>

<script>
export default {
    name: 'MyList',
    props: {
    sendToChild : Object,
    
    
    },
    data () {
    return {times: [
  "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
  "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
  "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
    ],}
    }
}
</script>

<style>

</style>