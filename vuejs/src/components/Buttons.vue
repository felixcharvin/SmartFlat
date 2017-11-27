<template>
  <div class="panel panel-default">
    <div class="panel-heading">Buttons</div>
    <div class="panel-body">
      <bar-chart :height="150" :chart-data="data"></bar-chart>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import URL from './../../config/global'
import barChart from './../charts/BarChart'

export default {
  name: 'buttons',
  components: { barChart },
  data () {
    return {
      buttons: [],
      doorFrequencies: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      tvFrequencies: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      labels: ['00h00', '01h00', '02h00', '03h00', '04h00', '05h00', '06h00', '07h00', '08h00', '09h00', '10h00', 
              '11h00', '12h00', '13h00', '14h00', '15h00', '16h00', '17h00', '18h00', '19h00',
              '20h00', '21h00', '22h00', '23h00'],
      data: null,
      errors: []
    }
  },
  methods: {
    fillData(frequencies) {
      frequencies.forEach(element => {
        let date = new Date(element.date)
        if (element.location == 'Furnace') this.doorFrequencies[date.getHours()]++
        if (element.location == 'TV') this.tvFrequencies[date.getHours()]++
      })
    },
    getFrequencies: function() {
      axios.get(URL.rootAPI + '/buttons/frequencies')
      .then(res => {
        this.fillData(res.data)
        this.data = {
          labels: this.labels,
          datasets: [{
            data: this.doorFrequencies,
            label: 'Furnace',
            borderColor: "#27ae60",
            backgroundColor: '#27ae60',
            fill: false
          }, {
            data: this.tvFrequencies,
            label: 'TV',
            borderColor: "#2980b9",
            backgroundColor: '#2980b9',
            fill: false
          }]
        }
        // console.log(this.kitchenOnFrequencies)
        // console.log(this.livingroomFrequencies)
      })
    },
  },
  created() {
    this.getFrequencies()
  }
}
</script>