let router      = require('express').Router()
let sys         = require('sys')
let child_proc  = require('child_process');
let db          = require('mongojs')('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')

router.get('/buttons', (req, res) => {
  db.buttons.find((err, buttons) => {
    if (err) console.log(err)
    res.json(buttons)
  })
})

router.post('/button', (req, res) => {
  let id = req.body.id
  let stat = req.body.status
  console.log('id: ' + id + ', status: ' + stat)

  let script = child_proc.spawn('python', ['./scripts/moc_buttons.py', id, stat])

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