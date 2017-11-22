let router      = require('express').Router()
let sys         = require('sys')
let child_proc  = require('child_process');

router.get('/refresh', (req, res) => {
  // todo: call manager to reload data & take decision
})

module.exports = router