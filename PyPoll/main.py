
import csv
import os

file_to_load = os.path.join("Resources", "election_data.csv")  
file_to_output = os.path.join("analysis", "election_analysis.txt")  

total_votes = 0  

VotesPerCandidate = {}

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:

        print(". ", end="")

        total_votes += 1
        if row[2] not in VotesPerCandidate:
            VotesPerCandidate[row[2]] = 1
        else:
            VotesPerCandidate[row[2]] += 1   

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

for candidate, votes in VotesPerCandidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(VotesPerCandidate, key=VotesPerCandidate.get)

print(f"Winner: {winner}")

f = open("election_results.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Votes: " + str(total_votes))
f.write('\n')
f.write("-------------------------")
f.write('\n')

for candidate, votes in VotesPerCandidate.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")
    f.write('\n')

f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}") 
f.write('\n')


