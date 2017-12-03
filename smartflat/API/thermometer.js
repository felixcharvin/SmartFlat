let router      = require('express').Router()
let sys         = require('sys')
let child_proc  = require('child_process');
let db          = require('mongojs')('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')

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

router.post('/thermometer', (req, res) => {
  let oldTemp = req.body.oldTemp
  let newTemp = req.body.newTemp
  console.log('old: ' + oldTemp + ', new: ' + newTemp)

  var status = 'normal' 
  if (newTemp > oldTemp) status = 'hot' 
  else if (newTemp < oldTemp) status = 'cold' 
  let script = child_proc.spawn('python', ['./scripts/led_rgb_switch.py', status])
  
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