import os
import csv
import operator
input_file = os.path.join(".","Resources","election_data.csv")
output_file = os.path.join(".","Resources","election_data_analyzed.txt")
voter_id = []
county = []
candidate = []
output_text = []
inputfile_header = []
set_candidate = ()
cnt_candidate = {}
pct_candidate = {}
with open(input_file,newline = "") as inputfile:
    inputfile_header = next(inputfile)
    inputfile_reader = csv.reader(inputfile)
    for column in inputfile_reader:
        voter_id.append(column[0])
        county.append(column[1])
        candidate.append(column[2])
    set_candidate = set(candidate)

    cnt_candidate = {cand:candidate.count(cand) for cand in set_candidate}
    cnt_candidate = dict(sorted(cnt_candidate.items(), key=operator.itemgetter(1),reverse=True))
    winner = sorted(cnt_candidate.items(), key=operator.itemgetter(1),reverse=True)[0][0]
    pct_candidate = {cand:round((candidate.count(cand)/len(candidate))*100,3) for cand in set_candidate}
    print(cnt_candidate)
    print(winner)
    output_text.append(f"Election Results")
    output_text.append(f"-------------------------")
    output_text.append(f"Total Votes: {len(voter_id)}")
    output_text.append(f"-------------------------")
    for kc,vc in cnt_candidate.items():
        output_text.append(f"{kc}: {pct_candidate[kc]}% ({vc})")
    output_text.append(f"-------------------------")
    output_text.append(f"Winner: {winner}")
    output_text.append(f"-------------------------")
with open(output_file,mode='w') as outputfile:
    for text in output_text:
        print(text)
        outputfile.write(text+"\n")

