import os
import csv


filename = 'data.csv'
total_row_count = 0
with open(filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)
        total_row_count += 1

print(f"Total rows processed: {total_row_count}")
    

    