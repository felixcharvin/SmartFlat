<template>
  <div class="panel panel-default">
    <div class="panel-heading">Alarm</div>
    <div class="panel-body">
      <div>Status: {{ alarm.status }}</div>
      <hr>
      <form>
        <div class="form-group">
          <label class="sr-only" for="code">Amount (in dollars)</label>
          <div class="input-group">
            <div class="input-group-addon">$</div>
            <input type="number" v-model="code" class="form-control" id="code" placeholder="pass code">
          </div>
        </div>
        <button type="button" class="btn btn-default" @click="enable()">Enable</button> 
        <button type="button" class="btn btn-danger" @click="disable()">Disable</button>
        <button type="button" class="btn btn-info" data-toggle="modal" data-target="#myModal">Edit Code</button>
      </form>
    </div>


    <div class="modal fade" id="myModal" role="dialog">
      <div class="modal-dialog">

        <!-- Modal content-->
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">&times;</button>
            <h4 class="modal-title">Edit Alarm Pass Code</h4>
          </div>
          <form action="">
            <div class="modal-body">
              <div class="form-group">
                <div class="input-group">
                  <input type="number" class="form-control" placeholder="Old pass code">
                  <input type="number" class="form-control" placeholder="New pass code">
                  <input type="number" class="form-control" placeholder="Repeat new pass code">
                </div>
              </div>
            </div>
            <div class="modal-footer">
              <button @click="changeCode()" class="btn btn-default" data-dismiss="modal">Edit</button>
            </div>
          </form>
        </div>

      </div>
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
      alarm: {},
      code: null,
      errors: []
    }
  },
  methods: {
    getAlarm: function() {
      axios.get(URL.rootAPI + '/ultrasonic')
      .then(res => {
        this.alarm = res.data
      })
      .catch(e => {
        this.errors.push(e)
      })
    },
    enable() {
      console.log('enabled')
      if (code == null || code == '') {
        
      }
    },
    disable() {
      console.log('disabled')
    },
    changeCode() {
      console.log("code changed")
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
    this.getAlarm()
  }
}
</script>