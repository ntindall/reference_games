import csv
import json
import os

CLICKED_OBJ_DIR = "../../data/spatialReference/clickedObj/"
MESSAGE_DIR = "../../data/spatialReference/message/"

clickedObjFiles = []
for filename in os.listdir(CLICKED_OBJ_DIR):
  clickedObjFiles.append(open(CLICKED_OBJ_DIR + filename, 'r'))

messageFiles = []
for filename in os.listdir(MESSAGE_DIR):
  messageFiles.append(open(MESSAGE_DIR + filename, 'r'))

jsonfile = open('output.json', 'w')

clickedFieldNames = ("gameid","time","roundNum","redH","redW","redX","redY","blueH","blueW","blueX","blueY","plazaD","plazaX","plazaY","lilyX","lilyY","mouseX", "mouseY")
messageFieldNames = ("gameid","time","roundNum","sender","contents")

for i, clickedObjFile in enumerate(clickedObjFiles):
  reader = csv.DictReader( clickedObjFile, clickedFieldNames)
  for row in reader:
    out = row.copy();

    messageReader = csv.DictReader(messageFiles[i], messageFieldNames)
    print row["roundNum"]
    roundNum = row["roundNum"]

    for row_prime in messageReader:
      if (row_prime["roundNum"] == row["roundNum"]):
        out.update(row_prime)
        # message is for this round, copy over
        # out["messageTime"] = row_prime["time"]
        # out["sender"] = row_prime["sender"]
        # out["contents"] = row_prime["contents"]

      else:
       if (row_prime["roundNum"] < roundNum):
        continue
       else:
        break

    print(out)
    # json.dump(row, jsonfile)
    # jsonfile.write('\n')