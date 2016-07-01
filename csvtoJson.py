import csv
import json

csvfile = open('adk.txt', 'r')
jsonfile = open('adk.json', 'w')
jsonfile.write('[\n')
x=10001
fieldnames = ("rank","name","height")
overarching={
				"model": 'blog.Mountain',
				"pk":None,
				"fields":None
			}


reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
	overarching['pk']=str(x)
	row['done']="False"
	overarching['fields']=row

	json.dump(overarching, jsonfile)
	jsonfile.write(',\n')
	x+=1

jsonfile.write(']')