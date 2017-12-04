let router      = require('express').Router()
let sys         = require('sys')
let child_proc  = require('child_process');
let db          = require('mongojs')('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')

const id = '5a19e631f36d280cc00ddb8f'

router.post('/ultrasonic', (req, res) => {
  let status = req.body.status
  var script = null
  if (status == 'enable') script = child_proc.spawn('python', ['./scripts/alarm_sensor.py']) 
  else if (status == 'disable') script = child_proc.spawn('python', ['./scripts/kill_process.py', id])
  
  res.json({success:true})
})

router.get('/ultrasonic', (req, res) => {
  db.sensors.findOne({name: 'Alarm'}, (err, item) => {
    if (err) console.log(err)
    res.json(item)
  })
})

router.get('/ultrasonics', (req, res) => {
  db.ultrasonics.find().toArray((err, items) => {
    if (err) console.log(err)
    res.json(items)
  })
})

router.put('/ultrasonic/passcode', (req, res) => {
  let passcode = req.body.passcode
  db.sensors.update({_id: db.ObjectId(id)}, {$set: {passcode: passcode}}, {}, (err, alarm) => {
    if (err) console.log(err)
    res.json({status:'success', alarm: alarm})
  })
})

module.exports = router