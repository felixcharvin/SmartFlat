let router      = require('express').Router()
let sys         = require('sys')
let child_proc  = require('child_process');

router.post('/refresh/:effector', (req, res) => {
  // todo: call manager to reload data & take decision
  let effector = req.param.effector  
  
})

module.exports = router