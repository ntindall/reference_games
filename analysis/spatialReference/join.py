var dir = require('node-dir');
var csv = require('parse-csv');

var CLICKED_OBJ_DIR = "../../data/spatialReference/clickedObj/";
var MESSAGE_DIR = "../../data/spatialReference/message/";

console.log("hey");

dir.readFiles(CLICKED_OBJ_DIR,
    function(err, content, next) {
        if (err) throw err;
        console.log('content:', content);
        next();
    },
    function(err, files){
        if (err) throw err;
        console.log('finished reading files:', files);
    });