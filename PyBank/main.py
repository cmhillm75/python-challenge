# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "budget_analysis.txt")  # Output file path

# Create the variables to track the financial data.
# Months, totals, profits/loss begin at 0 to ensure no previous data is present.
# Changes and months need to be lists to store constantly changing data.
total_months = 0
total_net = 0
changes = []
prev_profit_loss = 0
months = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list.
    first_row = next(reader)
    total_months = total_months + 1
    total_net += int(first_row[1])
    prev_profit_loss = int(first_row[1])
    months.append(first_row[0])

    # Process the data 1 row at a time.
    for row in reader:
        total_months = total_months + 1
        total_net += int(row[1])

        # Track the total and net change
        change = int(row[1]) - prev_profit_loss
        changes.append(change)  
        prev_profit_loss = int(row[1])

        # Count the number months
        months.append(row[0])

    # Calculate the average net change across the months, need to round to 2 decimals. 
    # Need to add the amounts in column 2, get the total change amounts and divide by the number of rows - 1.
        average_change = round(sum(changes) / len(changes), 2) if changes else 0
          
        # Calculate the greatest increase & decrease in profits (month and amount)
        # Utilized if statements to obtain a value for greatest increase/decrease months
        # code was stopping as the value was out of range. 
    if changes:
        greatest_increase = max(changes)
        greatest_decrease = min(changes)
        greatest_increase_month = months[changes.index(greatest_increase) + 1]
        greatest_decrease_month = months[changes.index(greatest_decrease) + 1]
    else:
        greatest_increase_month = greatest_decrease = 0
        greatest_increase_month = greatest_decrease_month = None
         
# Print the output to gitbash terminal - change to show 2 decimals on avg.
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_change:.2f}")
if greatest_increase_month and greatest_decrease_month:
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("--------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net} \n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    if greatest_increase_month and greatest_decrease_month:
        txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
        txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")            