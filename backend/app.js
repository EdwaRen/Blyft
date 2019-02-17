const express = require('express');
const app = express();
const mongoose = require('mongoose');
const fs = require('fs');

const db_cred = JSON.parse(fs.readFileSync('db_credentials.json'));
// let port = process.env.PORT || 80;


mongoose.connect('mongodb://localhost:27017/busroutes', {useNewUrlParser: true});


const User = mongoose.model('user', new mongoose.Schema({
    start: {
        lat: Number,
        lng: Number
    },
    end: {
        lat: Number,
        lng: Number
    }
}));

app.get('/', function(req, res){
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
    res.send('done');
});

app.get('/getRoutes', function(req, res){
    res.send("get routes")
});

app.post('/locationRequest', function(req, res){

});

// app.listen(port);

app.listen(8080, function() {
  console.log('server stared on port 8080')
});
