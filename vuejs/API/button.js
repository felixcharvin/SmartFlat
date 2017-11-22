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

module.exports = router