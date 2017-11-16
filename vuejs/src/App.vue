<template>
  <div id="app" class="container-fluid">
    <div class="row">
      <div class="col-md-6">
        <effectors></effectors>
      </div>
      <div class="col-md-6">
        <lights></lights>
      </div>
    </div>
    <div class="row">
      <div class="col-md-3">
        <ultrasonics></ultrasonics>
      </div>
    </div>
    <h1 v-if="errors.lenght > 0">{{ errors }}</h1>
  </div>
</template>

<script>

import axios from 'axios'
import URL from './../config/global'
import ultrasonics from './components/Ultrasonic.vue'
import lights from './components/Lights.vue'
import effectors from './components/Effectors.vue'

export default {
  name: 'app',
  components: { ultrasonics, lights, effectors },
  data () {
    return {
      msg: '',
      errors: []
    }
  }
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
