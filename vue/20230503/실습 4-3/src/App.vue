<template>
  <div id="app">
    <h1>SSAFY 상담 예약 시스템</h1>
    <div class='d-flex'>
    <timetable
      @send-to-parent='getFromChild'
    />
    <mylist
      :send-to-child="{teacher, select_list}"
    />
      
    
    
    
    <hr>
    </div>
  </div>
  
</template>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
import Mylist from './components/Mylist.vue'
import Timetable from './components/Timetable.vue'

export default {
  name: 'App',
  components: {
    Timetable,
    Mylist,

    
  },
  data () {
    return {times: [
  "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
  "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
  "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
    ],
    cnt : 0,
    select_list : new Array(30).fill(false),
    teacher_list : ['Eric', 'Tony'],
    teacher : ''
    }
    

  },
  methods : {
    getFromChild(teacher, select_list) {
      // console.log(teacher)
      // console.log(select_list)
      this.teacher = teacher
      this.select_list = select_list
    }
  }
}


</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.basic {
  background-color: white;
  color : #424242;
  border : none;
}

.selected {
  background-color: #658dc63d;
  color : #0F4C81;
}

.right {
  background-color: #658dc63d;
}


.teacherbutton {
  background-color: white;
  /* border : 1px; */
  
  border : 1px solid #0F4C81;
}
button:hover {
  background-color: aqua !important;
}
.teacherselect {
  background-color: #658dc63d;
}

</style>
