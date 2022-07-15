## PyBank Instructions

#In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: "Date" and "Profit/Losses". (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

#Your task is to create a Python script that analyzes the records to calculate each of the following:

#* The total number of months included in the dataset

#* The net total amount of "Profit/Losses" over the entire period

#* The changes in "Profit/Losses" over the entire period, and then the average of those changes

#* The greatest increase in profits (date and amount) over the entire period

#* The greatest decrease in profits (date and amount) over the entire period

#Import the necessary modules.
import os
import csv
from numpy import average

from sqlalchemy import LABEL_STYLE_DISAMBIGUATE_ONLY

#Allow Python to locate the .csv file
bank_data = os.path.join('Resources','budget_data.csv')

#Declare a variable to hold total Profit/Loss and a list to hold the values of Profit/Loss
total_p = 0
profit = []

#Declare a variable to hold the change in dates and the total number of months and list them appropriately
m_change = 0
last_m = 0
months = []

#Allow Python to read the .csv file we located
with open(bank_data,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    df_header = next(csvreader)
#Loop Through the list adding appropriate values to their respective lists
    for row in csvreader:
        months.append(row[0])
        profit.append(row[1])

        #Total months can be determined by grabbing the value of the length of the list.
        total_month = len(months)

        #Total Profit/Loss can be determined by added up the values stored in the second row of the file.
        total_p = total_p + int(row[1])

    #In order to calculate change in profit, we subtract the second row from the first and store their values respectively.
    profit = [int(i) for i in profit]
    change = [profit[i+1] - profit[i] for i in range(len(profit)-1)]

    #Then we take the sum total of the change in profit that we stored and divide it by the lenght of the list to gain AVERAGE PROFIT
    avg_p = sum(change)/len(change)

    #Round the result to 2 decimal places
    avg_p = round(avg_p,2)

    #Our Greatest Profit can be aquired through pulling the max value of individual profits we stored
    Greatest_i = max(change)

    #Similarly we can aquire the Greatest Loss through the min value
    Greatest_d = min(change)
    
    #We can display the dates of the values above by referencing their respective date in correspondance to the we Greatest Profit/Loss
    i_date = months[change.index(Greatest_i)]
    d_date = months[change.index(Greatest_d)]
    
        


#Final Print on the Terminal to display our results

print("Financial Analysis")
print("-----------------------------------------")
print(f"Total Months:   {str(total_month)}")
print(f"Total Profit: ${str(total_p)}")
print(f"Average Profit: ${str(avg_p)}")
print(f"Greatest Increase in Profit: {i_date} ${Greatest_i} ")
print(f"Greatest Loss: {d_date} ${Greatest_d}")
print("------------------------------------------")

#Exporting the results into a .txt file

with open('bank_data.txt', 'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("-----------------------------------------\n")
    text.write(f"Total Months:   {str(total_month)}"+"\n")
    text.write(f"Total Profit: ${str(total_p)}"+"\n")
    text.write(f"Average Profit: ${str(avg_p)}"+"\n")
    text.write(f"Greatest Increase in Profit: {i_date} ${Greatest_i}"+"\n ")
    text.write(f"Greatest Loss: {d_date} ${Greatest_d}"+"\n")
    text.write("------------------------------------------\n")

















