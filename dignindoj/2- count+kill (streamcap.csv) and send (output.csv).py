import csv
import os
from itertools import islice


#IF THE FILE EXISTS (... SHOULD) OPEN AND COUNT THE LINES, BIND TO X
if os.path.isfile(r'streamcap.csv'):
    x = sum(1 for row in csv.reader(open('streamcap.csv')))
    os.remove(r'streamcap.csv')
else:
    x = '0'

#IF THE FILE EXISTS (AGAIN, SHOULD) REMOVE IT
#if os.path.isfile(r'test.csv'):
#   os.remove(r'test.csv')
#else:
#   pass

saveFile = open(r'output.csv','a')
saveFile.write(str(x)+'\n')
saveFile.close()

#15 lines (15 minutes)
#60 lines (60 minutes)
