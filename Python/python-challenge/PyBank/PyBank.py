import os
import csv

csvpath = '../Resources/03-Python_Instructions_PyBank_Resources_budget_data.csv'

with open (csvpath, newline="") as handler:
	csvreader = csv.reader(handler, delimiter=",")

	print(csvreader)
	for row in csvreader:
		print(row)