#INITIAL IMPORTS
from datetime import datetime
import time, random
import urllib
import mechanize
import re

#IMPORT EXCEL READ / WRITE / UTILIS LIBRARIES
from xlrd import open_workbook
from xlutils.copy import copy
import xlwt

#DEFINE TIME
pingtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
in_time = datetime.now().replace(microsecond=0)

#TITLE
print ' _    _  _____  ______ ___  _____ '
print '| |  | ||  ___||___  //   ||  _  |'
print '| |  | ||___ \    / // /| | \ V / '
print '| |/\| |    \ \  / // /_| | / _ \ '
print '\  /\  //\__/ /_/ / \___  || |_| |'
print ' \/  \/ \____/ \_/      |_/\_____/\n'

print '----------------------------> INFO'
print '* ' + pingtime
print '* C:\dignin\output - reddit.xls' + '\n'
print '----------------------------> LOG'


#OPEN OUTPUT.XLS
wb = open_workbook('output - reddit.xls',formatting_info=True)
sheet = wb.sheet_by_name("sheet 1")

#COPY EXISTING CONTENTS / SHEETS
rb = copy(wb)
ws = rb.get_sheet(0)

#BROWSER AGENT SETTINGS
browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-Agent', 'Chrome 3.2')]

#BROWSER DEBUG CODES - SET TRUE FOR ADDITIONAL INFO
browser.set_debug_http(False)
browser.set_debug_redirects(False)
browser.set_debug_responses(False)

#DEFINING URLS
LOL = 'http://www.reddit.com/r/TAR3/'
HON = 'http://www.reddit.com/r/TAR2/'
DO2 = 'http://www.reddit.com/r/TAR1/'

#LIST FORM / POSITION
LIST = [TA1, TA2, TA3]
N = 0

#EXCEL PARAMETERS
ROW = 3
COL = 2
cell = sheet.cell(ROW,2)

#REPEAT FOR LOOP
repeat = 'yes'
while N <= 8:

    #MOVE THE ROW
    try:
        while repeat == 'yes':
            cell = sheet.cell(ROW,2)
            if cell.value != '':
                ROW += 1
            else:
                repeat = 'no'

    except IndexError:
        pass           

    #SLEEP TIMER
    zzz = random.randint(3,10)

    print '[' + str(N) + '] ' + LIST[N]
    print '  + REQUESTING IN ~' + str(zzz) + ' SECONDS'
    time.sleep(zzz)

    #BROWSER POINTING, HTML SEARCH
    browser.open(LIST[N])
    htmlback = browser.response().read()
    items=re.findall('<span class="subscribers"><span class=.*readers</span>',htmlback)
    for x in items:
        print '  - SCRAPE: ' + x

    #BECAUSE NO IMMEDIATE UNIQUE CUT-OFF EXISTS, THIS FILTER IS NECESSARY
    x = x.replace("&#32","")

    #FILTER OUT NON-NUMERIC CHARACTERS        
    for char in " abcdefghijklmnopqrstuvwxyz,.'^?!/;:":  
        x = x.replace(char,'')
    for char in ' ABCDEFGHIJKLMNOPQRSTUVWXYZ=#$%")(][><':  
        x = x.replace(char,'')

    print '  - REPORT: ' + x + '\n'
    i = int(x)
    N+=1

    #WRITE TO THE SPREADSHEET, MOVE THE COLUMN
    ws.write(ROW,COL,i)
    COL += 1

ws.write(ROW,1,pingtime)
rb.save('output - reddit.xls')

out_time = datetime.now().replace(microsecond=0)
duration = out_time-in_time
print '----------------------------> SENT'
print '       Completed in: ' + str(duration)
print 'w5748 <---------------------------'
time.sleep(2)
