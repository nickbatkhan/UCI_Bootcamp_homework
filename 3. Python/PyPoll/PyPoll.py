import os
import csv

csvpath = '../Resources/03-Python_Instructions_PyPoll_Resources_election_data.csv'

with open (csvpath, newline="") as handler:
	csvreader = csv.reader(handler, delimiter=",")
	header = next(csvreader)

	total_votes = 0
	khan_votes = 0
	correy_votes = 0
	li_votes = 0
	otooley_votes = 0
	my_list= []
	for row in csvreader:
		total_votes = total_votes + 1
		if "Khan" in row:
			khan_votes = khan_votes + 1
		if "Correy" in row:
			correy_votes = correy_votes + 1
		if "Li" in row:
			li_votes = li_votes + 1
		if "O'Tooley" in row:
			otooley_votes = otooley_votes + 1
		khan_percentage = int(khan_votes)*100/int(total_votes)
		correy_percentage = int(correy_votes)*100/int(total_votes)
		li_percentage = int(li_votes)*100/ int(total_votes)
		otooley_percentage = int(otooley_votes)*100/int(total_votes)
		my_list.append(khan_votes)
		my_list.append(correy_votes)
		my_list.append(li_votes)
		my_list.append(otooley_votes)
		winnter = max(my_list)


print("Election Result")
print("_____________________")
print(f"Total Votes: {total_votes} ")
print("_____________________")
print(f"Khan: {'%.3f' %khan_percentage}% ({khan_votes})")
print(f"Correy: {'%.3f' %correy_percentage}% ({correy_votes})")
print(f"Li: {'%.3f' %li_percentage}% ({li_votes})")
print(f"O'Tooley: {'%.3f' %otooley_percentage}% ({otooley_votes})")
print(f"Winner: {winner}")


