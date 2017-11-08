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

router.get('/light/:id', (req, res) => {
  let id = req.params.id
  console.log('id: ' + id)
  res.send(id)
})

router.post('/light/:id/:status', (req, res) => {
  
})

module.exports = router