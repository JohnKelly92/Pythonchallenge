import csv
import sys

# Define Local Variables.
filePath = "Resources/budget_data.csv" # Path to the budget data CSV file.
totalMonths = -1 # The total number of months included in the dataset.
netTotal = 0 # The net total amount of "Profit/Losses" over the entire period.
totalChange = 0 # The changes in "Profit/Losses" over the entire period.
averageChange = 0 # The average change in "Profit/Losses" over the entire period.

greatestProfitIncrease = -sys.maxsize # The greatest increase in profits over the entire period.
greatestIncreaseMonth = 0 # The index of the month with the greatest increase in profits.
greatestProfitDecrease = sys.maxsize # The greatest decrease in profits over the entire period.
greatestDecreaseMonth = 0 # The index of the months with the greatest decrease in profits.
output = '' # The final output string.

# Open and evaluate the contents of the CSV file.
with open(filePath) as csv_file:

    reader = csv.reader(csv_file, delimiter = ',') # Define the CSV reader object.
    index = -1 # Index holds the current row of the budget data.
    prevProfit = 0 # Track the profit of the previous period to calculate profit change.

    for row in reader:
        index += 1 # Increment the current row of election data that is being evaluated.

        # Skip the header of the CSV file
        if(index == 0):
            continue

        totalMonths += 1 # Increment the total months.
        date = row[0] # The Date of the current.
        currentProfit = row[1] # The Profit/Loss of the current row.
        netTotal += int(currentProfit) # Increment netTotal by the current profit/losses

        # If we have a previous month to determine profit change.
        if(index > 1):
            currentChange = int(currentProfit) - int(prevProfit)
            totalChange += currentChange

            # Determine if the current change is the greatestProfitIncrease
            if(int(currentChange) > int(greatestProfitIncrease)):
                greatestProfitIncrease = currentChange
                greatestIncreaseMonth = row[0]

            # Determine if the current change is the greatestProfitDecrease.
            if(int(currentChange) < int(greatestProfitDecrease)):
                greatestProfitDecrease = currentChange
                greatestDecreaseMonth = row[0]

        prevProfit = currentProfit # Assign the currentProfit to prevProfit.

averageChange = '{:.2f}'.format(totalChange/totalMonths) # Calculate the average change in Profit/Loss over the entire period.

# Write the header of our results to output
output +=('Financial Analysis')
output +=('\n___________________')
output +=('\n\nTotal Months: ' + str(totalMonths))
output +=('\n\nTotal: $' + str(netTotal))
output +=('\n\nAverage Change: $' + averageChange)
output +=('\n\nGreatest Increase in Profits: ' + str(greatestIncreaseMonth) + '( $'+ str(greatestProfitIncrease) + ')')
output +=('\n\nGreatest Decrease in Profits: ' + str(greatestDecreaseMonth) + '( $'+ str(greatestProfitDecrease) + ')')

# Write the results to a text file named "Pybank Output.txt"
with open('PyBank Output.txt', 'w') as file:
    file.write(output)
file.close()

# Print the results
print(output)


        

    