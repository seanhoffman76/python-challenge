# PyBank Homework Assignment - Sean Hoffman

# Load Modules
import os
import csv

# Define Variables
month = 0                                                       # Variable for the total number of months
total_pl = 0                                                    # Variable for the total value of the "Profit/Losses" field
chga = 0                                                        # Variable to hold the calculated change between "Profit/Losses" for a month
hi_prof = ["",-99999999999999]                                  # List to hold the month and amount for the month and amount of the Greatest Increase (set initial change value to -99999999999999 so first value read will be greater than the initial value)
lo_prof = ["",99999999999999]                                   # List to hold the month and amount for the month and amount of the Greatest Decrease (set initial change value to 99999999999999 so first value read will be less than the initial value)
prev = 0                                                        # Variable to hold the previous month's "Profit/Losses" value for calcluation through the iterations
monthchg = []                                                   # List to append the calculated changes between "Profit/Losses" for all months

# Set path for file using the os module
budget = os.path.join('Resources', 'budget_data.csv')

# Open the CSV using the csv module and place its contents into budget_data
with open(budget, newline='') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    # Iterate through budget_data to calculate from budget_data 
    # number of months, Total P/L amount, Greatest Increase in Profits, and Greatest Decrease in Profits
    # while appending calculated Profit/Losses change data to a list named monthchg
    for row in budget_data:
        if row[0] != '':                                        # iterate through the data using the if statement to exclude any blank rows
            month = month + 1                                   # calculate the number of months by adding 1 to the previous value of month
            total_pl = total_pl + int(row[1])                   # calculate the total profit/loss value by adding the value in the "Profit/Losses" field to the previous value of total_pl
            chga = int(row[1]) - prev                           # store the value of iterated Profit/Losses minus previous month's Profit/Losses as chga
            prev = int(row[1])                                  # change the value of variable prev to the current month's Profit/Losses value
            monthchg = monthchg + [chga]                        # append the chga value to the existing list monthchg
            if chga > hi_prof[1]:                               # When the value of chga is higher than the previous calculated change between "Profit/Losses", then overwrite list hi_prof with the current month and change value.
                hi_prof[0] = row[0]
                hi_prof[1] = chga
            if chga < lo_prof[1]:                               # When the value of chga is less than the previous calculated change between "Profit/Losses", then overwrite list lo_prof with the current month and change value.
                lo_prof[0] = row[0]
                lo_prof[1] = chga
    
    avgvar = sum(monthchg[1:]) / len(monthchg[1:])              # generate the average change amount stored in list monthchg (sum / length of monthchg) starting with the second value because the first month's change value isn't compared to anything
    

# Output the analysis to the terminal    
    print('')                                                             # print a blank line
    print('-------------------------------------')                        # print a separator line
    print('Financial Analysis')                                           # print the header
    print('-------------------------------------')                        # print a separator line
    print(f'Total Months: {month}')                                       # print the total months calculated as month
    print(f'Total P/L: ${total_pl}')                                      # print the total profit/loss calculated as total_pl
    print(f'Average Change: ${avgvar:.2f}')                               # use the average function defined above to output the average monthly change and round it to two places after the decimal point
    print(f'Greatest Increase in Profits: {hi_prof[0]} ${hi_prof[1]}')    # output the month and amount for the MAX value in monthChg
    print(f'Greatest Decrease in Profits: {lo_prof[0]} ${lo_prof[1]}')    # output the month and amount for the MIN value in monthChg

# Output the analysis to a CSV file in the same format as above
    # Set variable for output file
output_file = os.path.join("PyBank_Analysis.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow([''])
    writer.writerow(['Financial Analysis'])
    writer.writerow(['-------------------------------------'])
    writer.writerow([f'Total Months: {month}'])
    writer.writerow([f'Total P/L: ${total_pl}'])
    writer.writerow([f'Average Change: ${avgvar:.2f}'])
    writer.writerow([f'Greatest Increase in Profits: {hi_prof[0]} ${hi_prof[1]}'])
    writer.writerow([f'Greatest Decrease in Profits: {lo_prof[0]} ${lo_prof[1]}'])

# End of homework assignment PyBank