import pathlib
import csv
#
# PyBank
#
bank_csv = pathlib.Path('budget_data.csv')

with open(bank_csv) as csv_file:
    print(csv_file)
    reader = csv.reader(csv_file)
    headers = next(reader)
    dates = []
    profit =[]
# The total number of months included in the dataset
    for row in reader: 
        dates.append(row[0])
        profit.append(int(row[1]))

        
# print(dates)
# print(profit)
       
   # date = csv_file[0]
    #profit = csv_file[1]

# The net total amount of "Profit/Losses" over the entire period
# sum_profit = sum(profit)
# print(sum_profit)

# The average of the changes in "Profit/Losses" over the entire period
changes = [profit[i + 1] - profit[i] for i in range(len(profit)-1)]

# Perform calculations on the lists we created
total_profit = round(sum(profit))
date_length = len(dates)
avg_change = round(sum(changes)/len(changes),2)
max_change = round(max(changes)) 
max_index = changes.index(max_change)  
max_index_date = dates[max_index+1]
min_change = round(min(changes))
min_index = changes.index(min_change) 
min_index_date = dates[min_index+1]

print(min_index)

#print results

print(f"Financial Analysis")
print("-----------------")
print(f"Total Months: {date_length}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_index_date} (${max_change})")
print(f"Greatest Decrease in Profits: {max_index_date} (${min_change})")
print("-----------------")


# Specify the file to write to
output_path = pathlib.Path("pybank_output.csv")

# # # Open the file using "write" mode. Specify the variable to hold the contents
with open(file=output_path, mode='w') as csvfile:

# #     # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
# ​
#     # Write the first row (column headers)
    csvwriter.writerow(['Total months', 'Total', 'Average Change', 'Greatest_Increase in Profits_Date', 'Greatest Increase in Profits', 'Greatest Decrease in Profits Date', 'Greatest Decrease in Profts'])
    
#     # Fill in the data rows
    csvwriter.writerow([date_length,total_profit,avg_change,max_index_date,max_change,min_index_date,min_change])

