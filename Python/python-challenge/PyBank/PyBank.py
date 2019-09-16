import os
import csv

csvpath = '../Resources/03-Python_Instructions_PyBank_Resources_budget_data.csv'

with open (csvpath, newline="") as handler:
	csvreader = csv.reader(handler, delimiter=",")
	header = next(csvreader)

	#To find total months and net total
	count_months = 0
	sum_total = 0
	my_list = []

	for row in csvreader:
		count_months+=1
		sum_total += int(row[1])
		my_list.append(int(row[1]))

	#To find average change, greates increase and decrease
	my_list_average_change = []
	sum_average_change = 0
	for i in range(len(my_list)-1):
		change = int(my_list[i+1]-my_list[i])
		sum_average_change = sum_average_change + change
		my_list_average_change.append(change)
		average_change = int(sum_average_change) / int(len(my_list_average_change))

	greatest_increase = max(my_list_average_change)
	gratest_decrease = min(my_list_average_change)

	print("Financial Analysis")
	print("______________________________")
	print(f"total months: {count_months}")
	print(f"total sum: ${sum_total}")
	print(F"Average Change: ${'%.2f' %average_change}")
	print(F"Greatest Increase in Profits: ${greatest_increase}")
	print(F"Greatest Decrease in Profits: ${gratest_decrease}")

	



	