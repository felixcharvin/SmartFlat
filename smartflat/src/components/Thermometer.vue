<template>
  <div class="panel panel-default">
    <div class="panel-heading">Thermometer</div>
    <div class="panel-body">
      <div class="alert alert-info" role="alert">
        <div class="row">
        <div class="col-xs-6 text-left">Temperature:</div> <div class="col-xs-6 text-right"><b>{{ thermometer.temperature }} °C</b></div>
        <div class="col-xs-6 text-left">Humidity:</div> <div class="col-xs-6 text-right"><b>{{ thermometer.humidity }} %</b></div>
        </div>
      </div>
      <h4>Settings:</h4>
      <form class="form-horizontal">
        <div class="form-group">
          <label for="temperature" class="col-sm-2 control-label">Temperature: </label>
          <div class="col-sm-10">
            <input type="number" class="form-control" id="temperature" v-model="settings" placeholder="Temperature">
          </div>
        </div>
      </form>
      <!-- <vue-slider v-bind="slider" v-model="slider.value"></vue-slider> -->
    </div>
  </div>
</template>

<script>
import URL from './../../config/global'
import axios from 'axios'
import vueSlider from 'vue-slider-component'

export default {
  name: 'thermometer',
  components: { vueSlider },
  data () {
    return {
      thermometer: {temperature: null, humidity: null},
      settings: null,
      slider: {
        value: null,
        height: 6,
        dotSize: 14,
        min: 10,
        max: 30,
        interval: 0.5,
        tooltip: 'always',
      },
      data: null,
      errors: []
    }
  },
  watch: {
    'settings': function(val, old) {
      if (this.thermometer.temperature) {
        axios.put(URL.rootAPI + '/thermometer', {curTemp: this.thermometer.temperature, newTemp: val})
        .catch(err => {
          console.log(err)
        })
      }
    }
  },
  methods: {
    getThermometer: function() {
      axios.get(URL.rootAPI+'/thermometer/setting')
      .then(res => {
        // console.log(res.data)
        // this.slider.value = res.data.settings
        this.settings = res.data.settings
      })
      .catch(err => {
        console.log(err)
      })
      axios.get(URL.rootAPI + '/thermometer')
      .then(res => {
        this.thermometer.temperature = res.data.temperature
        this.thermometer.humidity = res.data.humidity
        // console.log(this.thermometer)
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