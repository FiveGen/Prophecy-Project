
#Notes: Last Updated: 6/1/14
#Still really unhappy with this. Need to look into Reddit's API.

#INITIAL IMPORTS
from datetime import datetime
import time, random
import urllib, mechanize
import re, csv

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
print '* PROPHECY\social\o-reddit-subs.csv' + '\n'
print '----------------------------> LOG'

################################# REDDIT #################################

#BROWSER AGENT SETTINGS
browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-Agent', 'Chrome 3.2')]

#BROWSER DEBUG CODES - SET TRUE FOR ADDITIONAL INFO
browser.set_debug_http(False)
browser.set_debug_redirects(False)
browser.set_debug_responses(False)

#OUTPUT BUCKET
bucket = {}
bucket[0] = '0'
START = '0'

#DEFINING URLS
LOL = 'http://www.reddit.com/r/leagueoflegends'
LOLN = 'League of Legends'

HON = 'http://www.reddit.com/r/HeroesofNewerth/'
HONN = 'Heroes of Newerth'

DO2 = 'http://www.reddit.com/r/dota2'
DO2N = 'Defense of the Ancients 2'

GW2 = 'http://www.reddit.com/r/Guildwars2/'
GW2N = 'Guild Wars 2'

XIV = 'http://www.reddit.com/r/ffxiv/'
XIVN = 'Final Fantasy XIV'

WOW = 'http://www.reddit.com/r/wow/'
WOWN = 'World of Warcraft'

ESO = 'http://www.reddit.com/r/elderscrollsonline'
ESON = 'Elder Scrolls Online'

EQN = 'http://www.reddit.com/r/EQNext'
EQNN = 'EverQuest Next'

WIS = 'http://www.reddit.com/r/WildStar'
WISN = 'WildStar'

#LIST FORM / POSITION
LIST = [START, LOL, HON, DO2, GW2, XIV, WOW, ESO, EQN, WIS]
LISTN = [START, LOLN, HONN, DO2N, GW2N, XIVN, WOWN, ESON, EQNN, WISN]
N = 1

#REPEAT FOR LOOP
while N <= 9:  

    #SLEEP TIMER
    zzz = random.randint(3,10)
    print '[' + str(N) + '] ' + LISTN[N]
    print ' + REQUESTING IN ~' + str(zzz) + ' SECONDS'
    time.sleep(zzz)

    #BROWSER POINTING, HTML SEARCH
    browser.open(LIST[N])
    htmlback = browser.response().read()
    items=re.findall("<span class='number'>.*</span>&#32;<span class='word'>r",htmlback)
    for x in items:
        print ' - SCRAPED: ' + x

    #BECAUSE NO IMMEDIATE UNIQUE CUT-OFF EXISTS, THIS FILTER IS NECESSARY
    x = x.replace("&#32","")

    #FILTER OUT NON-NUMERIC CHARACTERS        
    for char in " abcdefghijklmnopqrstuvwxyz_,.-~'^?!/;:":  
        x = x.replace(char,'')
    for char in ' ABCDEFGHIJKLMNOPQRSTUVWXYZ=#$%")(][><':  
        x = x.replace(char,'')

    print ' - STORING: ' + x + ' IN BUCKET[' + str(N) + ']'
    i = int(x)

    #SAVING FORK#
    if N <=9 :
        bucket[N] = i
        print ''
        
    if bucket[N] == bucket[N-1]:
        bucket[N] = 'n/a'
        print ' - ERROR: DUPLICATE ENTRY; PASSING' + '\n'

    #NEXT#   
    N+=1

#OUTPUT#
print '*!* ATTEMPTING TO SAVE OUTPUT -- WAIT *!*'
with open('o-reddit-subs.csv', 'ab') as fp:
    output = csv.writer(fp, delimiter=',')
    data = [[pingtime, bucket[1], bucket[2], bucket[3], bucket[4], bucket[5], bucket[6], bucket[7], bucket[8], bucket[9]]]
    output.writerows(data)

################################# REDDIT #################################

#WRAP UP#
out_time = datetime.now().replace(microsecond=0)
duration = out_time-in_time
print '----------------------------> SENT'
print '       Completed in: ' + str(duration)
print 'w5748 <---------------------------'
time.sleep(2)
