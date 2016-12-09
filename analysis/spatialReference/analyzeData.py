import json
from pprint import pprint

with open('joinedExperimentalData.json') as data_file:
	data = json.load(data_file)

print len(data)
count = 0

relevantTrials = []

for trial in data:

	def relevantTrial(trial):
		for message in trial['messages']:
			if ('in ' in message['contents']):
				print message['contents']
				return True

	if relevantTrial(trial):
		relevantTrials.append(trial)
print len(relevantTrials)
# with open('relevantExperimentalData.json', 'w') as outfile:
# 	json.dump(relevantTrials, outfile)