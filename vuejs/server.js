const express = require('express')
const path = require('path');
const bodyParser = require("body-parser");
const app = express();
const port = 3000

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "POST, GET, PUT, DELETE, OPTIONS");
  res.header("access-control-allow-headers", "origin, X-Requested-With, Content-Type, Accept, Access-Control-Allow-Methods, Access-Control-Allow-Origin");
  res.header("Content-Type", "application/json");
  next();
});

let ultrasonic = require('./API/ultrasonic')
let light = require('./API/light')
let effector = require('./API/effector')
app.use('/api', ultrasonic)
app.use('/api', light)
app.use('/api', effector)

app.listen(port, () => {
  console.log('Server is running on port', port);
});