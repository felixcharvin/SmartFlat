let router      = require('express').Router()
let sys         = require('sys')
let child_proc  = require('child_process');
let db          = require('mongojs')('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')

const id = '5a2313bcf36d285138ee0af1'

router.get('/thermometers', (req, res) => {
  db.thermometers.find((err, items) => {
    if (err) console.log(err)
    res.json(items)
  })
})

router.get('/thermometer', (req, res) => {
  db.thermometers.find().sort({$natural: -1}).limit(1, (err, items) => {
    if (err) console.log(err)
    res.json(items[0])
  })
})

router.get('/thermometer/setting', (req, res) => {
  db.sensors.findOne({_id: db.ObjectId(id)}, (err, item) => {
    if (err) console.log(err)
    console.log(item)
    res.json(item)
  })
})

router.post('/thermometer', (req, res) => {
  let status = req.body.status
  console.log('thermometer status: '+status)
  var script = null
  if (status == 1) script = child_proc.spawn('python', ['./scripts/temperature_humidity_sensor.py']) 
  else if (status == 0) script = child_proc.spawn('python', ['./scripts/kill_process.py', id])
  
  if (script) {
    script.stderr.on('data', (data) => {
      console.log('stderr: ' + data);
    });
  }

  setTimeout(function() { res.json({status:status}); }, 1000)
}) 

router.put('/thermometer', (req, res) => {
  let curTemp = req.body.curTemp
  let newTemp = req.body.newTemp
  console.log('current: ' + curTemp + ', new: ' + newTemp)

  var status = 'normal' 
  if (newTemp > curTemp) status = 'hot' 
  else if (newTemp < curTemp) status = 'cold' 
  let script = child_proc.spawn('python', ['./scripts/led_rgb_switch.py', status])
  
  db.sensors.update({_id: db.ObjectId(id)}, {$set: {settings: newTemp}}, {}, (err, therm) => {
    if (err) console.log(err)
    console.log(therm)
    res.json({status:'success', thermometer: therm})
  })

  let response = { success: null, data: null }
  script.stderr.on('data', (data) => {
    console.log('stderr: ' + data);
    response.success = false
    response.data = data
    res.json(status)
  });
  script.stdout.on('data', (data) => {
    console.log('stdout: ' + data);
    response.success = true
    response.data = data
    res.json(status)    
  });
})

module.exports = router