

// const express = require('express');
// const app = express();
const mongoose = require('mongoose');
var path = require('path');

// let port = process.env.PORT || 80;

// mongoose.connect(`mongodb+srv://${db_cred.username}:${db_cred.password}@busroutes-hd8th.mongodb.net/BusPool`, { useNewUrlParser: true });
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

data = [[51.0099, -114.0670],
[51.0782, -114.1358],
[51.0452, -114.0811],
[51.0409, -114.0550],
[51.0379, -114.0532],
[51.0454, -114.0550],
[51.0436, -114.0783],
[51.0633, -114.0645],
[51.0666, -114.0539],
[51.0494, -114.0615],
[51.0848, -114.1555],
[50.9985, -114.0733],
[51.2033, -113.9931],
[50.9530, -114.0659],
[51.0460, -114.0698],
[51.0450, -114.0611],
[51.0443, -114.0631],
[51.0450, -114.0618],
[51.0459, -114.0590],
[51.0479, -114.0619],
[51.0476, -114.0621],
[51.0539, -114.0790],
[51.0559, -114.0700],
[51.1595, -114.0655],
[51.0345, -114.0633],
[51.1126, -114.0652],
[51.1215, -114.0076],
[51.0459, -114.0237],
[51.0537, -114.0248],
[51.0856, -114.3562],
[51.0469, -114.0560],
[51.0640, -114.0885],
[51.0165, -114.0391],
[51.0187, -114.0475],
[51.0071, -114.1464],
[50.9495, -113.9832],
[51.1095, -114.1089],
[51.0633, -114.1557],
[51.0464, -114.0691],
[51.0972, -114.2169]
]

for (var i = 0; i < data.length; i++){

  let obj = {
      start: {
          lat: data[i][0],
          lng: data[i][1]
      },
      end: {
          lat: data[i][0],
          lng: data[i][1]
      }
  };


  let newUser = new User(obj);
  newUser.save(function(err, res){
      if(err) console.log(err);
      console.log("res", res);
  });

  console.log("end detected", i, obj);

}

console.log("DONE");
