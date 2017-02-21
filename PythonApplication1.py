import csv
import urllib


#from urllib.request import urlopen
#f = urlopen("http://winterolympicsmedals.com/medals.csv")


yr= input()
f = open('c:\python34\medals.csv')
csv_f = csv.reader(f)

for row in csv_f:
 if yr == row[0]: 
  print (row)

f.close

