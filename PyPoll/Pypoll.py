#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

#You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:

#* The total number of votes cast

#* A complete list of candidates who received votes

#* The percentage of votes each candidate won

#* The total number of votes each candidate won

#* The winner of the election based on popular vote.

#Import the Necessary Modules
import os
import csv

#Allow Python to locate the .csv file
poll_data = os.path.join('Resources','election_data.csv')

#Create a list to store ballot ids which we shall use to determine total vote count.
#Declare a variable to hold total amount of votes.
ballot_id = []
tot_vote = 0

#Similarly create a list to store the county.
county = []

#Create lists to hold candidate name and votes that we won individually. We can use this to determine
#Votes each candidate gone, the percentage and ultimately the winner of the ELECTION!
candidate = []
each_candidate = []
each_vote=[]
cand_vote = []

#Create a list to hold the percentage attributed to each candidate
tot_percent = []

#set initial vote count to zero
cand_vote_count = 0

#Allow Python to read the .csv file that we previously enabled the os to locate
with open(poll_data,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    df_header = next(csvreader)

    #Initiate a For loop to begin storing the values into their appropriate lists
    for row in csvreader:

        #Store ballot ids into our list as integers.
        ballot_id.append (int(row[0]))

        #Candidate and county name can be strings
        county.append (str(row[1]))
        candidate.append (str(row[2]))

        #We can calculate the total amount of votes by just outputting the lenght of the ballot id list
        tot_vote = len(ballot_id)

        #Variable to hold candidate vote count
        cand_vote_count = cand_vote_count + 1

        #We can run a for loop within a set to islate the values and attribute them to their respective candidates
    for x in set(candidate):
        each_candidate.append(x)
        y = candidate.count(x)
        cand_vote.append(y)

        #In order to gain the percent we can divide the votes a single candidate got by the total and multiply by 100
        z = ((y/cand_vote_count)*100)
        
        tot_percent.append(z)

    #We can calculate the winner by indentifying the max value of the individual votes we separated    
    winner_count = max(cand_vote)
    #We can print the name of the winner by addressing the indez in the winner count list
    winner = each_candidate[cand_vote.index(winner_count)]

print("Election results")
print("-------------------------------------------------------------")
print(f"Total Vote count: {str(tot_vote)}")
#We need to run a loop to display the candidate names with the amount if votes they got and percentages
for i in range(len(each_candidate)):
    print(f"Candidate:  {(each_candidate) [i]} : {(tot_percent)[i]}% {(cand_vote)[i]}")
print("-------------------------------------------------------------")
print(f"AND THE WINNER IS {winner}!!")
print("-------------------------------------------------------------")

with open('election_results.txt', 'w') as text:
    text.write("Election results" + "\n")
    text.write("-------------------------------------------------------------\n")
    text.write(f"Total Vote count: {str(tot_vote)}" +"\n")
    for i in range(len(each_candidate)):
        text.write(f"Candidate:  {(each_candidate) [i]} : {(tot_percent)[i]}% {(cand_vote)[i]}" + "\n")
    text.write("-------------------------------------------------------------\n")
    text.write(f"AND THE WINNER IS {winner}!!" + "\n")
    text.write("-------------------------------------------------------------\n")

