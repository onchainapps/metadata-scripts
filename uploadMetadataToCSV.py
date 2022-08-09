# importing csv module
import csv
import json
import glob
import os


# Opening JSON file and loading the data
# into the variable data
with open('_metadata.json') as json_file:
	data = json.load(json_file)

# attribute_data = data['attributes']
# collection_data = data['collection']

# now we will open a file for writing
data_file = open('_metadata.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0


for coll in data:
	if count == 0:

		# Writing headers of CSV file
		header = coll.keys()
		csv_writer.writerow(header)
		count += 1

	# Writing data of CSV file
	csv_writer.writerow(coll.values())

data_file.close()
