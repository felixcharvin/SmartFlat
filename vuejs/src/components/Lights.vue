<template>
  <div class="panel panel-default">
    <div class="panel-heading">Lights</div>
    <div class="panel-body">
      <div class="table-responsive">
        <table class="table">
          <thead>
            <tr>
              <th>location</th>
              <th>status</th>
              <th>date</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="light in lights">
              <td>{{ light.location }}</td>
              <td>{{ light.status }}</td>
              <td>{{ light.date }}</td>
              <td><a class="btn btn-default" href="">On</a> <a class="btn btn-danger" href="">Off</a></td>
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
  name: 'lights',
  data () {
    return {
      lights: [],
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
    switchOn: function(i) {
      axios.post(URL.rootAPI + '/light/' + i)
      .then(res => {
        this.msg = res.data
      })
      .catch(e => {
        this.errors.push(e)
      })
    }
  },
  created() {
    let self=this
    self.getHistory()
  }
}
</script>