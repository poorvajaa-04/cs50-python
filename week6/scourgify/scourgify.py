'''

In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name 
and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an 
error message.


'''

import csv
import sys

if len(sys.argv) != 3 or not sys.argv[1].endswith(".csv"):
    sys.exit("Invalid arguments.")

try:
    with open(sys.argv[1]) as input, open(sys.argv[2], "w", newline="") as output:
        reader = csv.DictReader(input)
        writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last_name, first_name = row["name"].strip().split(", ")
            writer.writerow(
                {"first": first_name, "last": last_name, "house": row["house"]}
            )

except FileNotFoundError:
    sys.exit("File does not exist.")