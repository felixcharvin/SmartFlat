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

router.get('/lights/status', (req, res) => {

})

router.post('/lights/:id/:status', (req, res) => {
  
})

module.exports = router