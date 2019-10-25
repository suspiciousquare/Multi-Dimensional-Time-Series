import csv
import os

o = "fullcsv.csv"
files = ['mnist_train.csv','mnist_test.csv']
directory = os.getcwd()

with open(o, 'w', newline='') as csvfile: 
    i = 0
    writer = csv.writer(csvfile, delimiter=',') #writes to fullcsv.csv
    
    for filename in os.listdir(directory): #loops through all csvs
        if filename.endswith(".csv") and filename!=o: # makes sure only each cities csv is selected and not fullcsv.csv
 
            readCSV = csv.reader(open(filename), delimiter=',') # reads from file
            for row in readCSV:
                row.insert(0, filename.split()[4]) # adds city name to the beginning of the row

                if len(row) == 27 and row[1] != "Year": # ensures that non-information rows will not be included
                    writer.writerow(row) 

        i+=1

print("done")
