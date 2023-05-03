<template>
<div>
    <h1>AppChild</h1>
    <input type="text" v-model='child_input' @input="sendToParent">
    <h3>appData: {{sendToChild.app_input}}</h3>
    <h3>parentData: {{sendToChild.parent_input}}</h3>
    <h3>childData: {{child_input}}</h3>
</div>
</template>

<script>
export default {
    name : 'AppChild',
    props: {
    sendToChild : Object,
    
    },
    data : function () {
    return {
      child_input : '',
    }
  },
  methods : {
    sendToParent () {
        this.$emit('send-to-parent', this.child_input)
    }
  }
}

</script>

<style>

</style>