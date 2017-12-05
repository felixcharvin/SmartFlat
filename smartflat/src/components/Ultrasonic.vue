<template>
  <div class="panel panel-default">
    <div class="panel-heading">Alarm</div>
    <div class="panel-body">
      <div class="alert" v-bind:class="{'alert-danger':alarm && alarm.status=='off', 'alert-success':alarm && alarm.status=='on'}">
        <div class="row">
          <div class="col-xs-6">Status:</div>
          <div v-if="alarm" class="col-xs-6 text-right"><b>{{ alarm.status.toUpperCase() }}</b></div>
        </div>
      </div>
      <hr>
      <form>
        <div class="form-group">
          <label class="sr-only" for="code"></label>
          <div class="input-group">
            <div class="input-group-addon"><span class="glyphicon glyphicon-lock" aria-hidden="true"></span></div>
            <input type="number" v-model="code" class="form-control" id="code" placeholder="pass code">
          </div>
        </div>
        <div v-if="passcodeError" class="col-xs-12">
          <div class="alert alert-danger" role="alert">Incorrect passcode</div>
        </div>
        <button v-if="alarm && alarm.status == 'off'" type="reset" class="btn btn-default" @click="enable()">Enable</button> 
        <button v-if="alarm && alarm.status == 'on'" type="reset" class="btn btn-danger" @click="disable()">Disable</button>
        <button type="button" class="btn btn-info" data-toggle="modal" data-target="#myModal">Edit Passcode</button>
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
          <form class="form-horizontal">
            <div class="modal-body">
              <div class="form-group">
                <label class="col-xs-4 control-label" for="old-pass">Old passcode: </label>
                <div class="col-xs-8">
                  <input type="text" id="old-pass" class="form-control" v-model="oldCode" placeholder="Old pass code">
                </div>
              </div>
              <div class="form-group">
                <label class="col-xs-4 control-label" for="new-pass">New passcode: </label>
                <div class="col-xs-8">
                  <input type="text" id="new-pass" class="form-control" v-model="newCode" placeholder="New pass code">
                </div>
              </div>
              <div class="form-group">
                <label class="col-xs-4 control-label" for="new-pass2">Repeat new passcode: </label>
                <div class="col-xs-8">
                  <input type="text" id="new-pass2" class="form-control" v-model="newCode2" placeholder="Repeat new pass code">
                </div>
              </div>
            </div>
            <div v-if="changePasscodeSuccess" class="col-xs-12">
              <div class="alert alert-success" role="alert">Passcode changed</div>
            </div>
            <div v-if="changePasscodeError" class="col-xs-12">
              <div class="alert alert-danger" role="alert">
                <ul v-for="error in errors">
                  <li>{{ error }}</li>
                </ul>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" @click="changeCode()" class="btn btn-primary">Edit</button>
              <button @click="closeModal()" class="btn btn-default" data-dismiss="modal">Close</button>
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
      alarm: null,
      code: null,
      oldCode: null,
      newCode: null,
      newCode2: null,
      passcodeError: false,
      changePasscodeError: false,
      changePasscodeSuccess: false,
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
      if (this.code == this.alarm.passcode) {
        //todo: enable alarm
        this.passcodeError = false
        this.alarm.status = 'on'
        this.code = null
        this.init('enable')
      }
      else this.passcodeError = true
    },
    disable() {
      if (this.code == this.alarm.passcode) {
        //todo: disable alarm
        this.passcodeError = false
        this.alarm.status = 'off'
        this.code = null
        this.init('disable')
      }
      else this.passcodeError = true
    },
    changeCode() {
      this.errors = []
      if (this.oldCode != this.alarm.passcode) this.errors.push("Old passcode incorrect")
      if (this.newCode == null || this.newCode && this.newCode.length != 4) this.errors.push("Passcode must have 4 digits numbers")
      if (this.newCode != this.newCode2) this.errors.push("Passcode and confirmation do not match")
      if (this.errors.length > 0) this.changePasscodeError = true
      else {
        this.changePasscodeError = false
        axios.put(URL.rootAPI + '/ultrasonic/passcode', {passcode: this.newCode})
        .then(res => {
          this.changePasscodeSuccess = true
          this.alarm.passcode = this.newCode
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
    closeModal() {
      this.changePasscodeError = false
      this.changePasscodeSuccess = false
      this.errors = []
    },
    init: function(status) {
      axios.post(URL.rootAPI + '/ultrasonic', {status:status})
      .then(res => {
        // console.log(res)
      })
      .catch(e => {
        console.log(e)
      })
    }
  },
  created() {
    this.getAlarm()
  }
}
</script>