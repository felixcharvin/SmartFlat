import { Line, mixins } from 'vue-chartjs'
import axios from 'axios'
import URL from './../../config/global'

export default {
  extends: Line,
  mixins: [mixins.reactiveProp],
  props: ['chartData'],  
  data() {
    return {
      option: {responsive: true, maintainAspectRatio: false,
        hover: {
          mode: 'nearest',
          intersect: true
        },
        tooltips: {
          mode: 'index',
          intersect: false,
        },
      }     
    }
  },
  mounted () {
    this.renderChart(this.data,this.option)
  }
}