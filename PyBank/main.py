
import csv
import os
import statistics

file_to_load = os.path.join("Resources", "budget_data.csv")  
file_to_output = os.path.join("analysis", "budget_analysis.txt")  

total_months = 0
total_net = 0

MonthCount = 0
TotalVolume = 0
GreatestIncrease = 0
BestMonth = ''
GreatestDecrease = 0
WorstMonth = ''

change = []
MonthToMonthChange = []

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    header = next(reader)

    for row in reader:

        MonthCount += 1
        TotalVolume += int(row[1])
        if int(row[1]) > GreatestIncrease:
            BestMonth = (row[0])
            GreatestIncrease = int(row[1])
        elif int(row[1]) < GreatestDecrease:
            WorstMonth = (row[0])
            GreatestDecrease = int(row[1])
        change.append(int(row[1]))

for i in range(len(change)-1):
    MonthlyChange = (change[i+1] - change[i])
    MonthToMonthChange.append(MonthlyChange)   

AverageChange = statistics.mean(MonthToMonthChange)

print("Financial Analysis")
print("___________________________________")

print("Total Months: " + str(MonthCount))
print("Average Change is: $" + str(round(AverageChange, 2)))
print("Total: $" + str(TotalVolume))
print("Greatest Increase in Profits: " + str(BestMonth) + "  ($" + str(GreatestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(WorstMonth) + "  ($" + str(GreatestDecrease) + ")")

f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write("___________________________________")

f.write("Total Months: " + str(MonthCount))
f.write("Average Change is: $" + str(round(AverageChange, 2)))
f.write("Total: $" + str(TotalVolume))
f.write("Greatest Increase in Profits: " + str(BestMonth) + "  ($" + str(GreatestIncrease) + ")")
f.write("Greatest Decrease in Profits: " + str(WorstMonth) + "  ($" + str(GreatestDecrease) + ")")


