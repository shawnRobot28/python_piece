import json

fileName='pig_schema'
with open(fileName) as data_file:
	data = json.load(data_file)
	f = data['fields']
	for var in f:
		if(var['name'] !='t1_bad' and (var['type']==25 or var['type']==10 or var['type']==15)):
			print '\''+var['name']+'\':\''+'Numeric'+'\','
		elif(var['name']=='t1_bad'):
			print '\'t1_bad\':\'Enum\','
		else:
			print '\''+var['name']+'\':\''+'String'+'\','
