<template>
  <div>
    <p>연봉 입력 (만원) : <input type="number" v-model.number="totalSalary"></p>
    <p>세액감면액 (만원) : <input type="number" v-model.number="taxFree"></p>
    <hr>
    <br>
    <h2>종합소득 금액 : {{totalSalary }} 만원</h2>
    <h2>종합소득 공제 :(-) 150 만원</h2>
    <h2>과세표준 : {{ taxStandard }} 만원 </h2>
    <hr>
    <TaxRate :tax-standard="taxStandard"
    :tax-free="taxFree" />
  </div>
</template>

<script>

import TaxRate from '@/components/TaxRate'
export default {
    name : 'InCome',
    data(){
    return {
      totalSalary : 0,
      taxFree : 0,
    }
  },
  components : {
    TaxRate
  },
  
  computed : {
    taxStandard(){
      const temp = this.totalSalary - 150
      return temp < 0 ? 0 : temp
    } 
  }
}
</script>

<style>

</style>