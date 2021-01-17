import pathlib
import csv

# #
# # PyPoll
# #
poll_csv = pathlib.Path('election_data.csv')


khan_count = 0
correy_count = 0
li_count = 0
tooley_count = 0

with open(poll_csv) as poll_file:
    print(poll_file)
    reader2 = csv.reader(poll_file)
    headers = next(reader2)


# # The total number of votes cast
    for row in reader2: 
        if row [2] == "Khan":
            khan_count = khan_count + 1   
        elif row [2] == "Correy":
            correy_count = correy_count +1
        elif row [2] == "Li":
            li_count = li_count +1  
        else:
            tooley_count = tooley_count +1  

# # A complete list of candidates who received votes
total_votes = khan_count + correy_count + li_count + tooley_count
#print(total_votes)
# # The percentage of votes each candidate won
khan_percent = (khan_count / total_votes)*100
correy_percent  = (correy_count / total_votes)*100
li_percent  = (li_count / total_votes)*100
tooley_percent  = (tooley_count / total_votes)*100

#print(tooley_percent)

candidate_list = [khan_count, correy_count, li_count, tooley_count]

if candidate_list.index(max(candidate_list)) == 0:
    winner = "Khan"
elif candidate_list.index(max(candidate_list)) == 1:
    winner = "Correy"
elif candidate_list.index(max(candidate_list)) == 2:
    winner = "Li"
else:
    winner = "Tooley"

# # The winner of the election based on popular vote.

print(f"Election Results")
print(f"_________________")
print(f"Total Votes: {total_votes}")
print(f"_________________")
print(f"Khan: {khan_percent:.3f}% ({khan_count})")
print(f"Correy: {correy_percent:.3f}% ({correy_count})")
print(f"Li: {li_percent:.3f}% ({li_count})")
print(f"Tooley: {tooley_percent:.3f}% ({tooley_count})")
print(f"_________________")
print(f"Winner: {winner}")
print(f"_________________")


#output

# Specify the file to write to
output_path = pathlib.Path("pypoll_output.csv")

# # # Open the file using "write" mode. Specify the variable to hold the contents
with open(file=output_path, mode='w') as csvfile:

# #     # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
# ​
#     # Write the first row (column headers)
    csvwriter.writerow(['Total Votes','Khan Votes', 'Khan Percent', 'Correy Count', 'Correy Percent', 'Li Count', 'Li Percent', 'Tooley Count', 'Tooley Percent', 'Winner'])
    
#     # Fill in the data rows
    csvwriter.writerow([total_votes,khan_count,khan_percent,correy_count,correy_percent,li_count,li_percent, tooley_count, tooley_percent, winner])
