import csv
import sys
import customerio 

csv_name = "example.csv"
site_id = "<add your site id here>"
api_key = "<add your api key here>"

try:
	cio = customerio.CustomerIO(site_id, api_key)
	csv_reader = csv.reader( open( csv_name, 'rb' ), delimiter=',', quotechar='"' )
	csv_list = list( csv_reader )
	if ( len( csv_list ) <= 0 ):
		raise Exception("The csv file is empty")

	keys = csv_list.pop(0)

	check_keys = [key for key in keys if key.lower() == 'id']

	if len( check_keys ) <= 0:
		print "The ID key is needed!"
		raise Exception( "The ID key is needed!")

	#print keys
	objs = [ i for i in csv_list]
	results = []
	for i in csv_list:
		data = {}
		for x in range(len(keys)):
			data[keys[x].lower()] = i[x]
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
	
	
