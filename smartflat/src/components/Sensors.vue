<template>
  <div class="panel panel-default">
    <div class="panel-heading">Sensors</div>
    <div class="panel-body">
      <div class="table-responsive">
        <table class="table">
          <thead>
            <tr>
              <th>name</th>
              <th>location</th>
              <th>status</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="sensor in sensors">
              <td>{{ sensor.name }}</td>
              <td>{{ sensor.location }}</td>
              <td v-bind:class="{'text-danger':sensor.status=='off','text-success':sensor.status=='on'}"><b>{{ sensor.status.toUpperCase() }}</b></td>
              <td>
                <a v-if="sensor.status != 'on'" class="btn btn-default" @click="switchStatus(sensor.type, sensor.pin, 1)">On</a> 
                <a v-if="sensor.status != 'off'" class="btn btn-danger" @click="switchStatus(sensor.type, sensor.pin, 0)">Off</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import URL from './../../config/global'

export default {
  name: 'sensors',
  data () {
    return {
      sensors: []
    }
  },
  methods: {
    getSensors: function() {
      axios.get(URL.rootAPI + '/sensors')
      .then(res => {
        this.sensors = res.data
      })
      .catch(e => {
        console.log(e)
      })
    },
    switchStatus: function(type, pin, status) {
      axios.post(URL.rootAPI+'/'+type, {id: pin, status: status})
      .then(res => {
        this.msg = res.data
        this.getSensors()
      })
      .catch(e => {
        console.log(e)
      })
    }
  },
  created() {
    this.getSensors()
  }
}
</script>