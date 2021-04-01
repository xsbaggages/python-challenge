import os
import csv

def print_list(string, slist):
    print(string)
    slist.append(string)

    return slist

dirname = os.path.dirname(__file__)

election_data_csv = os.path.join(dirname, "Resources/election_data.csv")

with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    totalVotes = 0
    candidates = {}

    
    # Loop through the data
    for row in csvreader:
        name = row[2]   
        
        if name in candidates:
            candidates[name] += 1
        else: 
            candidates[name] = 1
        
        totalVotes += 1

    lines = []
    lines = print_list('Election Results', lines)
    lines = print_list('--------------------------', lines)
    lines = print_list(f'Total Votes: {totalVotes}', lines)
    lines = print_list('--------------------------', lines)

    votes = list(candidates.values())
    names = list(candidates.keys())
  
    #namelist = []
    for name in names:
        lines = print_list(f'{name}: {(candidates[name] / totalVotes * 100):.3f}% ({candidates[name]})', lines)       
        #namelist.append(name)
        #print(f'{namelist}:{(candidates[name] / totalVotes * 100):.3f}% ({candidates[name]})' )
    
    mostVotes = max(votes)
    mostVotesIdx = votes.index(mostVotes)
    winner = names[mostVotesIdx]

    lines = print_list('--------------------------', lines)
    lines = print_list(f'Winner: {winner}', lines)
    lines = print_list('--------------------------', lines)

    output_file = os.path.join(dirname, "Analysis/PyPoll.txt")
    with open(output_file, "w") as Analysis:
        
        #  Open the output file
        Analysis.write('\n'.join(lines))


