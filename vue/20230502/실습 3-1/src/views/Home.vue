<template>
  <div>
    <h1>Home or About</h1>
    <h2>첫 번째 박스</h2>
    <div class="global">
      <div class="box scoped-box"></div>
    </div>
    <h2>두 번째 박스</h2>
    <div class="global">
      <div class="box scoped-box"></div>
    </div>
  </div>
</template>

<script>
export default {
    name : 'HomeComponent',
}
</script>

<style>
    .box {
        width : 100px;
        border : solid 1px;
        height: 100px;

    }

    .global {
        width: 100px;
        margin : 0 auto;
    }
</style>