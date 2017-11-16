import { Bar, mixins } from 'vue-chartjs'
import axios from 'axios'
import URL from './../../config/global'

export default {
  extends: Bar,
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
      scales: {
        xAxes: [{
            barPercentage: 1.2
        }]
    }}     
    }
  },
  mounted () {
    this.renderChart(this.data,this.option)
  }
}