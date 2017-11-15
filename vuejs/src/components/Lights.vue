<template>
  <div class="panel panel-default">
    <div class="panel-heading">Lights</div>
    <div class="panel-body">
      <line-chart :height="100" :chart-data="data"></line-chart>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import URL from './../../config/global'
import lineChart from './../charts/LineChart'

export default {
  name: 'lights',
  components: { lineChart },
  data () {
    return {
      lights: [],
      kitchenFrequencies: [],
      livingroomFrequencies: [],
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
    getFrequencies: function() {
      for (var i = 0; i < 24; i++) {
        axios.get(URL.rootAPI + '/lights/count/' + (i < 10 ? '0' : '') + i)
        .then(res => {
          this.kitchenFrequencies.push(res.data)
          console.log(this.kitchenFrequencies)
          this.data = {
            labels: ['00h00', '01h00', '02h00', '03h00', '04h00', '05h00', '06h00', '07h00', '08h00', '09h00', '10h00', 
              '11h00', '12h00', '13h00', '14h00', '15h00', '16h00', '17h00', '18h00', '19h00',
              '20h00', '21h00', '22h00', '23h00'],
            datasets: [{
              data: this.kitchenFrequencies,
              label: 'kitchen',
              borderColor: "#3e95cd",
              backgroundColor: '#3e95cd',
              fill: false     
            }, {
              data: [1, 10],
              label: 'livingroom',
              borderColor: "#8e5ea2",
              backgroundColor: '#8e5ea2',
              fill: false
            }]
          }
        })
        .catch(e => {
          console.log(e)
        })
      }
    }
  },
  created() {
    let self=this
    self.getHistory()
    self.getFrequencies()
  }
}
</script>