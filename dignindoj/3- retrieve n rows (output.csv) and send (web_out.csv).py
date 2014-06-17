import csv
from itertools import islice

x = sum(1 for row in csv.reader(open('output.csv')))
print 'LAST LINE NUM: ' + str(x)

with open('output.csv') as file:
    five = list(file)[x-5]
with open('output.csv') as file:
    four = list(file)[x-4]
with open('output.csv') as file:
    three = list(file)[x-3]
with open('output.csv') as file:
    two = list(file)[x-2]
with open('output.csv') as file:
    one = list(file)[x-1]

with open('web_out.csv', mode = 'w') as file:
    file.write(five)
    file.write(four)
    file.write(three)
    file.write(two)
    file.write(one)

with open("web_out.csv") as fin:
    fin.next()
    total = sum(int(r[1]) for r in csv.reader(fin))

#The number of rows (n) denotes how many minutes we're looking back for the
# web report.

#1 line = 1 min of reporting
#15 lines (15 minutes)
#60 lines (60 minutes) etc.


