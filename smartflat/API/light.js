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
  let s = 'python ./scripts/buttons_manager.py '+pin+' '+stat+' 1'
  child_proc.exec(s, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return;
    }
    res.json({ok:'ok'})
  });
})

module.exports = router
