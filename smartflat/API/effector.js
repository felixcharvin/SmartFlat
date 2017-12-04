let router      = require('express').Router()
let sys         = require('sys')
let child_proc  = require('child_process');
let db          = require('mongojs')('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')

router.get('/effectors', (req, res) => {
  db.effectors.find().toArray((err, items) => {
    if (err) console.log(err)
    res.json(items)
  })
})

router.get('/sensors', (req, res) => {
  db.sensors.find().toArray((err, items) => {
    if (err) console.log(err)
    res.json(items)
  })
})


module.exports = router