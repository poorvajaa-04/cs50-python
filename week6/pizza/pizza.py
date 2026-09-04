'''

In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio's 
format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the 
library's grid format. If the user does not specify exactly one command-line argument, or if the specified file's name does not end in .csv, 
or if the specified file does not exist, the program should instead exit via sys.exit.

'''

from tabulate import tabulate
import csv
import sys

if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
    sys.exit("Invalid arguments.")

try:
    with open(sys.argv[1]) as file:
        print(tabulate(csv.DictReader(file), headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist.")