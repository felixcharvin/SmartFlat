<template>
  <div class="panel panel-default">
    <div class="panel-heading">Thermometer</div>
    <div class="panel-body">
      <div>Temperature: {{ thermometer.temperature }} °C</div>
      <div>Humidity: {{ thermometer.humidity }} %</div>
    </div>
  </div>
</template>

<script>
import URL from './../../config/global'
import axios from 'axios'

export default {
  name: 'thermometer',
  data () {
    return {
      thermometer: {temperature: null, humidity: null},
      data: null,
      errors: []
    }
  },
  methods: {
    getThermometer: function() {
      axios.get(URL.rootAPI + '/thermometer')
      .then(res => {
        this.thermometer.temperature = res.data.temperature
        this.thermometer.humidity = res.data.humidity
    
        console.log(this.thermometer)
      })
      .catch(e => {
        this.errors.push(e)
      })
    }
  },
  created() {
    let self=this
    self.getThermometer()
  }
}

</script>