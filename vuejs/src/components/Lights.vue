<template>
  <div class="panel panel-default">
    <div class="panel-heading">Lights</div>
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
  name: 'lights',
  components: { barChart },
  data () {
    return {
      lights: [],
      kitchenOnFrequencies: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      livingroomOnFrequencies: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      kitchenLowFrequencies: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      livingroomLowFrequencies: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      labels: ['00h00', '01h00', '02h00', '03h00', '04h00', '05h00', '06h00', '07h00', '08h00', '09h00', '10h00', 
              '11h00', '12h00', '13h00', '14h00', '15h00', '16h00', '17h00', '18h00', '19h00',
              '20h00', '21h00', '22h00', '23h00'],
      data: null,
      errors: []
    }
  },
  methods: {
    getHistory: function() {
      axios.get(URL.rootAPI + '/lights')
      .then(res => {
        this.lights = res.data
      })
      .catch(e => {
        this.errors.push(e)
      })
    },

    fillData(frequencies) {
      frequencies.forEach(element => {
        let date = new Date(element.date)
        if (element.location == 'kitchen' && element.status == 'on') this.kitchenOnFrequencies[date.getHours()]++
        if (element.location == 'kitchen' && element.status == 'low') this.kitchenLowFrequencies[date.getHours()]++
        if (element.location == 'livingroom' && element.status == 'on') this.livingroomOnFrequencies[date.getHours()]++
        if (element.location == 'livingroom' && element.status == 'low') this.livingroomLowFrequencies[date.getHours()]++
      })
    },
    getFrequencies: function() {
      axios.get(URL.rootAPI + '/lights/frequencies')
      .then(res => {
        this.fillData(res.data)
        this.data = {
          labels: this.labels,
          datasets: [{
            data: this.kitchenOnFrequencies,
            label: 'kitchen on',
            borderColor: "#27ae60",
            backgroundColor: '#27ae60',
            fill: false
          }, {
            data: this.kitchenLowFrequencies,
            label: 'kitchen low',
            borderColor: "#f1c40f",
            backgroundColor: '#f1c40f',
            fill: false
          }, {
            data: this.livingroomOnFrequencies,
            label: 'livingroom on',
            borderColor: "#2980b9",
            backgroundColor: '#2980b9',
            fill: false
          }, {
            data: this.livingroomLowFrequencies,
            label: 'livingroom low',
            borderColor: "#e74c3c",
            backgroundColor: '#e74c3c',
            fill: false
          }]
        }
        // console.log(this.kitchenOnFrequencies)
        // console.log(this.livingroomFrequencies)
      })
    },
  },
  created() {
    let self=this
    self.getHistory()
    self.getFrequencies()
  }
}
</script>