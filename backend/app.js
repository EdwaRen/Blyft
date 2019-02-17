const express = require('express');
const app = express();
const mongoose = require('mongoose');
const fs = require('fs');
const path = require('path');
const gmaps = require('./gmaps.js');

gmaps.getLatLng('107 Macewan Meadow Crescent NW', function([lat, lng]){
    console.log(lat + " " + lng)
});

const db_cred = JSON.parse(fs.readFileSync('db_credentials.json'));
// let port = process.env.PORT || 80;
var bodyParser = require('body-parser')
app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
}));
app.locals.cur_locations = [['wow'], ['nice', "gneiss"]];

app.use(express.json());       // to support JSON-encoded bodies
app.use(express.urlencoded()); // to support URL-encoded bodies

var allowCrossDomain = function(req, res, next) {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
  res.header('Access-Control-Allow-Headers',
    'Content-Type, Authorization, Content-Length, X-Requested-With');

  // intercept OPTIONS method
  if ('OPTIONS' == req.method) {
    res.send(200);
  } else {
    next();
  }
};

mongoose.connect('mongodb://localhost:27017/busroutes', {useNewUrlParser: true});

const User = mongoose.model('users', new mongoose.Schema({

    start: {
        lat: Number,
        lng: Number
    },
    end: {
        lat: Number,
        lng: Number
    }
}));

// 6 handpicked destinations


app.post('/addRoute', function(req, res){
    let {startLat, startLng, endLat, endLng} = req.query;
    let obj = {
        start: {
            lat: startLat,
            lng: startLng
        },
        end: {
            lat: endLat,
            lng: endLng
        }
    };

    let newUser = new User(obj);
    newUser.save(function(err, res){
        if(err) console.log(err);
    });


    const { spawn } = require('child_process');
    const pyProg = spawn('python3', ['kmeans.py']);
    console.log("pyProg launched");

    pyProg.stdout.on('data', function(data) {
        console.log("logging data");
        // console.log(data.toString());
        // res.write(data);
        res.end('end');
    });
    console.log("end detected");

});

app.get('/getRoutes', function(req, res){
    // console.log("global variable test", req.app.locals.cur_locations);
    // // res.sendFile(path.join(__dirname + '/index.html'));
    // console.log(req.app.locals.cur_locations);

    var MongoClient = require('mongodb').MongoClient;
    var url = "mongodb://localhost:27017/";

    MongoClient.connect(url, function(err, db) {
      if (err) throw err;
      var dbo = db.db("busroutes");
      dbo.collection("return_list").find({}).toArray(function(err, result) {
        if (err) throw err;
        console.log(result);
        db.close();
        res.json(result)

      });
    });

});

app.post('/locationRequest', function(req, res){
    // console.log(req.body);
    req.app.locals.cur_locations = req.body;
    console.log("NEW");
    // console.log(req.app.locals.cur_locations);
    // console.log(req.body[0]);

    // res.send("location request")
    // res.sendFile(path.join(__dirname + '/index.html'));




    response_obj = {"res": req.body}
    res.json(response_obj);

});

// app.listen(port);

app.listen(8080, function() {
  console.log('server stared on port 8080')
});
