#INITIAL IMPORTS
from datetime import datetime
import time, random, csv
import facebook, json

#DEFINE TIME
pingtime = datetime.now().strftime('%Y-%m-%d %H:%M')
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
print '* PROPHECY\social\o-facebook-likes.csv' + '\n'
print '----------------------------> LOG'

################################# FACEBOOK #################################

#OUTPUT BUCKET
bucket = {}
bucket[0] = '0'
START = '0'

#FACEBOOK API
def pp(o): 
    print json.dumps(o, indent=1)

#GRAPH ACCESS TOKEN (EXTENDED)
g = facebook.GraphAPI('API-KEY-REMOVED')

#PROFILE IDS
LOL = '82061850555'
LOLN = 'League of Legends'

HON = '63037549101'
HONN = 'Heroes of Newerth'

DO2 = '106876872711112'
DO2N = 'Defense of the Ancients 2'

GW2 = '114036714208'
GW2N = 'Guild Wars 2'

XIV = '116214575870'
XIVN = 'Final Fantasy XIV'

WOW = '138011799033'
WOWN = 'World of Warcraft'

ESO = '401899346486771'
ESON = 'Elder Scrolls Online'

EQN = '142045689307777'
EQNN = 'EverQuest Next'

WIS = '138242926249490'
WISN = 'WildStar'

#LIST FORM / POSITION
LIST = [START, LOL, HON, DO2, GW2, XIV, WOW, ESO, EQN, WIS]
LISTN = [START, LOLN, HONN, DO2N, GW2N, XIVN, WOWN, ESON, EQNN, WISN]
N = 1

#REPEAT FOR LOOP
while N <= 9:

    #CONTENT
    def int_format(y): return "{:}".format(y)
    x = int_format(g.get_object(LIST[N])['likes'])
    i = int(x)
    
    print '[' + str(N) + '] ' + LISTN[N]
    print ' + PROFILE ID: ' + LIST[N]
    print ' + LIKES RETREIVED: ' + str(x) + '\n'

    #SAVING FORK#
    if N <=9 :
        bucket[N] = i
        print ''
        
    if bucket[N] == bucket[N-1]:
        bucket[N] = 'n/a'
        print ' - ERROR: DUPLICATE ENTRY; PASSING' + '\n'

    #NEXT   
    N+=1

#OUTPUT#
print '*!* ATTEMPTING TO SAVE OUTPUT -- WAIT *!*'
with open('o-facebook-likes.csv', 'ab') as fp:
    output = csv.writer(fp, delimiter=',')
    data = [[pingtime, bucket[1], bucket[2], bucket[3], bucket[4], bucket[5], bucket[6], bucket[7], bucket[8], bucket[9]]]
    output.writerows(data)

################################# FACEBOOK #################################

#WRAP UP#
out_time = datetime.now().replace(microsecond=0)
duration = out_time-in_time
print '----------------------------> SENT'
print '       Completed in: ' + str(duration)
print 'w5748 <---------------------------'
time.sleep(2)
