# reading the file line by line
with open("customers.txt","r") as fobj:
    for line in fobj:
        print(line.strip())

# reading the file using fobj.readlines()
with open("customers.txt","r") as fobj:
    print(fobj.readlines())

# read the file using fobj.read()
with open("customers.txt","r") as fobj:
    print(fobj.read()) # single string

# using csv library
import csv
with open("customers.txt","r") as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print(line)

# usingp pandas
import pandas 
df  = pandas.read_csv("customers.txt",header = None)
print(df)