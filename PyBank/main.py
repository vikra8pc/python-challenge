import os
import csv

input_file = os.path.join(".", "Resources", "budget_data.csv")
output_file = os.path.join(".", "Resources", "budget_data_analyzed.txt")
date_col = []
profit_loss_col = []
profit_loss_change = []
profit_loss_previous = 0
int_profit_loss_change = 0
greatest_increase_profit = 0
greatest_decrease_profit = 0
greatest_increase_profit_date = ""
greatest_decrease_profit_date = ""
record_counter = 0
output_text = []

with open(input_file, newline="") as budget_data:
    budget_data_reader = csv.reader(budget_data, delimiter=",")
    budget_data_header = next(budget_data_reader)

    for row in budget_data_reader:
        record_counter += 1
        date_col.append(row[0])
        profit_loss_col.append(int(row[1]))
        if record_counter > 1:
            int_profit_loss_change = int(row[1]) - profit_loss_previous
            profit_loss_change.append(int_profit_loss_change)
            if int_profit_loss_change > greatest_increase_profit:
                greatest_increase_profit = int_profit_loss_change
                greatest_increase_profit_date = row[0]
            if int_profit_loss_change < greatest_decrease_profit:
                greatest_decrease_profit = int_profit_loss_change
                greatest_decrease_profit_date = row[0]

        profit_loss_previous = int(row[1])

    output_text.append(f"Financial Analysis")
    output_text.append(f"----------------------------")
    output_text.append(f"Total Months: {len(date_col)}")
    output_text.append(f"Total: ${sum(profit_loss_col)}")
    output_text.append(f"Average  Change: ${round(sum(profit_loss_change)/len(profit_loss_change),2)}")
    output_text.append(f"Greatest Increase in Profits: {greatest_increase_profit_date} (${greatest_increase_profit})")
    output_text.append(f"Greatest Decrease in Profits: {greatest_decrease_profit_date} (${greatest_decrease_profit})")
    for text in output_text:
        print(text)
with open(output_file, 'w') as budget_data_analyzed:
    # budget_data_writer = writer(budget_data_analyzed)
    # budget_data_writer.writerows(output_text)
    for text in output_text:
        print(text)
        budget_data_analyzed.write(text+"\n")
