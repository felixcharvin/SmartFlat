<template>
  <div class="panel panel-default">
    <div class="panel-heading">Effectors</div>
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
              <td v-bind:class="{'text-danger':effector.status=='off','text-success':effector.status=='on'}"><b>{{ effector.status.toUpperCase() }}</b></td>
              <td>
                <a v-if="effector.status == 'off'" class="btn btn-default" @click="switchOn(effector, 1)">On</a> 
                <a v-if="effector.status == 'on'" class="btn btn-danger" @click="switchOn(effector, 0)">Off</a>
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
    getEffectors: function() {
      axios.get(URL.rootAPI + '/effectors')
      .then(res => {
        this.effectors = res.data
      })
      .catch(e => {
        this.errors.push(e)
      })
    },
    switchOn: function(effector, status) {
      axios.post(URL.rootAPI+'/'+effector.type, {id: effector.pin, status: status})
      .then(res => {
        this.msg = res.data
        this.getEffectors()
      })
      .catch(e => {
        this.errors.push(e)
      })
    }
  },
  created() {
    this.getEffectors()
  }
}
</script>