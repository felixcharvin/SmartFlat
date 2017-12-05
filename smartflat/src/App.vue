<template>
  <div id="app" class="container-fluid">
    <div class="page-header">
      <h1>SmartFlat <small>Manage your appartment</small></h1>
    </div>
    <div class="row">
      <div class="col-md-6">
        <effectors></effectors>
      </div>
      <div class="col-md-6">
        <sensors></sensors>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6">
        <ultrasonics></ultrasonics>
      </div>
      <div class="col-md-6">
        <thermometer></thermometer>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6">
        <lights></lights>
      </div>
      <div class="col-md-6">
        <buttons></buttons>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'
import URL from './../config/global'
import ultrasonics from './components/Ultrasonic.vue'
import lights from './components/Lights.vue'
import effectors from './components/Effectors.vue'
import thermometer from './components/Thermometer.vue'
import buttons from './components/Buttons.vue'
import sensors from './components/Sensors.vue'

export default {
  name: 'app',
  components: { ultrasonics, lights, buttons, effectors, thermometer, sensors },
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}

a {
  color: #42b983;
}
</style>
