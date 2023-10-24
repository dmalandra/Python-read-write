import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("Analysis", "budget_summary.txt")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    total_months = 0
    profit_loss = 0

    previous_profit = 0
    delta_profit = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 999999999999]

    delta_profit_loss = []

# Calculate total months
    for row in csvreader:
        total_months += 1
        profit_loss += int(row[1])

# Track changes in profit/loss
        delta_profit = int(row[1]) - previous_profit

# Find greatest increase and decrease
        if delta_profit > greatest_increase[1]:
            greatest_increase[1] = delta_profit
            greatest_increase[0] = row[0]

        if delta_profit < greatest_decrease[1]:
            greatest_decrease[1] = delta_profit
            greatest_decrease[0] = row[0]

# Append profit/loss list
        delta_profit_loss.append(int(row[1]))

# Calcluate average profit/loss
    average = round(sum(delta_profit_loss)/len(delta_profit_loss), 2)

print(f"Financial Analysis")
print(f"------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${profit_loss}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write to text file
with open(output_file, 'w') as text:
    text.write(f"Financial Analysis\n")
    text.write(f"-----------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Average Change: ${average}\n")
    text.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    text.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")



        


