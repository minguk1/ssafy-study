<template>
  <div>
    <h2>산출세액 : {{ computedTax }} 만원</h2>
    <h2>세액감면 : {{ taxFree }} 만원</h2>
    <hr>
    <FinalTax :final-tax="finalTax"/>
  </div>
</template>

<script>
import FinalTax from '@/components/FinalTax'

export default {
    name : 'TaxRate',
    components :{
    FinalTax,
  },
  props:{
    taxStandard : Number,
    taxFree : Number,
  },
  computed : {
    finalTax(){
      const temp = this.computedTax - this.taxFree
      return temp < 0 ? 0 : temp
    },
    computedTax(){
      if(this.taxStandard <= 1200 ){
        return Math.round(this.taxStandard * 0.06) 
      }else if(this.taxStandard <= 4600){
        return Math.round(this.taxStandard * 0.15 - 108) 
      }else if(this.taxStandard <= 8800){
        return Math.round(this.taxStandard * 0.24 - 522) 
      }else if(this.taxStandard <= 15000){
        return Math.round(this.taxStandard * 0.35 - 1490) 
      }else if(this.taxStandard <= 30000){
        return Math.round(this.taxStandard * 0.38 - 1940) 
      }else if(this.taxStandard <= 50000){
        return Math.round(this.taxStandard * 0.40 - 2540) 
      }else if(this.taxStandard <= 100000){
        return Math.round(this.taxStandard * 0.42 - 3540) 
      }else{
        return Math.round(this.taxStandard * 0.45 - 6540) 
      }
    }
  }


}
</script>

<style>

</style>