<template>
  <div>
    <h1>오늘 할일</h1>
    <!-- {{bringToday}} -->
    <input type="text" v-model="inputData" @click="makenull"
    @keyup.enter="plusTodo">
    <div v-for="b in bringToday" :key="b.id" class="border">
        <button v-if="b.isCompleted" @click="changeComplete(b.id)">O</button>
        <button v-if="b.isCompleted === false" @click="changeComplete(b.id)">X</button>
        {{b.content}}
        <button v-if="b.isImportant" @click="changeImportant(b.id)">★</button>
        <button v-if="b.isImportant === false" @click="changeImportant(b.id)">☆</button>
    </div>
  </div>
</template>

<script>
export default {
    name : "TodayTodoPage",
    data () {
        return {
            inputData : '할 일을 작성하라!'
        }
    },
    computed : {
        bringToday () {
            
            return this.$store.getters.bringToday
        }
    },
    methods : {
        makenull () {
            this.inputData = null
        },
        plusTodo () {
            this.$store.commit('plusTodo', this.inputData)
            this.makenull()
        },
        changeComplete(id) {
            console.log(id)
            this.$store.commit('changeComplete', id)
        },
        changeImportant(id) {
            console.log(id)
            this.$store.commit('changeImportant', id)
        },
    }
}
</script>

<style>

</style>