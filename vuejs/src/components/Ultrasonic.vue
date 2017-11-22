<template>
  <div class="panel panel-default">
    <div class="panel-heading">Alarm</div>
    <div class="panel-body">
      <div class="table-responsive">
        <table class="table">
          <thead>
            <tr>
              <th>duration</th>
              <th>distance</th>
              <th>date</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="ultra in ultrasonics">
              <td>{{ ultra.duration }}</td>
              <td>{{ ultra.distance }}</td>
              <td>{{ ultra.date }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <button class="btn btn-default" @click="init()">Init</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import URL from './../../config/global'

export default {
  name: 'ultrasonics',
  data () {
    return {
      ultrasonics: [],
      errors: []
    }
  },
  methods: {
    getHistory: function() {
      axios.get(URL.rootAPI + '/ultrasonics')
      .then(res => {
        this.ultrasonics = res.data
      })
      .catch(e => {
        this.errors.push(e)
      })
    },
    init: function() {
      axios.post(URL.rootAPI + '/ultrasonic-init')
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