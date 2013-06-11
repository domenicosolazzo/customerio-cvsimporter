import csv
import sys
import customerio 

csv_name = "example.csv"
site_id = "67791824ca146a14ee53"
api_key = "23044f477b3963e28b83"

try:
	cio = customerio.CustomerIO(site_id, api_key)
	csv_reader = csv.reader( open( csv_name, 'rb' ), delimiter=',', quotechar='"' )
	csv_list = list( csv_reader )
	if ( len( csv_list ) <= 0 ):
		raise Exception("The csv file is empty")

	keys = csv_list.pop(0)

	#print keys
	objs = [ i for i in csv_list]
	results = []
	for i in csv_list:
		data = {}
		for x in range(len(keys)):
			data[keys[x]] = i[x]
		results.append(data)
	#print results
	for customer in results:
		cio.identify(**customer)
except IOError, e:
	print("The input file ({0}) was missing. Error({1}): {2}".format(csv_name,e.errno, e.strerror))
	raise e
except csv.Error, e:
	print("Error opening the csv file. Error: %s" % (str(e), ))
	raise 
except customerio.CustomerIOException, e:
	print("Error using the Customer.io library. Error: %s" % (e.message, ))
	
	
