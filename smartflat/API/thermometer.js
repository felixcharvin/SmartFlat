let router      = require('express').Router()
let sys         = require('sys')
let child_proc  = require('child_process');
let db          = require('mongojs')('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')

router.get('/thermometers', (req, res) => {
  db.thermometers.find((err, items) => {
    if (err) console.log(err)
    res.json(items)
  })
})

router.get('/thermometer', (req, res) => {
  db.thermometers.find().sort({date:1}).limit(1, (err, items) => {
    if (err) console.log(err)
    res.json(items[0])
  })
})

router.post('/thermometer', (req, res) => {
  let temperature = req.body.temperature
  console.log('temp: ' + temperature);
  //todo: call edit temp script
  res.json({status: 'success'})
})

module.exports = router