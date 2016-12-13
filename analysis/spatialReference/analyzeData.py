import json
from pprint import pprint

with open('joinedExperimentalData.json') as data_file:
	data = json.load(data_file)

print len(data)
count = 0

#relevantTrials = []
worlds = {}
for trial in data:
	#print trial
	trial_id = (trial['world']['red']['x'], trial['world']['red']['y'], trial['world']['blue']['x'], trial['world']['plaza']['x'], trial['world']['lily']['x'], trial['world']['lily']['y']) 
	if (worlds.get(trial_id) == None):
		worlds[trial_id] = [trial]
	else:
		worlds[trial_id].append(trial)

	def relevantTrial(trial):
		for message in trial['messages']:
			if ('just outside' in message['contents']):
				print message['contents']
				return True

	if relevantTrial(trial):
		count += 1
print len(worlds)
print count	
# for world in worlds:
# 	print world,len(worlds[world])
# with open('relevantExperimentalData.json', 'w') as outfile:
# 	json.dump(relevantTrials, outfile)