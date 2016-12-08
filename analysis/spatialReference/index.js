var dir = require('node-dir');
var parse = require('csv-parse');
var jsonfile = require('jsonfile');
var _ = require('underscore');

var CLICKED_OBJ_DIR = "../../data/spatialReference/clickedObj/";
var MESSAGE_DIR = "../../data/spatialReference/message/";

var clickedObjJson = [];
var messageJson = [];
var finalOut = [];

var prettyPrint = function(o, messages) {
  var out = {};

  out.gameid = o.gameid;
  out.clickTime = o.time;
  out.roundNum = o.roundNum;
  out.world = {
    red: {
      x: o.redX,
      y: o.redY,
      w: o.redW,
      h: o.redH
    },
    blue: {
      x: o.blueX,
      y: o.blueY,
      w: o.blueW,
      h: o.blueH
    },
    plaza: {
      x: o.plazaX,
      y: o.plazaY,
      d: o.plazaD
    },
    lily: {
      x: o.lilyX,
      y: o.lilyY
    }
  };
  out.click = {
    x: o.mouseX,
    y: o.mouseY
  };
  out.messages = messages;

  finalOut.push(out);
}

dir.readFiles(CLICKED_OBJ_DIR,
    function(err, content, next) {
        if (err) throw err;
        parse(content, {
          columns: true,
          trim: true,
          auto_parse: true
        }, function(err, output) {
          clickedObjJson = clickedObjJson.concat(output);
          next();
        });
    },
    function(err, files){
        if (err) throw err;
      // // console.log('finished reading files:', files);

      //   console.log(clickedObjJson);

        dir.readFiles(MESSAGE_DIR,
          function(err, content, next) {
            if (err) throw err;
              parse(content, {
                columns: true,
                trim: true,
                auto_parse: true
              }, function(err, output) {
                messageJson = messageJson.concat(output);
                next();
              });
          },
          function(err, files) {
            if (err) throw err;

            messageJson = _.filter(messageJson, function(o) { return _.isObject(o) });
            clickedObjJson = _.filter(clickedObjJson, function(o) { return _.isObject(o) });

            _.each(clickedObjJson, function(o) {
                var messages = _.filter(messageJson, function(mo) {
                  return (mo.gameid == o.gameid && mo.roundNum == o.roundNum);
                });

                prettyPrint(o, messages);
            });

            jsonfile.writeFile('joinedExperimentalData.json', finalOut, function (err) {
              console.error(err)
            })
          });
    });