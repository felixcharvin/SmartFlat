let router      = require('express').Router()
let sys         = require('sys')
let child_proc  = require('child_process');
let db          = require('mongojs')('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')

router.get('/lights', (req, res) => {
  db.lights.find().toArray((err, items) => {
    if (err) console.log(err)
    res.json(items)
  })
})

router.get('/lights/count/:hour', (req, res) => {
  let hour = ' '+req.params.hour+':'
  let regex = new RegExp(hour)

  db.lights.count({date: regex, status: 'on'}, (err, count) => {
    if (err) console.log(err)
    res.json(count)
  })
})

router.get('/lights/frequencies', (req, res) => {
  db.lights.find({$or: [{status: 'on'}, {status: 'low'}]}).limit(1000, (err, items) => {
    if (err) console.log(err)
    res.json(items)
  })
})

router.get('/light/:location', (req, res) => {
  let location = req.params.location
  let regex = new RegExp("on|low")  
  db.lights.find({location: location}).sort({date:1}).limit(1, (err, items) => {
    if (err) console.log(err)
    res.json(items)
  })
})

router.post('/light/:id/:status', (req, res) => {
  let id = req.params.id
  let stat = req.params.status
  console.log('id: ' + id + ', status: ' + stat)
  let script = child_proc.spawn('python', ['./scripts/moc_light.py', id, stat])

  let status = { success: true, data: {} }
  script.stderr.on('data', (data) => {
    console.log('stderr: ' + data);
    status.success = false
    status.data = data
  });
  script.stdout.on('data', (data) => {
    console.log('stderr: ' + data);
    status.success = true
    status.data = data
  });
  res.json(status)  
})

module.exports = router