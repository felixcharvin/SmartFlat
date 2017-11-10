import { Line, mixins } from 'vue-chartjs'
import axios from 'axios'
import URL from './../../config/global'

export default {
  extends: Line,
  mixins: [mixins.reactiveProp],
  props: ['chartData'],  
  data() {
    return {
      option: {responsive: true, maintainAspectRatio: false}     
    }
  },
  mounted () {
    this.renderChart(this.data,this.option)
  }
}