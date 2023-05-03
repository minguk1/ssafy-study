<template>
<div>
    <h1>AppParent</h1>
    <input type="text" v-model='parent_input' @input="sendToApp">
    
    <h3>AppData : {{sendToParent.app_input}}</h3>
    <h3>childData : {{child_input}}</h3>
    <app-child
        :send-to-child="{parent_input, app_input : sendToParent.app_input}"
        @send-to-parent="getFromChild"
    />
    
</div>
</template>

<script>
import AppChild from './AppChild.vue'

export default {
    name : 'AppParent',

    props: {
    sendToParent : Object,
    
    },

    components: {
    AppChild,
        
  },
    data : function () {
    return {
      parent_input : '',
      child_input : '',
      
    }
  },
  methods : {
    getFromChild (child_input) {
        this.child_input = child_input
        
    },
    sendToApp () {
        this.$emit('send-to-app', this.child_input, this.parent_input)
    }
  }
}
</script>

<style>

</style>