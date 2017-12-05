let router      = require('express').Router()
let sys         = require('sys')
let child_proc  = require('child_process');
let db          = require('mongojs')('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')

const id = "5a1f0969734d1d3ed2310a53"

router.get('/luminosities', (req, res) => {  
  db.luminosities.find((err, items) => {
    if (err) console.log(err)
    res.json(items)
  })
})

router.post('/luminosity', (req, res) => {
  let status = req.body.status
  var script = null
  if (status == 1) script = child_proc.spawn('python', ['./scripts/luminosity_sensor.py']) 
  else if (status == 0) script = child_proc.spawn('python', ['./scripts/kill_process.py', id])
  
  if (script) {
    script.stderr.on('data', (data) => {
      console.log('stderr: ' + data);
    });
  }

  setTimeout(function() { res.json({status:status}); }, 1200)
})

module.exports = router