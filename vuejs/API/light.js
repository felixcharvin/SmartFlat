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

router.get('/lights/frequencies', (req, res) => {
  db.lights.find({$or: [{status: 'on'}, {status: 'low'}]}).limit(1000, (err, items) => {
    if (err) console.log(err)
    res.json(items)
  })
})

router.get('/light/:location', (req, res) => {
  let location = req.params.location
  db.lights.find({location: location}).sort({date:1}).limit(1, (err, items) => {
    if (err) console.log(err)
    if (items.lenght < 1) console.log("no data found")
    res.json(items[0])
  })
})

router.post('/light', (req, res) => {
  let id = req.body.id
  let stat = req.body.status
  console.log('id: ' + id + ', status: ' + stat)

  let script = child_proc.spawn('python', ['./scripts/moc_lights.py', id, stat])

  let status = { success: null, data: null }
  script.stderr.on('data', (data) => {
    console.log('stderr: ' + data);
    status.success = false
    status.data = data
    res.json(status)  
  });
  script.stdout.on('data', (data) => {
    console.log('stdout: ' + data);
    status.success = true
    status.data = data
    res.json(status)  
  });
})

module.exports = router