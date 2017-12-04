let router      = require('express').Router()
let sys         = require('sys')
let child_proc  = require('child_process');
let db          = require('mongojs')('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')

router.get('/luminosities', (req, res) => {  
  db.luminosities.find((err, items) => {
    if (err) console.log(err)
    res.json(items)
  })
})

router.post('/luminosity', (req, res) => {
  let status = req.body.status
  db.sensors.update({_id: db.ObjectId(id)}, {$set: {status: status}}, {}, (err, therm) => {
    if (err) console.log(err)
    console.log(therm)
    res.json({status:'success', thermometer: therm})
  })

})

module.exports = router