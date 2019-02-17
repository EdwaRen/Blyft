const express = require('express');
const app = express();
const mongoose = require('mongoose');
const fs = require('fs');

const db_cred = JSON.parse(fs.readFileSync('db_credentials.json'));
let port = process.env.PORT || 80;

mongoose.connect(`mongodb+srv://${db_cred.username}:${db_cred.password}@busroutes-hd8th.mongodb.net/BusPool`, { useNewUrlParser: true });

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
    res.send();
});

app.get('/getRoutes', function(req, res){

});

app.post('/locationRequest', function(req, res){

});

app.listen(port);
