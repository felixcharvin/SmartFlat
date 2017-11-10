<template>
  <div class="panel panel-default">
    <div class="panel-heading">Lights</div>
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
            <tr v-for="effector in effectors">
              <td>{{ effector.name }}</td>
              <td>{{ effector.location }}</td>
              <td>{{ effector.status }}</td>
              <td>
                <a class="btn btn-default" @click="switchOn(effector.type, effectors.pin, 1)">On</a> 
                <a class="btn btn-danger" @click="switchOn(effector.type, effectors.pin, 0)">Off</a>
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
  name: 'effectors',
  data () {
    return {
      effectors: [],
      errors: []
    }
  },
  methods: {
    getHistory: function() {
      axios.get(URL.rootAPI + '/effectors')
      .then(res => {
        this.effectors = res.data
      })
      .catch(e => {
        this.errors.push(e)
      })
    },
    switchOn: function(type, pin, status) {
      axios.post(URL.rootAPI+'/'+type+'/'+pin+'/'+status)
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