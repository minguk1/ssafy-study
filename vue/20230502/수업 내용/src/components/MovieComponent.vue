<template>
  <div>
    <h1>{{title}}</h1>
    <h2>{{description}}</h2>
  </div>
</template>

<script>
export default {
  name: 'MovieComponent',
  props: {
    msg: String,
    title : String,
    description : String
  }
}
</script>

<style>

</style>