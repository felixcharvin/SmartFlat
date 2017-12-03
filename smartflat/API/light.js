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

router.post('/light', (req, res) => {
  let pin = req.body.id
  let stat = req.body.status

  child_proc.exec('python ./scripts/buttons_manager.py '+pin+' '+stat+' 1', (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return;
    }
    res.send("ok")
    console.log(`stdout: ${stdout}`);
    console.log(`stderr: ${stderr}`);
  });
  

  // console.log('status: ' + stat + ', pin: ' + pin)
  // // let script = child_proc.spawn('python', ['./scripts/mocs/moc_lights.py', pin, stat, '1'])
  // let script = child_proc.spawn('python', ['./scripts/buttons_manager.py', pin, stat, '1'])

  // let status = { success: null, data: null }
  // script.stderr.on('data', (data) => {
  //   console.log('stderr: ' + data);
  //   status.success = false
  //   status.data = data
  //   res.json(status)
  // });
  // script.stdout.on('data', (data) => {
  //   console.log('stdout: ' + data);
  //   status.success = true
  //   status.data = data
  //   res.json(status)    
  // });
})

module.exports = router