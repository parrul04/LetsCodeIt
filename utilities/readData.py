import csv

def getCsvData(filename):
    # CREATE EMPTY LIST TO STORE DATA

    rows = []

    # open the csv file

    filedata = open(filename, "r")

    # reader to itrate through lines in csv file

    reader = csv.reader(filedata)

    # skip the header

    next(reader)

    # add rows from reader to list

    for row in reader:
        rows.append(row)
    return rows



