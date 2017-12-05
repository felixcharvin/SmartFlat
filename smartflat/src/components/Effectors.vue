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
              <td class="text-right">
                <a v-if="effector.status != 'on'" class="btn btn-default" @click="switchStatus(effector.type, effector.pin, 1)">On</a> 
                <a v-if="effector.pinLow && effector.status != 'low'" class="btn btn-primary" @click="switchStatus(effector.type, effector.pinLow, 1)">Low</a> 
                <a v-if="effector.status != 'off'" class="btn btn-danger" @click="switchStatus(effector.type, effector.pin, 0)">Off</a>
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
      effectors: []
    }
  },
  methods: {
    getEffectors: function() {
      axios.get(URL.rootAPI + '/effectors')
      .then(res => {
        this.effectors = res.data
      })
      .catch(e => {
        console.log(e)
      })
    },
    switchStatus: function(type, pin, status) {
      axios.post(URL.rootAPI+'/'+type, {id: pin, status: status})
      .then(res => {
        this.msg = res.data
        this.getEffectors()
      })
      .catch(e => {
        console.log(e)
      })
    }
  },
  created() {
    this.getEffectors()
  }
}
</script>