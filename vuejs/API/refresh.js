let router      = require('express').Router()
let sys         = require('sys')
let child_proc  = require('child_process');

router.post('/refresh', (req, res) => {
  // todo: call manager to reload data & take decision
  let type = req.body.type
  let key = req.body.key
  let param = req.body.param
  let option = req.body.option

  let script = child_proc.spawn('python',['./scripts/behaviour_manager.py',type,key,param,option])
  let status ={success:null, data:null}
  script.stderr.on('data',(data)=>{
    console.log('stderr: '+ data);
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
