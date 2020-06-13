import csv

with open('[.txt filename]', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('.csv filename', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)