import os
import csv
import statistics

dirname = os.path.dirname(__file__)

budget_data_csv = os.path.join(dirname, "Resources/budget_data.csv")

with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    

    totalMonths = 0
    totalPL = 0
    changes = []
    dates = []
    PL = 0
    # Loop through the data
    for row in csvreader:
        if totalMonths != 0:
            changes.append(int(row[1]) - PL)    

        dates.append(row[0])
        PL = int(row[1])
        
        totalMonths += 1
        totalPL += PL 

    GreatInc = max(changes)
    GreatDec = min(changes)
    GreatIncIdx = changes.index(GreatInc)
    GreatDecIdx = changes.index(GreatDec)

        
    print(f'Total Months: {totalMonths}')
    print(f'Total: ${totalPL}')
    print(f'Average Change:  ${statistics.mean(changes)}')
    print(f'Greatest Increase in Profits: {dates[GreatIncIdx + 1]}  ${GreatInc}')
    print(f'Greatest Decrease in Profits: {dates[GreatDecIdx + 1]}  ${GreatDec}')

output_file = os.path.join(dirname, "Analysis/PyBank.txt")

lines = ['Financial Analysis', '-------------------', f'Total Months: ${totalMonths}', f'Total: ${totalPL}', f'Average Change:  ${statistics.mean(changes):.2f}', f'Greatest Increase in Profits: {dates[GreatIncIdx + 1]} (${GreatInc})', f'Greatest Decrease in Profits: {dates[GreatDecIdx + 1]} (${GreatDec})']
#  Open the output file
with open(output_file, "w") as Analysis:
   
    Analysis.write('\n'.join(lines))