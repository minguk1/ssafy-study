<template>
  <div>
    <h1>모든 할일</h1>
    <input type="text" v-model="inputData" @click="makenull"
    @keyup.enter="plusTodo">
    <!-- {{bb}} -->
    <div v-for="b in bb" :key="b.id" class="border d-flex justify-content-between">
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
    name : "AllTodoPage",
    computed : {
        bb () {
            return this.$store.state.state1.list
        }
    },
    data () {
        return {
            inputData : '할 일을 작성하라!'
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