import json
from pprint import pprint

with open('relevantExperimentalData.json') as data_file:
	data = json.load(data_file)

print len(data)
count = 0

#relevantTrials = []
worlds = {}
for trial in data:
	print trial
	trial_id = trial['world']
	if (worlds.get(trial_id) == None):
		worlds[trial_id] = [trial]
	else:
		worlds[trial_id].append(trial)
	# def relevantTrial(trial):
	# 	for message in trial['messages']:
	# 		if ('in ' in message['contents']):
	# 			print message['contents']
	# 			return True

	
for world in worlds:
	print world,len(worlds[world])
# with open('relevantExperimentalData.json', 'w') as outfile:
# 	json.dump(relevantTrials, outfile)