let router      = require('express').Router()
let sys         = require('sys')
let child_proc  = require('child_process');
let db          = require('mongojs')('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')

router.post('/ultrasonic-init', (req, res) => {
  let script = child_proc.spawn('python', ['./scripts/moc_ultrasonic.py'])
  
  script.stderr.on('data', (data) => {
    console.log('stderr: ${data}');
  });
  
  let status = { success: true }
  res.json(status)
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
  console.log(passcode)
  db.sensors.update({_id: db.ObjectId('5a19e631f36d280cc00ddb8f')}, {$set: {passcode: passcode}}, {}, (err, alarm) => {
    if (err) console.log(err);
    res.json({status:'success', alarm: alarm});
});
})

module.exports = router