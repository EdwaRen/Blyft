let googleMapsClient = require('@google/maps').createClient({
    key: 'AIzaSyBipGTaEpZxIOqSRoYJakq64x9BQNjZwJs',
    Promise: Promise
});

module.exports.getLatLng = function(address, cb){
    googleMapsClient.geocode({address})
        .asPromise()
        .then((response) => {
        let {lat, lng} = response.json.results[0].geometry.location;
        if(lat == undefined || lng == undefined){
            cb('Location not found');
        }
        cb([lat, lng]);
    });
}


