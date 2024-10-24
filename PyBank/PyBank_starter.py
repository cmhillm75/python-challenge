# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
months = []
changes = []
prev_profit_loss = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_profit_loss = int(first_row[1])
    months.append(first_row[0])

    # Process each row of data
    for row in reader:
        total_months += 1
        total_net += int(row[1])

        # Track the total and net change
        change = int(row[1]) - prev_profit_loss
        changes.append(change)  
        prev_profit_loss = int(row[1])
          
        # Calculate the greatest increase & in profits (month and amount)
        greatest_increase = max(changes)
        greatest_increase_month = months[changes.index(greatest_increase) + 1]

        # Calculate the greatest decrease in losses (month and amount)
        greatest_decrease = min(changes)
        greatest_decrease_months = months[changes.index(greatest_decrease) + 1]


# Calculate the average net change across the months
        average_change = sum(changes) / len(changes)

# Generate the output summary


# Print the output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_change:2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_months} (${greatest_decrease})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("--------------------------\n")
    txt_file.write(f"Total MonthsL {total_months}\n")
    txt_file.write(f"Total: ${total_net} \ n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_months} (${greatest_decrease})\n")