<template>
  
    
    
      <div class='col-6'>
        <h2>예약 페이지</h2>
        <br>
        <h3>선생님 선택</h3>
        <div>
          <button @click='teacher1' :class="{teacherselect: teacher==='Eric'}"  class='mx-2 teacherbutton'>Eric</button>
          <button @click='teacher2' :class="{teacherselect: teacher==='Tony'}" class='mx-2 teacherbutton'>Tony</button>
        </div>
        <hr>
        <h3>시간 선택</h3>
        <div>
          <button @click='select(time, index)' :class="{selected : select_list[index] }"   class='col-2 mx-1 my-1 basic' v-for="(time, index ) in times" :key="index">{{time}}</button>
        </div>
        
        <button @click="sendToParent">예약 확정</button>
        
        
      </div>
      
    
    
  
</template>


<script>


export default {
  name: 'TimeTable',
  components: {
    
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
    select (time, index) {
      // 
      // 
      if (this.select_list[index] === false){
        this.cnt += 1
        if (this.cnt > 5) {
        alert('5타임까지만 신청할 수 있습니다.')
      }
        else {
          this.select_list.splice(index, 1, true)
          }}
      else {
          this.cnt -= 1
          this.select_list.splice(index, 1, false)
    

      }
    //   console.log(this.select_list)
    //   console.log(this.select_list[index])
    },
    teacher1 () {
      this.teacher = 'Eric'
    },
    teacher2 () {
      this.teacher = 'Tony'
    },
    sendToParent () {
        if (this.teacher === '') {
            alert('선생님을 선택해 주세요.')
        }
        else if (!this.select_list.includes(true)) {
            alert('시간을 선택해 주세요.')
        }

        else {
            this.$emit('send-to-parent', this.teacher, this.select_list)
            this.teacher = ''
            this.select_list = new Array(30).fill(false)
            console.log(this.select_list)
            this.cnt = 0

        }
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
