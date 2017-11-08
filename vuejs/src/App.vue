<template>
  <div id="app" class="container-fluid">
    <div class="row">
      <div class="col-xs-3">
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

export default {
  name: 'app',
  components: { ultrasonics },
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
