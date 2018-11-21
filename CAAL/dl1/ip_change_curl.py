import csv
import argparse
import requests
import time

parser = argparse.ArgumentParser(description='Script to change Digital Logger network info')
parser.add_argument("-csv", dest='csv', required=True, help='CSV files containing all Digital logger info to be changed')

args = parser.parse_args()

with open(args.csv) as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
    	command = "http://admin:1234@{}/network.cgi?netmask={}&gateway={}".format(row[0],row[1],row[2])
    	resp = requests.get(command)
    	if resp != None:
			print("Gateway and Netmask changed successfully")
			print resp
    	time.sleep(2)