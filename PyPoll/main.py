import os
import csv
input_file = os.path.join(".","Resources","election_data.csv")
output_file = os.path.join(".","Resources","election_data_analyzed.txt")
voter_id = []
county = []
candidate = []
output_text = []
inputfile_header = []
with open(input_file,newline = "") as inputfile:
    inputfile_header = next(inputfile)
    inputfile_reader = csv.reader(inputfile)
    for column in inputfile_reader:
        voter_id.append(column[0])
        county.append(column[1])
        candidate.append(column[2])

    output_text.append(f"Election Results")
    output_text.append(f"-------------------------")
    output_text.append(f"Total Votes: {len(voter_id)}")
    output_text.append(f"-------------------------")
with open(output_file,mode='w') as outputfile:
    for text in output_text:
        print(text)
        outputfile.write(text)

