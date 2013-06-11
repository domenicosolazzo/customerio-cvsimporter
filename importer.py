import csv
import sys


csv_name = "example.csv"
try:
	csv_reader = csv.reader( open( csv_name, 'rb' ), delimiter=',', quotechar='"' )
	csv_list = list( csv_reader )
	if ( len( csv_list ) <= 0 ):
		raise Exception("The csv file is empty")

	keys = csv_list.pop(0)

	print keys
	objs = [ i for i in csv_list]
	results = []
	for i in csv_list:
		data = {}
		for x in range(len(keys)):
			data[keys[x]] = i[x]
		results.append(data)
	print results
except IOError, e:
	print("The input file ({0}) was missing. Error({1}): {2}".format(csv_name,e.errno, e.strerror))
	raise e
except csv.Error, e:
	print("Error opening the csv file. Error: %s" % (str(e), ))
	raise e
	
